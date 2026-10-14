import json

TOPICS_DATA = [
    {
        'category': 'Aptitude',
        'subcategory': 'Quantitative',
        'title': 'Percentages, Profit & Loss Master Guide',
        'summary': 'Core mathematical concepts tested in TCS NQT, AMCAT, eLitmus, Cognizant, and CoCubes aptitude tests.',
        'content_markdown': '''### Percentages & Profit/Loss Overview

Percentage represents a fraction out of 100. It forms the base for Profit & Loss, Simple & Compound Interest, and Data Interpretation.

#### Key Concepts & Definitions:
- **Cost Price (CP)**: Price at which an article is purchased.
- **Selling Price (SP)**: Price at which an article is sold.
- **Profit**: SP > CP, Profit = SP - CP
- **Loss**: CP > SP, Loss = CP - SP
- **Profit Percentage**: (Profit / CP) * 100
- **Loss Percentage**: (Loss / CP) * 100
- **Marked Price (MP)**: List price on the label.
- **Discount**: Discount = MP - SP; Discount% = (Discount / MP) * 100

#### Speed Math Multiplier Method:
- If a value increases by 20%, multiply by 1.20.
- If a value decreases by 15%, multiply by 0.85.
- Two successive changes of +a% and +b%:
  Net Change% = a + b + (a * b) / 100

#### Classic Interview Trap:
If cost price of 10 articles equals selling price of 8 articles:
10 * CP = 8 * SP => SP / CP = 10 / 8 = 5 / 4
Gain is 1/4 = 25%. Always equate CP and SP ratios!''',
        'key_formulas': [
            "Profit% is ALWAYS calculated on CP unless explicitly stated otherwise.",
            "Successive discounts: D_net = d1 + d2 - (d1 * d2)/100",
            "Faulty Balance Trick: Gain% = [Error / (True Value - Error)] * 100",
            "If SP is same with x% profit and x% loss: Net Loss% = (x/10)^2"
        ],
        'order_index': 1
    },
    {
        'category': 'Aptitude',
        'subcategory': 'Quantitative',
        'title': 'Time, Speed & Distance / Work & Time',
        'summary': 'Formulas and shortcuts for Relative Speed, Trains, Boats & Streams, and Men-Work-Hours problems.',
        'content_markdown': '''### Time, Speed, Distance & Work Essentials

#### 1. Speed, Time & Distance:
- Distance = Speed * Time
- Conversion: 1 km/hr = 5/18 m/s; 1 m/s = 18/5 km/hr
- **Average Speed**:
  - Equal distance covered at speeds u and v: Avg Speed = 2uv / (u + v)
  - General formula: Total Distance / Total Time
- **Relative Speed**:
  - Same Direction: |u - v|
  - Opposite Direction: u + v

#### 2. Boats & Streams:
- Downstream Speed (D) = u + v (Boat speed + Stream speed)
- Upstream Speed (U) = u - v
- Speed of Boat in Still Water = (D + U) / 2
- Speed of Stream = (D - U) / 2

#### 3. Time & Work:
- If A completes work in n days, 1 day work = 1/n.
- **LCM Method**: Take LCM of days as Total Units of Work. Compute efficiency (units/day) for each person.
- **Chain Rule**: (M1 * D1 * H1) / W1 = (M2 * D2 * H2) / W2''',
        'key_formulas': [
            "Convert km/h to m/s by multiplying with 5/18 immediately.",
            "Train crossing pole: Distance = Length of Train.",
            "Train crossing platform: Distance = Length of Train + Length of Platform.",
            "Negative Work: Drain pipe does negative work (-1/n units/hour)."
        ],
        'order_index': 2
    },
    {
        'category': 'Aptitude',
        'subcategory': 'Logical',
        'title': 'Syllogisms & Seating Arrangements',
        'summary': 'Venn diagram logic rules, deductions, linear & circular seating arrangement strategies.',
        'content_markdown': '''### Logical Reasoning Masterclass

#### 1. Syllogisms (Venn Diagram Method):
- Statements consist of:
  - **All A are B**: Circle A completely inside Circle B.
  - **Some A are B**: Circle A overlaps Circle B.
  - **No A is B**: Circle A and Circle B do not touch.
  - **Some A are not B**: There is a part of A strictly outside B.

#### Complementary Pairs (Either-Or Case):
Either conclusion I or II follows if:
1. Both conclusions are individually false (indefinite).
2. One conclusion is affirmative and the other is negative.
3. Both have the same subject and predicate.
*(Pairs: Some + No, Some + Some not, All + Some not)*

#### 2. Seating Arrangements:
- **Circular Facing Center**: Right = Anti-Clockwise, Left = Clockwise
- **Circular Facing Outside**: Right = Clockwise, Left = Anti-Clockwise
- Always start with definite positions rather than negative constraints.''',
        'key_formulas': [
            "Never assume outside the Venn diagram in Syllogisms.",
            "In circular arrangements, count clockwise vs anti-clockwise carefully.",
            "Linear arrangement facing North: your left is their left.",
            "Linear arrangement facing South: your right is their left."
        ],
        'order_index': 3
    },
    {
        'category': 'Technical',
        'subcategory': 'DBMS',
        'title': 'DBMS & SQL Core Cheat Sheet',
        'summary': 'SQL Joins, ACID Properties, Normalization (1NF to BCNF), Indexing, and Transactions.',
        'content_markdown': '''### Database Management Systems (DBMS)

#### 1. ACID Properties:
- **Atomicity**: All operations in a transaction succeed or all fail ("All or Nothing").
- **Consistency**: Database transitions from one valid state to another, respecting all constraints.
- **Isolation**: Concurrent transactions execute as if they were serial (Read Uncommitted, Read Committed, Repeatable Read, Serializable).
- **Durability**: Once committed, changes survive system crashes (Write Ahead Logging - WAL).

#### 2. SQL Joins Illustrated:
- **INNER JOIN**: Returns records with matching values in both tables.
- **LEFT JOIN**: Returns all records from left table, and matched records from right.
- **RIGHT JOIN**: Returns all records from right table, and matched from left.
- **FULL OUTER JOIN**: Returns all records when there is a match in either table.
- **CROSS JOIN**: Cartesian product of two tables.

#### 3. Database Normalization:
- **1NF**: Atomic values only (no repeating groups/arrays in a column).
- **2NF**: In 1NF + No Partial Dependency (all non-key attributes fully dependent on candidate key).
- **3NF**: In 2NF + No Transitive Dependency (non-prime determining non-prime).
- **BCNF**: Stricter 3NF; for every functional dependency X -> Y, X must be a super key.

#### 4. Indexing:
- **Clustered Index**: Determines physical storage order of rows (Only 1 per table, usually Primary Key).
- **Non-Clustered Index**: Separate B+ Tree structure storing pointers to data rows (Multiple allowed).''',
        'key_formulas': [
            "HAVING vs WHERE: WHERE filters rows before grouping; HAVING filters groups after GROUP BY.",
            "DELETE vs TRUNCATE vs DROP: DELETE is DML (rollback allowed), TRUNCATE is DDL (resets identity), DROP removes table completely.",
            "Candidate Key is minimal Super Key.",
            "SQL Injection prevention: Use Prepared Statements / Parameterized Queries."
        ],
        'order_index': 4
    },
    {
        'category': 'Technical',
        'subcategory': 'OS',
        'title': 'Operating Systems Fundamentals',
        'summary': 'Processes vs Threads, CPU Scheduling, Deadlocks, Paging, Virtual Memory, and Semaphores.',
        'content_markdown': '''### Operating Systems (OS) Essentials

#### 1. Process vs Thread:
- **Process**: Program in execution with isolated memory space. Heavy context switch.
- **Thread**: Lightweight execution unit within process. Shares code, data, heap with parent process; has private stack.

#### 2. Deadlocks (4 Coffman Conditions):
A deadlock occurs if and only if all 4 conditions hold simultaneously:
1. **Mutual Exclusion**: Non-shareable resource.
2. **Hold and Wait**: Process holding resources requests additional ones.
3. **No Preemption**: Resources cannot be forcibly seized.
4. **Circular Wait**: Closed chain of processes each waiting for resource held by next.

> **Deadlock Handling**: Banker algorithm (Safety & resource check), Resource Ordering.

#### 3. Virtual Memory & Paging:
- **Page**: Fixed size block of logical memory.
- **Frame**: Fixed size block of physical RAM.
- **Page Fault**: Occurs when requested page is not in main memory.
- **Page Replacement**: FIFO, LRU (Least Recently Used), Optimal. Belady anomaly occurs in FIFO.
- **Thrashing**: CPU spends more time swapping pages than executing instructions.''',
        'key_formulas': [
            "Process States: New -> Ready -> Running -> Waiting/Blocked -> Terminated.",
            "Mutex has ownership (binary lock). Semaphore is a signaling counter.",
            "Belady Anomaly: Adding more memory frames increases page faults in FIFO.",
            "Spooling: Simultaneous Peripheral Operations On-Line (e.g. Printer queue)."
        ],
        'order_index': 5
    },
    {
        'category': 'Technical',
        'subcategory': 'CN',
        'title': 'Computer Networks & Protocols',
        'summary': 'OSI vs TCP/IP models, TCP 3-way handshake, DNS, HTTP/HTTPS, and Socket connections.',
        'content_markdown': '''### Computer Networks (CN) Guide

#### 1. OSI 7 Layers vs TCP/IP:
1. **Application**: HTTP, DNS, FTP, SMTP
2. **Presentation**: TLS/SSL encryption, compression
3. **Session**: Session establishment, checkpoints
4. **Transport**: TCP, UDP (Port addressing, reliability)
5. **Network**: IP, ICMP, Routing (IP addressing)
6. **Data Link**: MAC addressing, Framing, Error detection
7. **Physical**: Bits, electrical signals, cables

#### 2. TCP vs UDP:
- **TCP**: Connection-oriented, Reliable (ACKs), Flow control, Congestion control. Used in HTTP, SSH, Email.
- **UDP**: Connectionless, Unreliable, Low latency, No handshake. Used in Video streaming, DNS, VoIP, Gaming.

#### 3. TCP 3-Way Handshake:
1. Client -> Server: **SYN** (Synchronize sequence number X)
2. Server -> Client: **SYN + ACK** (Acknowledge X+1, Synchronize sequence number Y)
3. Client -> Server: **ACK** (Acknowledge Y+1)

#### 4. What happens when you type https://google.com?
1. Browser checks local cache (Browser, OS, Router).
2. DNS query sent to Recursive Resolver -> Root Server -> TLD (.com) -> Authoritative Name Server -> Returns IP.
3. TCP 3-way handshake to port 443.
4. TLS Handshake (Cipher suite negotiation, Certificate validation, Session keys exchange).
5. HTTP GET request sent over encrypted TLS channel.
6. Server processes request and returns HTTP 200 OK + HTML/CSS/JS.''',
        'key_formulas': [
            "Subnet Mask /24 = 255.255.255.0, leaves 8 bits for hosts (254 usable IPs).",
            "Private IP Ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.",
            "HTTP Status Codes: 2xx (Success), 3xx (Redirection), 4xx (Client Error), 5xx (Server Error).",
            "ARP (Address Resolution Protocol) maps IP address to physical MAC address."
        ],
        'order_index': 6
    },
    {
        'category': 'HR',
        'subcategory': 'Behavioral',
        'title': 'The STAR Method & Behavioral Interview Mastery',
        'summary': 'Framework for answering situational questions like leadership, failure, conflict, and tight deadlines.',
        'content_markdown': '''### The STAR Method Framework

Every behavioral interview question should be structured using **STAR**:
- **S - Situation**: Set the scene. Briefly give context, company/college project, and initial problem (15-20% of time).
- **T - Task**: What was your specific responsibility or goal? What was at stake? (10-15% of time).
- **A - Action**: What specific steps did YOU take? Highlight your individual leadership, technical decisions, and problem-solving (50-60% of time).
- **R - Result**: What was the quantifiable outcome? What did you learn? Always include numbers (15-20% of time).

---

### Top HR Questions & Winning Blueprints:

#### 1. "Tell me about yourself."
- **Formula**: Past (Education & foundational interest) -> Present (Recent projects/internships & skills) -> Future (Why this specific company & role excites you).
- **Pitfall**: Do not recite your resume chronologically. Keep it under 90 seconds.

#### 2. "Why should we hire you over other candidates?"
- **Blueprint**: Connect your specific technical strengths, fast learning agility, and cultural alignment directly with the job description.
- *Sample Hook*: "Beyond my strong foundation in algorithms and backend engineering, I take ownership. In my previous project, I didn't just write code; I automated test pipelines which reduced build failures by 35%."

#### 3. "Tell me about a time you had a conflict with a team member."
- **Blueprint**: Focus on resolving difference in technical opinion objectively through data and testing, without personal ego.
- *Sample Focus*: "We disagreed on whether to use SQL vs MongoDB. Rather than debating, we benchmarked our queries with 100k records and chose the one that met our latency SLA."

#### 4. "What is your greatest weakness?"
- **Blueprint**: Pick a genuine professional weakness (not a cliché like 'I am a perfectionist') that you have actively taken structured steps to improve.
- *Sample*: "Earlier, I hesitated to delegate tasks because I wanted to ensure perfection. I realized this bottlenecked project velocity, so I started adopting Kanban boards and peer review checklists, which boosted team velocity."''',
        'key_formulas': [
            "Always quantify results (e.g. 'reduced latency by 40%', 'delivered 3 days before deadline').",
            "Never badmouth past teammates, professors, or employers.",
            "Always have 2-3 thoughtful questions prepared for the interviewer at the end.",
            "Salary Question: 'I am excited about this role and confident we can agree on a competitive package aligned with industry standards for this tier.'"
        ],
        'order_index': 7
    }
]

QUESTIONS_DATA = [
    {
        'category': 'Aptitude',
        'subcategory': 'Quantitative',
        'question': 'A vendor sells an article for INR 840, making a profit of 20%. What was the cost price of the article?',
        'options': ['INR 680', 'INR 700', 'INR 720', 'INR 750'],
        'correct_index': 1,
        'explanation': 'SP = CP * (1 + Profit%). 840 = CP * 1.20 => CP = 840 / 1.20 = INR 700.',
        'difficulty': 'Easy'
    },
    {
        'category': 'Aptitude',
        'subcategory': 'Quantitative',
        'question': 'A train 240 m long passes a pole in 24 seconds. How long will it take to pass a platform 650 m long?',
        'options': ['65 seconds', '89 seconds', '90 seconds', '100 seconds'],
        'correct_index': 1,
        'explanation': 'Speed = 240 / 24 = 10 m/s. Total distance to cross platform = 240 + 650 = 890 m. Time = 890 / 10 = 89 seconds.',
        'difficulty': 'Medium'
    },
    {
        'category': 'Aptitude',
        'subcategory': 'Quantitative',
        'question': 'A can complete a piece of work in 12 days, and B can complete it in 18 days. If they work together for 4 days, what fraction of work is left?',
        'options': ['1/3', '4/9', '5/9', '7/18'],
        'correct_index': 1,
        'explanation': 'Total work (LCM 12, 18) = 36 units. Efficiency of A = 3 units/day, B = 2 units/day. In 4 days they do 4 * (3+2) = 20 units. Remaining = 16 units. Fraction = 16/36 = 4/9.',
        'difficulty': 'Medium'
    },
    {
        'category': 'Aptitude',
        'subcategory': 'Logical',
        'question': 'Statements: All engineers are problem solvers. Some problem solvers are designers. Conclusion I: Some engineers are designers. Conclusion II: No engineer is a designer.',
        'options': ['Only I follows', 'Only II follows', 'Either I or II follows', 'Neither I nor II follows'],
        'correct_index': 2,
        'explanation': 'Engineers and designers have no definite overlap given in premises. However conclusion I is "Some" and II is "No" with identical terms. This forms a complementary pair. Hence Either I or II follows.',
        'difficulty': 'Hard'
    },
    {
        'category': 'Aptitude',
        'subcategory': 'Logical',
        'question': 'Pointing to a photograph, Rohit said, "She is the daughter of the only son of my grandfather." How is Rohit related to the girl?',
        'options': ['Uncle', 'Brother', 'Father', 'Cousin'],
        'correct_index': 1,
        'explanation': 'Only son of Rohit grandfather is Rohit father. Daughter of Rohit father is Rohit sister. Thus Rohit is her brother.',
        'difficulty': 'Easy'
    },
    {
        'category': 'Aptitude',
        'subcategory': 'Verbal',
        'question': 'Choose the word most nearly OPPOSITE in meaning to EPHEMERAL:',
        'options': ['Transient', 'Perpetual', 'Fleeting', 'Momentary'],
        'correct_index': 1,
        'explanation': 'Ephemeral means lasting for a very short time. The exact opposite is Perpetual (never-ending or everlasting).',
        'difficulty': 'Easy'
    },
    {
        'category': 'Technical',
        'subcategory': 'DBMS',
        'question': 'Which normal form strictly eliminates transitive functional dependencies?',
        'options': ['1NF', '2NF', '3NF', 'BCNF'],
        'correct_index': 2,
        'explanation': '3NF removes transitive dependencies (where a non-prime attribute determines another non-prime attribute). 2NF removes partial dependencies.',
        'difficulty': 'Medium'
    },
    {
        'category': 'Technical',
        'subcategory': 'DBMS',
        'question': 'Which SQL clause is used to filter records AFTER an aggregation operation like GROUP BY?',
        'options': ['WHERE', 'FILTER', 'HAVING', 'ORDER BY'],
        'correct_index': 2,
        'explanation': 'WHERE filters rows before aggregation; HAVING filters groups after GROUP BY aggregation.',
        'difficulty': 'Easy'
    },
    {
        'category': 'Technical',
        'subcategory': 'OS',
        'question': 'Which of the following condition is NOT one of Coffman four conditions required for a deadlock?',
        'options': ['Mutual Exclusion', 'Hold and Wait', 'Preemption Allowed', 'Circular Wait'],
        'correct_index': 2,
        'explanation': 'Deadlock requires NO preemption. If preemption is allowed, resources can be reclaimed, preventing deadlock.',
        'difficulty': 'Medium'
    },
    {
        'category': 'Technical',
        'subcategory': 'OS',
        'question': 'Which page replacement algorithm suffers from Belady Anomaly (where increasing frame count increases page faults)?',
        'options': ['Optimal', 'LRU (Least Recently Used)', 'FIFO (First-In, First-Out)', 'LFU (Least Frequently Used)'],
        'correct_index': 2,
        'explanation': 'FIFO suffers from Belady anomaly because older pages are discarded regardless of recent reference locality.',
        'difficulty': 'Medium'
    },
    {
        'category': 'Technical',
        'subcategory': 'CN',
        'question': 'At which layer of the OSI model does the TCP protocol operate?',
        'options': ['Application Layer', 'Transport Layer', 'Network Layer', 'Data Link Layer'],
        'correct_index': 1,
        'explanation': 'TCP (and UDP) operates at Layer 4: Transport Layer, providing end-to-end communication and port multiplexing.',
        'difficulty': 'Easy'
    },
    {
        'category': 'HR',
        'subcategory': 'Behavioral',
        'question': 'In the STAR interview response framework, what does the letter "A" stand for?',
        'options': ['Assessment', 'Action', 'Agreement', 'Achievement'],
        'correct_index': 1,
        'explanation': 'STAR stands for Situation, Task, Action, Result. Action describes the specific steps taken by the candidate.',
        'difficulty': 'Easy'
    }
]
