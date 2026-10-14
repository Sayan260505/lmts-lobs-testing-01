# LMT JOBS - Job Portal & Placement Preparation Platform

A modern, full-featured web application combining a **Job Portal**, a multi-module **Placement Preparation Hub**, official **Company Hiring Process Guides**, and a **Dedicated Topic-Wise DSA Sheet**.

---

## 🌟 Key Features

### 1. 💼 Job Portal & Application Tracker
- **Smart Filtering & Search**: Filter by Role, Job Type (Full-time, Internship, Remote), Experience Level (Fresher, 0-1 yrs, 1-3 yrs), and Tech Stacks.
- **Job Details View**: Comprehensive overview of company expectations, eligibility, required skills, and deadlines.
- **One-Click Quick Apply**: Built-in application modal that connects directly to the tracker database.
- **My Tracker Pipeline**: Track status across *Applied*, *In Review*, *Interviewing*, *Offered*, and *Rejected*.
- **Bookmarking**: Star and save jobs with persistent status.

### 2. 📚 Placement Preparation Hub
- **Subjects Covered**:
  - **Quantitative Aptitude**: Percentages, Profit & Loss, Speed-Time-Distance, Work & Time, speed math multipliers.
  - **Logical Reasoning**: Syllogisms with Venn diagrams, Seating Arrangements, Blood Relations.
  - **Verbal Ability**: Vocabulary, antonyms, grammar rules.
  - **Core CS Technical**:
    - **DBMS & SQL**: ACID properties, Joins cheatsheet, Normalization (1NF to BCNF), Clustered/Non-clustered indexing.
    - **Operating Systems**: Processes vs. Threads, Deadlocks (Coffman conditions), Paging & Virtual Memory.
    - **Computer Networks**: OSI vs. TCP/IP layers, TCP 3-way handshake, DNS resolution flow.
  - **HR & Behavioral Round**: Complete guide to the **STAR method** (Situation, Task, Action, Result) with winning answers to top interview questions and traps to avoid.
- **Interactive Timed Practice Quizzes**:
  - 10-minute mock test engine with instant automated grading, percentage accuracy, and question-by-question explanations.

### 3. 🏢 Company Hiring Process & Exam Blueprints
- **Profiles Included**: Google, Amazon, Microsoft, TCS, Infosys, Cognizant.
- **Hiring Blueprint**:
  - Official eligibility guidelines (minimum CGPA, allowed degree branches, backlog rules).
  - Selection rounds progression timeline (Online Assessment -> Technical Screen -> Loop / System Design -> HR / Managerial).
  - Online Assessment patterns and sectional durations.
  - Detailed syllabus focus areas and weightage.
  - Past interview questions from recent campus drives.
  - Pro tips from placed alumni.
- **Interactive Eligibility Checker**: Enter your CGPA, Branch, and Backlog count to test your eligibility against the company's real cutoff rules.

### 4. ⚡ Dedicated Topic-Wise DSA Sheet
- **Categorized Problem Sheets**: Arrays, Strings, Linked Lists, Stacks & Queues, Trees & BST, Graphs, Dynamic Programming, Backtracking, and Bit Manipulation.
- **Optimal Solutions in 4 Languages**: Every problem comes with full solutions in **Python 3**, **C++ 17**, **Java**, and **JavaScript** alongside step-by-step Intuition and Time/Space Complexity analysis.
- **Direct Links**: Instant links to LeetCode and GeeksforGeeks problems.
- **Personal Notes**: Save your own revision hints and edge cases directly in SQLite.
- **Progress Analytics**: Real-time progress bar, solved counters by difficulty (Easy, Medium, Hard), and status filters (Todo, Doing, Solved, Review Later).

---

## 🚀 How to Run the Platform

### Prerequisites
- Python 3.10+ (Tested on Python 3.14)
- Packages installed: `Flask`, `flask-cors` (Included in standard environment)

### Launching the Application
1. Double-click `run.bat` or run:
   ```bash
   py app.py
   ```
2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

### Re-seeding the Database (Optional)
If you wish to reset or re-seed the SQLite database with sample data:
```bash
py seed_data.py
```
