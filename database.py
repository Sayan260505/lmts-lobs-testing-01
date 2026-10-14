import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), 'hireprep.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Jobs Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        company TEXT NOT NULL,
        logo_url TEXT,
        location TEXT NOT NULL,
        job_type TEXT NOT NULL, -- Full-time, Internship, Remote, Contract
        experience_level TEXT NOT NULL, -- Fresher, 0-1 Years, 1-3 Years, 3+ Years
        salary_range TEXT NOT NULL,
        skills TEXT NOT NULL, -- Comma-separated or JSON
        description TEXT NOT NULL,
        requirements TEXT NOT NULL,
        deadline TEXT,
        posted_date TEXT,
        is_featured INTEGER DEFAULT 0,
        apply_url TEXT
    )
    ''')

    # Job Applications Tracker Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER NOT NULL,
        candidate_name TEXT NOT NULL,
        candidate_email TEXT NOT NULL,
        portfolio_url TEXT,
        resume_name TEXT,
        status TEXT DEFAULT 'Applied', -- Applied, In Review, Interviewing, Offered, Rejected
        applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        notes TEXT,
        FOREIGN KEY (job_id) REFERENCES jobs (id)
    )
    ''')

    # Saved/Bookmarked Jobs
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS saved_jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER UNIQUE NOT NULL,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (job_id) REFERENCES jobs (id)
    )
    ''')

    # Preparation Topics & Notes (Aptitude, Core Technical, HR)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS prep_topics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL, -- Aptitude, Technical, HR
        subcategory TEXT NOT NULL, -- Quant, Logical, Verbal, DBMS, OS, CN, OOP, System Design, Behavioral
        title TEXT NOT NULL,
        summary TEXT NOT NULL,
        content_markdown TEXT NOT NULL,
        key_formulas_or_points TEXT, -- JSON array
        order_index INTEGER DEFAULT 0
    )
    ''')

    # Practice / Quiz Questions
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS practice_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL, -- Aptitude, Technical, HR
        subcategory TEXT NOT NULL,
        question TEXT NOT NULL,
        options_json TEXT NOT NULL, -- JSON array of 4 options
        correct_index INTEGER NOT NULL, -- 0 to 3
        explanation TEXT NOT NULL,
        difficulty TEXT DEFAULT 'Medium' -- Easy, Medium, Hard
    )
    ''')

    # Company Hiring Process Archives
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        category TEXT NOT NULL, -- Product, Service, FinTech
        badge TEXT, -- Tier-1, Mass Recruiter, Fortune 500
        logo_url TEXT,
        overview TEXT NOT NULL,
        package_info TEXT NOT NULL, -- e.g. "INR 18 - 45 LPA" or "INR 3.5 - 9.0 LPA"
        eligibility_criteria TEXT NOT NULL, -- JSON object
        exam_pattern TEXT NOT NULL, -- JSON array of sections
        rounds_breakdown TEXT NOT NULL, -- JSON array of round objects
        syllabus TEXT NOT NULL, -- JSON object with topics
        past_questions TEXT NOT NULL, -- JSON array
        pro_tips TEXT NOT NULL -- JSON array
    )
    ''')

    # Dedicated Topic-wise DSA Problems
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dsa_problems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT NOT NULL, -- Arrays, Strings, Linked List, Stack & Queue, Trees, Graphs, DP, etc.
        subtopic TEXT,
        title TEXT NOT NULL,
        difficulty TEXT NOT NULL, -- Easy, Medium, Hard
        leetcode_url TEXT,
        gfg_url TEXT,
        intuition TEXT NOT NULL,
        time_complexity TEXT NOT NULL,
        space_complexity TEXT NOT NULL,
        python_code TEXT NOT NULL,
        cpp_code TEXT NOT NULL,
        java_code TEXT NOT NULL,
        js_code TEXT NOT NULL
    )
    ''')

    # User DSA Progress Tracker
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_dsa_progress (
        problem_id INTEGER PRIMARY KEY,
        status TEXT DEFAULT 'unsolved', -- unsolved, in_progress, solved, review
        notes TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (problem_id) REFERENCES dsa_problems (id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")
