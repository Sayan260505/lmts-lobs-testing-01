import os
import json
import sqlite3
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from database import get_db, init_db

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

# ----------------- DASHBOARD STATS -----------------
@app.route('/api/dashboard/stats', methods=['GET'])
def get_dashboard_stats():
    conn = get_db()
    cursor = conn.cursor()

    total_jobs = cursor.execute('SELECT COUNT(*) FROM jobs').fetchone()[0]
    total_apps = cursor.execute('SELECT COUNT(*) FROM applications').fetchone()[0]
    total_dsa = cursor.execute('SELECT COUNT(*) FROM dsa_problems').fetchone()[0]
    
    solved_dsa = cursor.execute('''
        SELECT COUNT(*) FROM user_dsa_progress WHERE status = 'solved'
    ''').fetchone()[0]

    dsa_breakdown = cursor.execute('''
        SELECT p.difficulty, COUNT(u.problem_id) as count
        FROM user_dsa_progress u
        JOIN dsa_problems p ON u.problem_id = p.id
        WHERE u.status = 'solved'
        GROUP BY p.difficulty
    ''').fetchall()

    breakdown_dict = {'Easy': 0, 'Medium': 0, 'Hard': 0}
    for row in dsa_breakdown:
        breakdown_dict[row['difficulty']] = row['count']

    total_companies = cursor.execute('SELECT COUNT(*) FROM companies').fetchone()[0]
    total_topics = cursor.execute('SELECT COUNT(*) FROM prep_topics').fetchone()[0]

    conn.close()
    return jsonify({
        'total_jobs': total_jobs,
        'total_applications': total_apps,
        'total_dsa': total_dsa,
        'solved_dsa': solved_dsa,
        'dsa_breakdown': breakdown_dict,
        'total_companies': total_companies,
        'total_prep_topics': total_topics
    })

# ----------------- JOBS API -----------------
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    search = request.args.get('search', '').strip().lower()
    job_type = request.args.get('type', '').strip()
    experience = request.args.get('experience', '').strip()

    conn = get_db()
    cursor = conn.cursor()

    query = '''
        SELECT j.*, 
            CASE WHEN s.id IS NOT NULL THEN 1 ELSE 0 END as is_saved,
            a.status as application_status
        FROM jobs j
        LEFT JOIN saved_jobs s ON j.id = s.job_id
        LEFT JOIN applications a ON j.id = a.job_id
        WHERE 1=1
    '''
    params = []

    if search:
        query += ''' AND (
            LOWER(j.title) LIKE ? OR 
            LOWER(j.company) LIKE ? OR 
            LOWER(j.skills) LIKE ? OR
            LOWER(j.location) LIKE ?
        )'''
        term = f'%{search}%'
        params.extend([term, term, term, term])

    if job_type and job_type != 'All':
        query += ' AND j.job_type = ?'
        params.append(job_type)

    if experience and experience != 'All':
        query += ' AND j.experience_level LIKE ?'
        params.append(f'%{experience}%')

    query += ' ORDER BY j.is_featured DESC, j.id DESC'

    rows = cursor.execute(query, params).fetchall()
    jobs = [dict(r) for r in rows]
    conn.close()
    return jsonify(jobs)

@app.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_job_detail(job_id):
    conn = get_db()
    cursor = conn.cursor()
    row = cursor.execute('''
        SELECT j.*, 
            CASE WHEN s.id IS NOT NULL THEN 1 ELSE 0 END as is_saved,
            a.status as application_status
        FROM jobs j
        LEFT JOIN saved_jobs s ON j.id = s.job_id
        LEFT JOIN applications a ON j.id = a.job_id
        WHERE j.id = ?
    ''', (job_id,)).fetchone()
    conn.close()

    if not row:
        return jsonify({'error': 'Job not found'}), 404
    return jsonify(dict(row))

@app.route('/api/jobs/apply', methods=['POST'])
def apply_job():
    data = request.json or {}
    job_id = data.get('job_id')
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    portfolio = data.get('portfolio', '').strip()
    resume_name = data.get('resume_name', 'Uploaded_Resume.pdf')
    notes = data.get('notes', '').strip()

    if not job_id or not name or not email:
        return jsonify({'error': 'job_id, name, and email are required'}), 400

    conn = get_db()
    cursor = conn.cursor()

    existing = cursor.execute('SELECT id FROM applications WHERE job_id = ?', (job_id,)).fetchone()
    if existing:
        conn.close()
        return jsonify({'error': 'You have already applied for this position!'}), 400

    cursor.execute('''
        INSERT INTO applications (job_id, candidate_name, candidate_email, portfolio_url, resume_name, status, notes)
        VALUES (?, ?, ?, ?, ?, 'Applied', ?)
    ''', (job_id, name, email, portfolio, resume_name, notes))
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': 'Application submitted successfully!'})

@app.route('/api/applications', methods=['GET'])
def get_applications():
    conn = get_db()
    cursor = conn.cursor()
    rows = cursor.execute('''
        SELECT a.*, j.title, j.company, j.location, j.logo_url, j.salary_range, j.job_type
        FROM applications a
        JOIN jobs j ON a.job_id = j.id
        ORDER BY a.applied_at DESC
    ''').fetchall()
    apps = [dict(r) for r in rows]
    conn.close()
    return jsonify(apps)

@app.route('/api/applications/<int:app_id>/status', methods=['PATCH'])
def update_application_status(app_id):
    data = request.json or {}
    status = data.get('status')
    if not status:
        return jsonify({'error': 'status required'}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE applications SET status = ? WHERE id = ?', (status, app_id))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/jobs/toggle-save', methods=['POST'])
def toggle_save_job():
    data = request.json or {}
    job_id = data.get('job_id')
    if not job_id:
        return jsonify({'error': 'job_id required'}), 400

    conn = get_db()
    cursor = conn.cursor()
    existing = cursor.execute('SELECT id FROM saved_jobs WHERE job_id = ?', (job_id,)).fetchone()
    if existing:
        cursor.execute('DELETE FROM saved_jobs WHERE job_id = ?', (job_id,))
        is_saved = False
    else:
        cursor.execute('INSERT INTO saved_jobs (job_id) VALUES (?)', (job_id,))
        is_saved = True
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'is_saved': is_saved})

# ----------------- PREPARATION HUB API -----------------
@app.route('/api/prep/topics', methods=['GET'])
def get_prep_topics():
    category = request.args.get('category', '').strip()
    conn = get_db()
    cursor = conn.cursor()

    if category and category != 'All':
        rows = cursor.execute('''
            SELECT id, category, subcategory, title, summary, key_formulas_or_points, order_index
            FROM prep_topics
            WHERE category = ?
            ORDER BY order_index ASC
        ''', (category,)).fetchall()
    else:
        rows = cursor.execute('''
            SELECT id, category, subcategory, title, summary, key_formulas_or_points, order_index
            FROM prep_topics
            ORDER BY category, order_index ASC
        ''').fetchall()

    topics = []
    for r in rows:
        item = dict(r)
        if item['key_formulas_or_points']:
            try:
                item['key_formulas_or_points'] = json.loads(item['key_formulas_or_points'])
            except:
                pass
        topics.append(item)
    conn.close()
    return jsonify(topics)

@app.route('/api/prep/topics/<int:topic_id>', methods=['GET'])
def get_prep_topic_detail(topic_id):
    conn = get_db()
    cursor = conn.cursor()
    row = cursor.execute('SELECT * FROM prep_topics WHERE id = ?', (topic_id,)).fetchone()
    conn.close()
    if not row:
        return jsonify({'error': 'Topic not found'}), 404

    item = dict(row)
    if item['key_formulas_or_points']:
        try:
            item['key_formulas_or_points'] = json.loads(item['key_formulas_or_points'])
        except:
            pass
    return jsonify(item)

@app.route('/api/prep/quiz', methods=['GET'])
def get_quiz():
    category = request.args.get('category', '').strip()
    conn = get_db()
    cursor = conn.cursor()

    if category and category != 'All':
        rows = cursor.execute('''
            SELECT id, category, subcategory, question, options_json, difficulty
            FROM practice_questions
            WHERE category = ?
            ORDER BY RANDOM() LIMIT 10
        ''', (category,)).fetchall()
    else:
        rows = cursor.execute('''
            SELECT id, category, subcategory, question, options_json, difficulty
            FROM practice_questions
            ORDER BY RANDOM() LIMIT 10
        ''').fetchall()

    questions = []
    for r in rows:
        item = dict(r)
        item['options'] = json.loads(item['options_json'])
        del item['options_json']
        questions.append(item)
    conn.close()
    return jsonify(questions)

@app.route('/api/prep/quiz/submit', methods=['POST'])
def submit_quiz():
    data = request.json or {}
    answers = data.get('answers', {}) # dict of question_id -> selected_index

    if not answers:
        return jsonify({'error': 'No answers submitted'}), 400

    q_ids = [int(k) for k in answers.keys()]
    conn = get_db()
    cursor = conn.cursor()

    placeholders = ','.join('?' for _ in q_ids)
    rows = cursor.execute(f'''
        SELECT id, question, correct_index, explanation, options_json
        FROM practice_questions
        WHERE id IN ({placeholders})
    ''', q_ids).fetchall()

    correct_count = 0
    results = []
    for r in rows:
        qid = r['id']
        selected = answers.get(str(qid))
        if selected is not None:
            selected = int(selected)
        correct = (selected == r['correct_index'])
        if correct:
            correct_count += 1
        
        results.append({
            'question_id': qid,
            'question': r['question'],
            'selected_index': selected,
            'correct_index': r['correct_index'],
            'is_correct': correct,
            'explanation': r['explanation'],
            'options': json.loads(r['options_json'])
        })

    conn.close()
    total = len(rows)
    percentage = round((correct_count / total * 100) if total else 0, 1)

    return jsonify({
        'total': total,
        'correct': correct_count,
        'percentage': percentage,
        'results': results
    })

# ----------------- COMPANIES API -----------------
@app.route('/api/companies', methods=['GET'])
def get_companies():
    category = request.args.get('category', '').strip()
    conn = get_db()
    cursor = conn.cursor()

    if category and category != 'All':
        rows = cursor.execute('SELECT * FROM companies WHERE category = ? ORDER BY id ASC', (category,)).fetchall()
    else:
        rows = cursor.execute('SELECT * FROM companies ORDER BY id ASC').fetchall()

    companies = []
    for r in rows:
        item = dict(r)
        item['eligibility_criteria'] = json.loads(item['eligibility_criteria'])
        item['exam_pattern'] = json.loads(item['exam_pattern'])
        item['rounds_breakdown'] = json.loads(item['rounds_breakdown'])
        item['syllabus'] = json.loads(item['syllabus'])
        item['past_questions'] = json.loads(item['past_questions'])
        item['pro_tips'] = json.loads(item['pro_tips'])
        companies.append(item)

    conn.close()
    return jsonify(companies)

@app.route('/api/companies/<int:company_id>', methods=['GET'])
def get_company_detail(company_id):
    conn = get_db()
    cursor = conn.cursor()
    row = cursor.execute('SELECT * FROM companies WHERE id = ?', (company_id,)).fetchone()
    conn.close()

    if not row:
        return jsonify({'error': 'Company not found'}), 404

    item = dict(row)
    item['eligibility_criteria'] = json.loads(item['eligibility_criteria'])
    item['exam_pattern'] = json.loads(item['exam_pattern'])
    item['rounds_breakdown'] = json.loads(item['rounds_breakdown'])
    item['syllabus'] = json.loads(item['syllabus'])
    item['past_questions'] = json.loads(item['past_questions'])
    item['pro_tips'] = json.loads(item['pro_tips'])
    return jsonify(item)

@app.route('/api/companies/check-eligibility', methods=['POST'])
def check_eligibility():
    data = request.json or {}
    company_id = data.get('company_id')
    user_cgpa = float(data.get('cgpa', 0.0))
    user_branch = data.get('branch', '').strip().upper()
    user_backlogs = int(data.get('backlogs', 0))

    conn = get_db()
    cursor = conn.cursor()
    row = cursor.execute('SELECT name, eligibility_criteria FROM companies WHERE id = ?', (company_id,)).fetchone()
    conn.close()

    if not row:
        return jsonify({'error': 'Company not found'}), 404

    criteria = json.loads(row['eligibility_criteria'])
    company_name = row['name']

    # Evaluation logic
    min_cgpa_req = 6.0
    if '7.0' in criteria.get('min_cgpa', ''):
        min_cgpa_req = 7.0
    elif '6.5' in criteria.get('min_cgpa', ''):
        min_cgpa_req = 6.5

    reasons = []
    eligible = True

    if user_cgpa < min_cgpa_req:
        eligible = False
        reasons.append(f'CGPA ({user_cgpa}) is lower than requirement ({min_cgpa_req} CGPA).')
    else:
        reasons.append(f'CGPA ({user_cgpa}) meets or exceeds the required {min_cgpa_req} CGPA threshold.')

    if user_backlogs > 0:
        if 'zero' in criteria.get('backlog_policy', '').lower() or 'no active' in criteria.get('backlog_policy', '').lower():
            if user_backlogs > 0:
                eligible = False
                reasons.append(f'Active backlogs ({user_backlogs}) present. Policy states: {criteria.get("backlog_policy")}.')
        elif 'maximum 1' in criteria.get('backlog_policy', '').lower():
            if user_backlogs > 1:
                eligible = False
                reasons.append(f'Active backlogs ({user_backlogs}) exceed maximum allowed (1).')
            else:
                reasons.append('Active backlogs within allowed threshold (max 1 permitted).')
    else:
        reasons.append('Zero active backlogs satisfies all criteria.')

    return jsonify({
        'company': company_name,
        'is_eligible': eligible,
        'details': reasons,
        'criteria': criteria
    })

# ----------------- DEDICATED DSA SHEET API -----------------
@app.route('/api/dsa/sheet', methods=['GET'])
def get_dsa_sheet():
    topic = request.args.get('topic', '').strip()
    difficulty = request.args.get('difficulty', '').strip()
    search = request.args.get('search', '').strip().lower()
    status_filter = request.args.get('status', '').strip()

    conn = get_db()
    cursor = conn.cursor()

    query = '''
        SELECT p.*, COALESCE(u.status, 'unsolved') as user_status, u.notes as user_notes
        FROM dsa_problems p
        LEFT JOIN user_dsa_progress u ON p.id = u.problem_id
        WHERE 1=1
    '''
    params = []

    if topic and topic != 'All':
        query += ' AND p.topic = ?'
        params.append(topic)

    if difficulty and difficulty != 'All':
        query += ' AND p.difficulty = ?'
        params.append(difficulty)

    if search:
        query += ' AND (LOWER(p.title) LIKE ? OR LOWER(p.subtopic) LIKE ?)'
        params.extend([f'%{search}%', f'%{search}%'])

    if status_filter and status_filter != 'All':
        if status_filter == 'unsolved':
            query += " AND (u.status IS NULL OR u.status = 'unsolved')"
        else:
            query += ' AND u.status = ?'
            params.append(status_filter)

    query += ' ORDER BY p.id ASC'

    rows = cursor.execute(query, params).fetchall()
    problems = [dict(r) for r in rows]

    # Get distinct topics list and topic-level stats
    all_topics = cursor.execute('''
        SELECT topic, 
               COUNT(*) as total,
               SUM(CASE WHEN u.status = 'solved' THEN 1 ELSE 0 END) as solved
        FROM dsa_problems p
        LEFT JOIN user_dsa_progress u ON p.id = u.problem_id
        GROUP BY topic
        ORDER BY topic ASC
    ''').fetchall()

    topics_summary = [dict(t) for t in all_topics]

    conn.close()
    return jsonify({
        'problems': problems,
        'topics_summary': topics_summary
    })

@app.route('/api/dsa/status', methods=['POST'])
def update_dsa_status():
    data = request.json or {}
    problem_id = data.get('problem_id')
    status = data.get('status', 'unsolved')
    notes = data.get('notes')

    if not problem_id:
        return jsonify({'error': 'problem_id required'}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_dsa_progress (problem_id, status, notes, updated_at)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(problem_id) DO UPDATE SET
            status = excluded.status,
            notes = COALESCE(excluded.notes, user_dsa_progress.notes),
            updated_at = CURRENT_TIMESTAMP
    ''', (problem_id, status, notes))

    conn.commit()
    conn.close()
    return jsonify({'success': True, 'problem_id': problem_id, 'status': status})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting HirePrep & Job Portal on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
