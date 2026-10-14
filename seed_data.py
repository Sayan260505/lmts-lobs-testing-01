import json
import sqlite3
import os
from database import get_db, init_db
from data_jobs import JOBS_DATA
from data_topics import TOPICS_DATA, QUESTIONS_DATA
from data_companies import COMPANIES_DATA
from data_dsa import DSA_PROBLEMS_DATA

def seed_all():
    init_db()
    conn = get_db()
    cursor = conn.cursor()

    # Clear existing records
    cursor.execute('DELETE FROM jobs')
    cursor.execute('DELETE FROM prep_topics')
    cursor.execute('DELETE FROM practice_questions')
    cursor.execute('DELETE FROM companies')
    cursor.execute('DELETE FROM dsa_problems')
    cursor.execute('DELETE FROM saved_jobs')
    cursor.execute('DELETE FROM applications')
    cursor.execute('DELETE FROM user_dsa_progress')
    try:
        cursor.execute('DELETE FROM sqlite_sequence')
    except Exception:
        pass

    print(f"Inserting {len(JOBS_DATA)} Jobs...")
    for j in JOBS_DATA:
        cursor.execute('''
        INSERT INTO jobs (title, company, logo_url, location, job_type, experience_level, salary_range, skills, description, requirements, deadline, posted_date, is_featured, apply_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            j['title'], j['company'], j['logo_url'], j['location'], j['job_type'],
            j['experience_level'], j['salary_range'], j['skills'], j['description'],
            j['requirements'], j['deadline'], j['posted_date'], j['is_featured'], j['apply_url']
        ))

    print(f"Inserting {len(TOPICS_DATA)} Preparation Topics...")
    for t in TOPICS_DATA:
        cursor.execute('''
        INSERT INTO prep_topics (category, subcategory, title, summary, content_markdown, key_formulas_or_points, order_index)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            t['category'], t['subcategory'], t['title'], t['summary'],
            t['content_markdown'], json.dumps(t['key_formulas']), t['order_index']
        ))

    print(f"Inserting {len(QUESTIONS_DATA)} Practice Questions...")
    for q in QUESTIONS_DATA:
        cursor.execute('''
        INSERT INTO practice_questions (category, subcategory, question, options_json, correct_index, explanation, difficulty)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            q['category'], q['subcategory'], q['question'],
            json.dumps(q['options']), q['correct_index'], q['explanation'], q['difficulty']
        ))

    print(f"Inserting {len(COMPANIES_DATA)} Company Guides...")
    for c in COMPANIES_DATA:
        cursor.execute('''
        INSERT INTO companies (name, category, badge, logo_url, overview, package_info, eligibility_criteria, exam_pattern, rounds_breakdown, syllabus, past_questions, pro_tips)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            c['name'], c['category'], c['badge'], c['logo_url'], c['overview'],
            c['package_info'], json.dumps(c['eligibility_criteria']),
            json.dumps(c['exam_pattern']), json.dumps(c['rounds_breakdown']),
            json.dumps(c['syllabus']), json.dumps(c['past_questions']),
            json.dumps(c['pro_tips'])
        ))

    print(f"Inserting {len(DSA_PROBLEMS_DATA)} DSA Problems...")
    for d in DSA_PROBLEMS_DATA:
        cursor.execute('''
        INSERT INTO dsa_problems (topic, subtopic, title, difficulty, leetcode_url, gfg_url, intuition, time_complexity, space_complexity, python_code, cpp_code, java_code, js_code)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            d['topic'], d['subtopic'], d['title'], d['difficulty'],
            d['leetcode_url'], d['gfg_url'], d['intuition'],
            d['time_complexity'], d['space_complexity'],
            d['python_code'], d['cpp_code'], d['java_code'], d['js_code']
        ))

    print("Inserting Sample User Progress & Applications...")
    inserted_job_ids = [r[0] for r in cursor.execute('SELECT id FROM jobs ORDER BY id ASC LIMIT 4').fetchall()]
    if inserted_job_ids:
        cursor.execute('''
        INSERT INTO applications (job_id, candidate_name, candidate_email, portfolio_url, resume_name, status, notes)
        VALUES (?, 'Alex Sharma', 'alex.sharma@example.com', 'https://github.com/alexsharma', 'Alex_Sharma_SDE_Resume.pdf', 'Interviewing', 'Technical Round 1 scheduled for this Friday.')
        ''', (inserted_job_ids[0],))
        if len(inserted_job_ids) > 1:
            cursor.execute('''
            INSERT INTO applications (job_id, candidate_name, candidate_email, portfolio_url, resume_name, status, notes)
            VALUES (?, 'Alex Sharma', 'alex.sharma@example.com', 'https://github.com/alexsharma', 'Alex_Sharma_SDE_Resume.pdf', 'Applied', 'TCS NQT registration code verified.')
            ''', (inserted_job_ids[1],))
            cursor.execute('INSERT INTO saved_jobs (job_id) VALUES (?)', (inserted_job_ids[1],))
        if len(inserted_job_ids) > 2:
            cursor.execute('INSERT INTO saved_jobs (job_id) VALUES (?)', (inserted_job_ids[2],))

    inserted_prob_ids = [r[0] for r in cursor.execute('SELECT id FROM dsa_problems ORDER BY id ASC LIMIT 3').fetchall()]
    if inserted_prob_ids:
        cursor.execute("INSERT INTO user_dsa_progress (problem_id, status, notes) VALUES (?, 'solved', 'Solved using HashMap lookup in O(N) time.')", (inserted_prob_ids[0],))
        if len(inserted_prob_ids) > 1:
            cursor.execute("INSERT INTO user_dsa_progress (problem_id, status, notes) VALUES (?, 'solved', 'Kadane algorithm mastered; reset curr_sum when it drops below zero.')", (inserted_prob_ids[1],))
        if len(inserted_prob_ids) > 2:
            cursor.execute("INSERT INTO user_dsa_progress (problem_id, status, notes) VALUES (?, 'in_progress', 'Review edge cases with non-increasing prices.')", (inserted_prob_ids[2],))

    conn.commit()
    conn.close()
    print("All seed data successfully committed to SQLite database!")

if __name__ == '__main__':
    seed_all()
