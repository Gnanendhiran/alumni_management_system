"""
Populate Comprehensive Sample Data for Alumni Management System
Creates 25+ Alumni, 20+ Students, 10+ Jobs, 6+ Events, Announcements & Feed Posts
"""

from db_connect import execute_query
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

def populate_data():
    print("Populating Campuses...")
    campuses_list = [
        ("Main Campus", "MAIN", "Central City Campus"),
        ("Tech Park Campus", "TPC", "Innovation & Science Park"),
        ("South City Campus", "SCC", "Knowledge Quarter")
    ]
    for name, code, addr in campuses_list:
        execute_query("""
            INSERT INTO campuses (name, code, address, is_active) 
            VALUES (%s, %s, %s, 1)
            ON DUPLICATE KEY UPDATE name=VALUES(name)
        """, (name, code, addr), fetch=False)
    
    campus_ids = [c['id'] for c in execute_query("SELECT id FROM campuses")]
    campus_id = campus_ids[0] if campus_ids else 1

    print("Populating Degrees...")
    degrees_list = [
        ("Bachelor of Science in Computer Science and Engineering", "CSE", "bachelor"),
        ("Bachelor of Science in Electrical and Electronic Engineering", "EEE", "bachelor"),
        ("Bachelor of Science in Data Science & AI", "BSDS", "bachelor"),
        ("Bachelor of Business Administration", "BBA", "bachelor"),
        ("Master of Science in Software Engineering", "MSSE", "master")
    ]
    for name, abbr, level in degrees_list:
        execute_query("""
            INSERT INTO degrees (name, abbreviation, level, is_active) 
            VALUES (%s, %s, %s, 1)
            ON DUPLICATE KEY UPDATE name=VALUES(name)
        """, (name, abbr, level), fetch=False)
        
    degree_ids = [d['id'] for d in execute_query("SELECT id FROM degrees")]
    degree_id = degree_ids[0] if degree_ids else 1

    password_hash = generate_password_hash("user123")

    # List of 25 Alumni (Seniors)
    alumni_data = [
        ("Arun", "Kumar", "arun@example.com", "Google", "Senior Software Engineer", 2020),
        ("Arjun", "Ram", "arjun@example.com", "Microsoft", "Cloud Solutions Architect", 2019),
        ("Gokul", "Nath", "gokul@example.com", "Amazon", "SDE II", 2021),
        ("Jana", "Raman", "jana@example.com", "Zoho", "Product Manager", 2018),
        ("Guru", "Prasad", "guru@example.com", "TCS", "Tech Lead", 2017),
        ("Priya", "Dharshini", "priya@example.com", "Infosys", "Lead Data Analyst", 2020),
        ("Kavitha", "Srinivasan", "kavitha@example.com", "Accenture", "Consultant", 2019),
        ("Vikas", "Sharma", "vikas@example.com", "Freshworks", "Engineering Manager", 2016),
        ("Siddharth", "V", "siddharth@example.com", "Cognizant", "Full Stack Developer", 2021),
        ("Deepak", "Raj", "deepak@example.com", "Wipro", "Security Engineer", 2020),
        ("Surya", "Prakash", "surya@example.com", "Paytm", "Backend Developer", 2022),
        ("Karthik", "Subramanian", "karthik@example.com", "PayPal", "DevOps Engineer", 2019),
        ("Divya", "Bharathi", "divya@example.com", "IBM", "AI Research Scientist", 2018),
        ("Manish", "Verma", "manish@example.com", "Oracle", "Database Administrator", 2017),
        ("Rahul", "Dravid", "rahul@example.com", "Cisco", "Network Architect", 2015),
        ("Aravind", "Swamy", "aravind@example.com", "Zoho", "UI/UX Designer", 2021),
        ("Harish", "Kannan", "harish@example.com", "HCL", "Systems Engineer", 2020),
        ("Naveen", "Kumar", "naveen@example.com", "JPMorgan", "Quantitative Analyst", 2019),
        ("Swetha", "Rajan", "swetha@example.com", "Capgemini", "Scrum Master", 2018),
        ("Dinesh", "Karthik", "dinesh@example.com", "Salesforce", "Technical Specialist", 2021),
        ("Logesh", "Waran", "logesh@example.com", "Swiggy", "Mobile Developer (Flutter)", 2022),
        ("Nitin", "Gadkari", "nitin@example.com", "Flipkart", "Supply Chain Analyst", 2020),
        ("Aakash", "Deep", "aakash@example.com", "Intel", "Hardware Engineer", 2019),
        ("Suresh", "Raina", "suresh@example.com", "Uber", "Site Reliability Engineer", 2018),
        ("Vikram", "Prabhu", "vikram@example.com", "Nvidia", "Deep Learning Engineer", 2017)
    ]

    print("Populating Alumni Profiles...")
    alumni_user_ids = []
    for idx, (fname, lname, email, comp, title, grad_yr) in enumerate(alumni_data, start=101):
        user_res = execute_query("SELECT id FROM users WHERE email = %s", (email,))
        if user_res:
            uid = user_res[0]['id']
        else:
            uid = execute_query("""
                INSERT INTO users (email, password_hash, role_id, status) VALUES (%s, %s, 2, 'active')
            """, (email, password_hash), fetch=False)
        
        if uid:
            alumni_user_ids.append(uid)
            stu_num = f"0111{idx}"
            phone_num = f"9876543{idx:03d}"
            deg = random.choice(degree_ids)
            cam = random.choice(campus_ids)
            execute_query("""
                INSERT INTO alumni_profiles 
                (user_id, first_name, last_name, student_id, phone, degree_id, campus_id, graduation_year, current_company, current_job_title)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE current_company=VALUES(current_company), current_job_title=VALUES(current_job_title)
            """, (uid, fname, lname, stu_num, phone_num, deg, cam, grad_yr, comp, title), fetch=False)

    # List of 20 Students (Juniors)
    student_data = [
        ("Ananya", "Rao", "ananya@example.com", 2025, "Spring 2024"),
        ("Preeti", "Singh", "preeti@example.com", 2026, "Fall 2024"),
        ("Rohan", "Mehta", "rohan@example.com", 2025, "Spring 2024"),
        ("Suresh", "Chandran", "suresh.student@example.com", 2026, "Fall 2024"),
        ("Kavya", "Madhavan", "kavya@example.com", 2027, "Spring 2025"),
        ("Vijay", "Sethupathi", "vijay@example.com", 2025, "Spring 2024"),
        ("Ramesh", "Babu", "ramesh@example.com", 2026, "Fall 2024"),
        ("Srinivasan", "M", "srini@example.com", 2025, "Spring 2024"),
        ("Varun", "Tej", "varun@example.com", 2027, "Spring 2025"),
        ("Meena", "Kumari", "meena@example.com", 2026, "Fall 2024"),
        ("Pooja", "Hegde", "pooja@example.com", 2025, "Spring 2024"),
        ("Ashwin", "Kumar", "ashwin@example.com", 2026, "Fall 2024"),
        ("Ganesh", "Venkat", "ganesh@example.com", 2025, "Spring 2024"),
        ("Bhavana", "Reddy", "bhavana@example.com", 2027, "Spring 2025"),
        ("Chetan", "Bhagat", "chetan@example.com", 2026, "Fall 2024"),
        ("Dhanush", "K", "dhanush@example.com", 2025, "Spring 2024"),
        ("Elango", "V", "elango@example.com", 2026, "Fall 2024"),
        ("Farhan", "Akhtar", "farhan@example.com", 2027, "Spring 2025"),
        ("Gautam", "Gambhir", "gautam@example.com", 2025, "Spring 2024"),
        ("Hemant", "Soren", "hemant@example.com", 2026, "Fall 2024")
    ]

    print("Populating Student Profiles...")
    student_user_ids = []
    for idx, (fname, lname, email, exp_grad, sem) in enumerate(student_data, start=201):
        user_res = execute_query("SELECT id FROM users WHERE email = %s", (email,))
        if user_res:
            uid = user_res[0]['id']
        else:
            uid = execute_query("""
                INSERT INTO users (email, password_hash, role_id, status) VALUES (%s, %s, 3, 'active')
            """, (email, password_hash), fetch=False)
        
        if uid:
            student_user_ids.append(uid)
            stu_num = f"0112{idx}"
            phone_num = f"9123456{idx:03d}"
            deg = random.choice(degree_ids)
            cam = random.choice(campus_ids)
            execute_query("""
                INSERT INTO student_profiles 
                (user_id, first_name, last_name, student_id, phone, degree_id, campus_id, expected_graduation_year, current_semester)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE current_semester=VALUES(current_semester)
            """, (uid, fname, lname, stu_num, phone_num, deg, cam, exp_grad, sem), fetch=False)

    print("Populating Job Postings...")
    jobs = [
        ("Junior Software Engineer", "Google", "full_time", "Bangalore / Remote", "Looking for enthusiastic junior developer with strong DSA skills.", "Python, SQL, Data Structures", 600000, 1000000),
        ("Frontend Developer (React/Vue)", "Zoho", "full_time", "Chennai", "Build scalable web components for enterprise cloud SaaS applications.", "HTML, CSS, JavaScript, React", 450000, 800000),
        ("Data Analyst Intern", "Amazon", "internship", "Hyderabad", "Analyze customer behavior and optimize logistics telemetry data.", "SQL, Python, Excel, PowerBI", 25000, 40000),
        ("Cloud & DevOps Engineer", "Microsoft", "full_time", "Bangalore", "Manage CI/CD pipelines, Docker, Kubernetes, and Azure cloud infrastructure.", "Docker, Kubernetes, CI/CD, Python", 800000, 1400000),
        ("Graduate Engineer Trainee", "TCS", "full_time", "Chennai / Hybrid", "Core software development, client project implementation, and database design.", "C++, Java, SQL, Problem Solving", 360000, 500000),
        ("Associate Product Manager", "Freshworks", "full_time", "Chennai", "Drive product roadmap, collaborate with UX designers and software engineering teams.", "Product Management, Wireframing, Agile", 700000, 1100000),
        ("Cyber Security Analyst", "Cisco", "full_time", "Bangalore", "Monitor vulnerability reports, penetration testing, and network security audit.", "Networking, Wireshark, Python, Security", 650000, 950000),
        ("AI / Machine Learning Engineer", "Nvidia", "full_time", "Bangalore", "Optimize deep learning models for GPU inference and computer vision.", "PyTorch, CUDA, Python, Computer Vision", 900000, 1600000),
        ("Mobile App Developer", "Swiggy", "full_time", "Bangalore", "Build high performance Android and iOS mobile app features using Flutter.", "Flutter, Dart, REST APIs", 550000, 900000),
        ("QA & Automation Specialist", "Cognizant", "full_time", "Coimbatore", "Write automated test scripts using Selenium and PyTest for web applications.", "Python, Selenium, PyTest, Git", 400000, 650000)
    ]
    for idx, (title, comp, jtype, loc, desc, reqs, smin, smax) in enumerate(jobs):
        poster_id = alumni_user_ids[idx % len(alumni_user_ids)] if alumni_user_ids else 1
        execute_query("""
            INSERT INTO job_postings (posted_by, title, company_name, job_type, location, description, requirements, salary_min, salary_max, target_audience, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'all', 'open')
            ON DUPLICATE KEY UPDATE title=VALUES(title)
        """, (poster_id, title, comp, jtype, loc, desc, reqs, smin, smax), fetch=False)

    print("Populating Events & Reunions...")
    events = [
        ("Grand Alumni Reunion 2026", "grand-alumni-reunion-2026", "Join us for our annual grand campus reunion! Reconnect with classmates, faculty, and network with fellow leaders.", 30, "10:00:00", "Main Campus Auditorium"),
        ("Tech Talk: Career Growth in AI & Cloud", "tech-talk-ai-cloud-2026", "Arun Kumar (Senior SDE at Google) and Arjun Ram (Architect at Microsoft) share actionable advice for juniors.", 15, "18:30:00", "Virtual Zoom Event"),
        ("Annual Campus Career Fair & Job Expo", "annual-career-fair-2026", "Over 25 top tech companies visiting campus for walk-in interviews and internship opportunities.", 45, "09:00:00", "Student Convention Center"),
        ("Hackathon: Build for Social Good", "hackathon-social-good-2026", "24-Hour hackathon open to alumni and students. Cash prizes up to $5000 sponsored by alumni startups.", 20, "10:00:00", "Innovation Hub Lab 3"),
        ("Mentorship Dinner & Networking Night", "mentorship-dinner-networking", "An exclusive interactive dinner pairing senior alumni mentors with final year student mentees.", 60, "19:00:00", "Grand Palace Hotel Ballroom"),
        ("Alumni Sports League Tournament", "alumni-sports-league-2026", "Cricket, Football, and Badminton tournament bringing together alumni and current student teams.", 75, "08:00:00", "University Sports Complex")
    ]
    for title, slug, desc, days_offset, time_str, venue in events:
        creator = alumni_user_ids[0] if alumni_user_ids else 1
        execute_query("""
            INSERT INTO events (title, slug, description, start_date, start_time, venue, visibility, status, created_by)
            VALUES (%s, %s, %s, CURDATE() + INTERVAL %s DAY, %s, %s, 'all', 'published', %s)
            ON DUPLICATE KEY UPDATE title=VALUES(title)
        """, (title, slug, desc, days_offset, time_str, venue, creator), fetch=False)

    print("Populating Announcements...")
    announcements = [
        ("🚀 Welcome to the New Alumni Sync Portal!", "We are thrilled to unveil our revamped Alumni Sync Portal! Connect with mentors, explore job opportunities, and RSVP for upcoming reunions."),
        ("📢 Internship Drive 2026 Registration Open", "Final year and pre-final year students can now apply for exclusive alumni-referred internships via the Jobs tab."),
        ("🏆 Outstanding Alumni Achievement Award 2026", "Nominations are now open for the Annual Alumni Excellence Awards in Technology, Entrepreneurship, and Research.")
    ]
    for title, content in announcements:
        creator = alumni_user_ids[0] if alumni_user_ids else 1
        execute_query("""
            INSERT INTO announcements (title, content, target_audience, status, created_by)
            VALUES (%s, %s, 'all', 'published', %s)
            ON DUPLICATE KEY UPDATE title=VALUES(title)
        """, (title, content, creator), fetch=False)

    print("Data population complete! 25+ Alumni, 20+ Students, 10 Jobs, 6 Events successfully created.")

if __name__ == "__main__":
    populate_data()
