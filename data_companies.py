import json

COMPANIES_DATA = [
    {
        'name': 'Google',
        'category': 'Product',
        'badge': 'Tier-1 Global Tech',
        'logo_url': 'https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg',
        'overview': 'Google focuses on algorithmic efficiency, clean code quality, scalable architecture, and Googliness (collaborative values).',
        'package_info': 'INR 28 - 45 LPA (Base + Stock + Performance Bonus)',
        'eligibility_criteria': {
            'min_cgpa': '7.0 CGPA / 70%',
            'eligible_branches': ['CSE', 'IT', 'ECE', 'EE', 'Mathematics & Computing'],
            'backlog_policy': 'No active backlogs at time of joining',
            'gap_year_allowed': 'Up to 1 year gap with valid justification'
        },
        'exam_pattern': [
            {'section': 'Online Assessment (Google Online Challenge)', 'duration': '60 mins', 'questions': '2 LeetCode Medium/Hard algorithmic questions', 'platform': 'HackerEarth'},
            {'section': 'Technical Interview 1', 'duration': '45 mins', 'questions': 'Data Structures & Algorithms (Trees/Graphs/DP)'},
            {'section': 'Technical Interview 2', 'duration': '45 mins', 'questions': 'Advanced DSA & Optimization'},
            {'section': 'Technical Interview 3', 'duration': '45 mins', 'questions': 'System Design / Concurrency / Problem Solving'},
            {'section': 'Googliness & Leadership', 'duration': '45 mins', 'questions': 'Behavioral & Culture fit'}
        ],
        'rounds_breakdown': [
            {'round': 1, 'name': 'Google Online Challenge (GOC)', 'type': 'Online Assessment', 'desc': '2 algorithmic coding questions focused on dynamic programming, graph traversal, and segment trees.'},
            {'round': 2, 'name': 'Technical Screen', 'type': 'Video Call + Google Docs', 'desc': 'Live coding without auto-complete. Code clarity, edge cases, and runtime complexity matter.'},
            {'round': 3, 'name': 'Onsite Technical Loop (3 Rounds)', 'type': 'Coding & Algorithms', 'desc': 'Deep dive into complex data structures, graph algorithms, and time-space tradeoffs.'},
            {'round': 4, 'name': 'Googliness & Managerial', 'type': 'Behavioral', 'desc': 'Evaluates teamwork, intellectual humility, navigating ambiguity, and ethical decision making.'}
        ],
        'syllabus': {
            'DSA': ['Graphs (Dijkstra, BFS/DFS)', 'Dynamic Programming (2D, Bitmask)', 'Trie & String Hashing', 'Disjoint Set Union (DSU)'],
            'CS_Fundamentals': ['Operating Systems (Threads, Memory)', 'Computer Networks', 'Distributed Computing'],
            'Behavioral': ['Handling ambiguous problems', 'Conflict resolution', 'Leading without authority']
        },
        'past_questions': [
            'Given a stream of integers, design a data structure that finds median in O(1) time.',
            'Word Ladder II: Find all shortest transformation sequences.',
            'Design a hit counter that records hits in past 5 minutes.',
            'Serialize and Deserialize a Binary Tree with minimal memory footprint.'
        ],
        'pro_tips': [
            'Practice writing syntax-correct code on Google Docs without IDE highlighting.',
            'Think out loud: interviewers grade your thought process more than final answer.',
            'Always verify edge cases (null inputs, overflows, duplicate keys) before declaring code complete.'
        ]
    },
    {
        'name': 'Amazon',
        'category': 'Product',
        'badge': 'Big Tech / Cloud Leader',
        'logo_url': 'https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg',
        'overview': 'Amazon heavily values their 16 Leadership Principles alongside core DSA and Low Level Design.',
        'package_info': 'INR 22 - 35 LPA (Base + Sign-on bonus + RSU)',
        'eligibility_criteria': {
            'min_cgpa': '6.5 CGPA / 65%',
            'eligible_branches': ['All Engineering branches eligible if coding skills are strong'],
            'backlog_policy': 'Zero active backlogs at date of joining',
            'gap_year_allowed': 'Allowed with clear explanation'
        },
        'exam_pattern': [
            {'section': 'Online Assessment Round 1', 'duration': '90 mins', 'questions': '2 DSA Coding Problems (HackerRank)'},
            {'section': 'Online Assessment Round 2', 'duration': '20 mins', 'questions': 'Work Style Assessment (Amazon 16 LPs situational judgement)'},
            {'section': 'Technical Interview 1', 'duration': '60 mins', 'questions': '1-2 DSA Coding questions + 2 LP questions'},
            {'section': 'Technical Interview 2', 'duration': '60 mins', 'questions': 'Object Oriented Design / LLD + 2 LP questions'},
            {'section': 'Bar Raiser Interview', 'duration': '60 mins', 'questions': 'Challenging Problem Solving + Deep Behavioral LP probe'}
        ],
        'rounds_breakdown': [
            {'round': 1, 'name': 'Online Assessment (OA 1 & 2)', 'type': 'Coding & Simulation', 'desc': 'Contains algorithmic questions plus an interactive workplace simulation testing Leadership Principles.'},
            {'round': 2, 'name': 'Technical Interview I', 'type': 'Live Coding', 'desc': 'Tree traversal, Linked List, Heap, or Graph questions paired with 15 mins of STAR LP questions.'},
            {'round': 3, 'name': 'Technical Interview II (LLD/OOP)', 'type': 'Design & Code', 'desc': 'Design Parking Lot, Locker System, or Elevator using SOLID principles.'},
            {'round': 4, 'name': 'Bar Raiser Round', 'type': 'Evaluative Loop', 'desc': 'An independent Amazon interviewer outside the hiring team tests long-term potential and cultural bar.'}
        ],
        'syllabus': {
            'DSA': ['Priority Queues / Heaps', 'Breadth First Search (BFS)', 'Sliding Window', 'Binary Trees & BST', 'Hash Maps'],
            'Low_Level_Design': ['SOLID Principles', 'Design Patterns (Factory, Strategy, Singleton)', 'Schema Design'],
            'Leadership_Principles': ['Customer Obsession', 'Ownership', 'Invent & Simplify', 'Are Right, A Lot', 'Deliver Results']
        },
        'past_questions': [
            'LRU Cache implementation with O(1) get and put.',
            'Rotting Oranges / Number of Islands.',
            'Trapping Rain Water.',
            'Design Amazon Locker Delivery System.',
            'Tell me about a time you made a difficult decision with incomplete data (Bias for Action).'
        ],
        'pro_tips': [
            'Prepare at least two distinct STAR stories for EACH of Amazon 16 Leadership Principles.',
            'In the Bar Raiser round, focus on the business impact and measurable metrics.',
            'Write clean, modular code with descriptive variable names and helper functions.'
        ]
    },
    {
        'name': 'TCS',
        'category': 'Service',
        'badge': 'Mass Recruiter / Top Indian IT',
        'logo_url': 'https://upload.wikimedia.org/wikipedia/commons/b/b1/Tata_Consultancy_Services_Logo.svg',
        'overview': 'TCS recruits for Ninja (3.5 LPA), Digital (7.0 LPA), and Prime (9.0+ LPA) through the National Qualifier Test (NQT).',
        'package_info': 'INR 3.5 - 9.2 LPA',
        'eligibility_criteria': {
            'min_cgpa': '60% or 6.0 CGPA throughout 10th, 12th, and B.Tech',
            'eligible_branches': ['All Engineering Disciplines', 'MCA', 'M.Sc CS/IT'],
            'backlog_policy': 'Maximum 1 active backlog permitted during exam; 0 at joining',
            'gap_year_allowed': 'Total academic gap cannot exceed 24 months'
        },
        'exam_pattern': [
            {'section': 'Numerical Ability', 'duration': '25 mins', 'questions': '20 questions (Arithmetic, Algebra, DI)', 'marking': 'Negative marking applies'},
            {'section': 'Reasoning Ability', 'duration': '25 mins', 'questions': '20 questions (Data sufficiency, Syllogisms, Patterns)', 'marking': 'Negative marking applies'},
            {'section': 'Verbal Ability', 'duration': '25 mins', 'questions': '25 questions (Grammar, Reading comprehension)', 'marking': 'Negative marking applies'},
            {'section': 'Advanced Coding (Digital/Prime)', 'duration': '90 mins', 'questions': '2 questions (1 Medium, 1 Hard DSA)', 'marking': 'Compiler test cases'}
        ],
        'rounds_breakdown': [
            {'round': 1, 'name': 'TCS NQT Cognitive + Coding', 'type': 'Online Test', 'desc': 'Combined aptitude test and coding round on TCS iON platform. High coding score unlocks Digital/Prime interview.'},
            {'round': 2, 'name': 'Technical Interview', 'type': 'F2F / Virtual', 'desc': 'Questions on C/C++/Java, DBMS queries, basic OOPs concepts, and college major project.'},
            {'round': 3, 'name': 'Managerial & HR Round', 'type': 'Behavioral', 'desc': 'Checks willingness to relocate, shift flexibility, career aspirations, and communication skills.'}
        ],
        'syllabus': {
            'Aptitude': ['Percentages & Ratio', 'Time and Work', 'Permutations & Probability', 'Seating Arrangement', 'Blood Relations'],
            'Technical': ['C/Java Basics', 'SQL Joins & Group By', 'Array manipulation', 'String algorithms', 'SDLC models'],
            'Coding': ['Matrix rotation', 'Prime number generation', 'Subarray with given sum', 'Parentheses matching']
        },
        'past_questions': [
            'Write a program to find the largest sum contiguous subarray (Kadane algorithm).',
            'Explain the difference between call by value and call by reference.',
            'Write an SQL query to find the 2nd highest salary from an Employee table.',
            'Explain Polymorphism and method overloading with a real-life example.'
        ],
        'pro_tips': [
            'No calculator is allowed; practice speed-math techniques and multiplication shortcuts.',
            'TCS iON editor does NOT provide autocomplete; ensure you memorize standard C/Java syntax.',
            'Scoring full marks in the 2 coding problems guarantees an upgrade to the Digital or Prime interview.'
        ]
    },
    {
        'name': 'Infosys',
        'category': 'Service',
        'badge': 'Global Consulting & IT',
        'logo_url': 'https://upload.wikimedia.org/wikipedia/commons/9/95/Infosys_logo.svg',
        'overview': 'Infosys recruits for Systems Engineer (3.6 LPA), Digital Specialist Engineer (6.5 LPA), and Specialist Programmer (9.5 LPA).',
        'package_info': 'INR 3.6 - 9.5 LPA',
        'eligibility_criteria': {
            'min_cgpa': '60% or 6.0 CGPA throughout 10th, 12th, and Graduation',
            'eligible_branches': ['B.E./B.Tech (All branches)', 'M.E./M.Tech', 'MCA'],
            'backlog_policy': 'Zero active backlogs allowed during selection',
            'gap_year_allowed': 'Maximum 1 year allowed'
        },
        'exam_pattern': [
            {'section': 'Reasoning Ability', 'duration': '25 mins', 'questions': '15 questions'},
            {'section': 'Technical Ability (Pseudocode)', 'duration': '10 mins', 'questions': '5 questions'},
            {'section': 'Verbal Ability', 'duration': '20 mins', 'questions': '20 questions'},
            {'section': 'Numerical Puzzle Solving', 'duration': '10 mins', 'questions': '4 questions'},
            {'section': 'Hands-on Coding', 'duration': '30 mins', 'questions': '1 coding problem'}
        ],
        'rounds_breakdown': [
            {'round': 1, 'name': 'Infosys Online Assessment', 'type': 'Aptitude + Pseudocode + Coding', 'desc': 'Sectional cutoffs exist for all sections. Pseudocode requires tracing nested loops and bitwise operators.'},
            {'round': 2, 'name': 'Technical + HR Interview', 'type': 'Virtual Interview', 'desc': 'Discussion of resume projects, DBMS normalization, basic data structures, and problem solving.'}
        ],
        'syllabus': {
            'Pseudocode': ['Bitwise shifts', 'Recursive call stacks', 'Array bounds & Pointer logic'],
            'Reasoning': ['Data Sufficiency', 'Cryptarithmetic puzzles', 'Direction sense'],
            'Technical': ['Java Collections', 'SQL queries', 'Inheritance & Interfaces', 'Web development basics']
        },
        'past_questions': [
            'Trace output of a recursive C function with static variables.',
            'Difference between Abstract class and Interface in Java.',
            'Reverse words in a given string without using split() function.',
            'Explain BCNF and how it differs from 3NF.'
        ],
        'pro_tips': [
            'Beware of sectional cutoffs: you must pass EVERY section, including Verbal and Pseudocode.',
            'Practice cryptarithmetic puzzles; they are unique to Infosys assessments.',
            'For Specialist Programmer (SP), practice LeetCode Hard Dynamic Programming and Graph problems.'
        ]
    },
    {
        'name': 'Cognizant',
        'category': 'Service',
        'badge': 'MNC Tech Services',
        'logo_url': 'https://upload.wikimedia.org/wikipedia/commons/4/43/Cognizant_logo_2022.svg',
        'overview': 'Cognizant offers GenC (4.0 LPA), GenC Elevate (4.25 LPA), and GenC Next (6.75 LPA) career tracks.',
        'package_info': 'INR 4.0 - 7.5 LPA',
        'eligibility_criteria': {
            'min_cgpa': '65% or 6.5 CGPA throughout education',
            'eligible_branches': ['Circuit branches preferred; all B.Tech eligible for GenC'],
            'backlog_policy': 'Maximum 1 active backlog permitted',
            'gap_year_allowed': 'Maximum 1 year gap allowed'
        },
        'exam_pattern': [
            {'section': 'Communication Assessment', 'duration': '45 mins', 'questions': 'Listening, Reading, Speaking (Versant style)'},
            {'section': 'Quantitative & Logical Ability', 'duration': '35 mins', 'questions': '25 questions'},
            {'section': 'Code Debugging (GenC Elevate)', 'duration': '20 mins', 'questions': '7 debugging snippets'},
            {'section': 'Advanced Coding (GenC Next)', 'duration': '60 mins', 'questions': '2 algorithm questions'}
        ],
        'rounds_breakdown': [
            {'round': 1, 'name': 'Aptitude & Communication Test', 'type': 'Automated Assessment', 'desc': 'Tests English pronunciation, listening comprehension, and logical reasoning.'},
            {'round': 2, 'name': 'Technical Assessment / Coding', 'type': 'Code & Debug', 'desc': 'Fix bugs in buggy code snippets and write full solutions for algorithmic questions.'},
            {'round': 3, 'name': 'Technical & HR Interview', 'type': 'Video Call', 'desc': 'Evaluates foundational coding, project architecture, and adaptability.'}
        ],
        'syllabus': {
            'Debugging': ['Off-by-one errors in loops', 'Null pointer checks', 'Data type overflow'],
            'Aptitude': ['Ratio and proportion', 'Time & Distance', 'Sentence completion'],
            'Technical': ['Data Structures', 'OOP Concepts', 'Relational Databases']
        },
        'past_questions': [
            'Write a program to find if two strings are anagrams.',
            'Explain ACID properties with a banking transfer example.',
            'Debug a binary search function containing a while loop bug.',
            'Difference between primary key and unique key.'
        ],
        'pro_tips': [
            'Use a good quality headset for the Versant communication round to ensure clear audio recording.',
            'In code debugging, 80% of errors are loop termination conditions or operator precedence.',
            'Highlight your final year project and your individual module contribution.'
        ]
    },
    {
        'name': 'Microsoft',
        'category': 'Product',
        'badge': 'Tier-1 Global Tech',
        'logo_url': 'https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg',
        'overview': 'Microsoft assesses deep algorithmic ability, low-level design, cloud fundamentals, and strong collaboration skills.',
        'package_info': 'INR 24 - 44 LPA (Base + Stock Grants + Bonus)',
        'eligibility_criteria': {
            'min_cgpa': '7.0 CGPA / 70%',
            'eligible_branches': ['CSE', 'IT', 'ECE', 'EEE', 'Math & Computing'],
            'backlog_policy': 'Zero active backlogs',
            'gap_year_allowed': 'Up to 1 year permitted'
        },
        'exam_pattern': [
            {'section': 'Online Assessment (Codility)', 'duration': '90 mins', 'questions': '3 algorithmic questions', 'platform': 'Codility'},
            {'section': 'Technical Interview 1', 'duration': '45 mins', 'questions': 'Data structures & problem solving'},
            {'section': 'Technical Interview 2', 'duration': '45 mins', 'questions': 'Trees, Graphs, and System/Low-level Design'},
            {'section': 'Technical Interview 3 (AA Round)', 'duration': '45 mins', 'questions': 'Director/Principal SDE architectural & behavioral probe'}
        ],
        'rounds_breakdown': [
            {'round': 1, 'name': 'Codility Online Test', 'type': 'Coding Assessment', 'desc': '3 problems with heavy emphasis on corner cases and test coverage.'},
            {'round': 2, 'name': 'Technical Interview I', 'type': 'Pair Programming', 'desc': 'Linked Lists, Binary Trees, recursion, and time complexity proof.'},
            {'round': 3, 'name': 'Technical Interview II', 'type': 'DSA & Design', 'desc': 'Graph traversal, caching algorithms, or basic Low Level Design (e.g., Tic-Tac-Toe, Snake & Ladder).'},
            {'round': 4, 'name': 'As-Appropriate (AA) Round', 'type': 'Partner / Director Interview', 'desc': 'Tests growth mindset, culture fit, architectural perspective, and handling failure.'}
        ],
        'syllabus': {
            'DSA': ['Linked Lists', 'Binary Trees & BST', 'Dynamic Programming', 'Bit Manipulation'],
            'Design': ['Object-Oriented Design Patterns', 'Multi-threading / Concurrency', 'API Design'],
            'Culture': ['Growth Mindset', 'Customer Obsession', 'Diversity and Inclusion']
        },
        'past_questions': [
            'Reverse Nodes in k-Group.',
            'Serialize and Deserialize a Binary Tree.',
            'Implement LRU Cache using Doubly Linked List and Hash Map.',
            'Find median in a running data stream.'
        ],
        'pro_tips': [
            'Codility penalizes for edge-case failures heavily; write your own custom test cases before submitting.',
            'Microsoft loves candidates who demonstrate a Growth Mindset—never be defensive when an interviewer points out a bug.',
            'Be ready to discuss time vs memory tradeoffs in detail.'
        ]
    }
]
