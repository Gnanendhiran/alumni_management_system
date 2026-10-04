"""
Populate Real-World Sample Data for Alumni Management System
Colleges: CEG (College of Engineering Guindy), MIT (Madras Institute of Technology), ACTech, SAP
Companies: Wells Fargo, Amazon, Google, Microsoft, Goldman Sachs, Zoho, PayPal, JPMorgan Chase, etc.
No fake filler names — Authentic Alumni Seniors and Student Juniors.
"""

from db_connect import execute_query
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

def populate_data():
    print("Populating Reputed Campuses (CEG, MIT, ACTech, SAP)...")
    campuses_list = [
        ("College of Engineering, Guindy (CEG)", "CEG", "Sardar Patel Road, Guindy, Chennai, Tamil Nadu"),
        ("Madras Institute of Technology (MIT)", "MIT", "MIT Road, Chromepet, Chennai, Tamil Nadu"),
        ("Alagappa Chettiar College of Technology (ACTech)", "ACTECH", "Guindy Campus, Anna University, Chennai"),
        ("School of Architecture and Planning (SAP)", "SAP", "Anna University Campus, Guindy, Chennai")
    ]
    for name, code, addr in campuses_list:
        execute_query("""
            INSERT INTO campuses (name, code, address, is_active) 
            VALUES (%s, %s, %s, 1)
            ON DUPLICATE KEY UPDATE name=VALUES(name), address=VALUES(address)
        """, (name, code, addr), fetch=False)
    
    campus_rows = execute_query("SELECT id, code FROM campuses")
    campus_dict = {c['code']: c['id'] for c in campus_rows}
    ceg_id = campus_dict.get('CEG', 1)
    mit_id = campus_dict.get('MIT', 2)
    actech_id = campus_dict.get('ACTECH', 3)
    sap_id = campus_dict.get('SAP', 4)

    print("Populating Engineering & Tech Degrees...")
    degrees_list = [
        ("B.E. Computer Science and Engineering", "CSE", "bachelor"),
        ("B.Tech Information Technology", "IT", "bachelor"),
        ("B.E. Electronics and Communication Engineering", "ECE", "bachelor"),
        ("B.Tech Artificial Intelligence and Data Science", "AI & DS", "bachelor"),
        ("B.E. Electrical and Electronics Engineering", "EEE", "bachelor"),
        ("M.E. Software Engineering", "SE", "master")
    ]
    for name, abbr, level in degrees_list:
        execute_query("""
            INSERT INTO degrees (name, abbreviation, level, is_active) 
            VALUES (%s, %s, %s, 1)
            ON DUPLICATE KEY UPDATE name=VALUES(name)
        """, (name, abbr, level), fetch=False)
        
    degree_rows = execute_query("SELECT id, abbreviation FROM degrees")
    degree_dict = {d['abbreviation']: d['id'] for d in degree_rows}
    cse_id = degree_dict.get('CSE', 1)

    password_hash = generate_password_hash("user123")

    # 28 Reputed Alumni Seniors with Top MNCs (Wells Fargo, Amazon, Google, Microsoft, Goldman Sachs, Zoho, etc.)
    alumni_data = [
        ("Arun", "Kumar", "arun@example.com", "Wells Fargo", "Senior Software Engineer", 2020, ceg_id),
        ("Arjun", "Ram", "arjun@example.com", "Amazon", "Cloud Solutions Architect", 2019, mit_id),
        ("Gokul", "Nath", "gokul@example.com", "Google", "SDE II", 2021, ceg_id),
        ("Janardhanan", "R", "janardhanan@example.com", "Wells Fargo", "Lead Financial Systems Developer", 2018, mit_id),
        ("Guruprasad", "S", "guruprasad@example.com", "Microsoft", "Principal Software Engineer", 2017, ceg_id),
        ("Priyadharshini", "K", "priya@example.com", "Goldman Sachs", "VP of Technology & Engineering", 2018, mit_id),
        ("Kavitha", "Srinivasan", "kavitha@example.com", "Zoho Corporation", "Senior Product Manager", 2019, ceg_id),
        ("Vikas", "Sharma", "vikas@example.com", "PayPal", "Engineering Manager", 2016, mit_id),
        ("Siddharth", "V", "siddharth@example.com", "JPMorgan Chase", "Quantitative Software Analyst", 2021, ceg_id),
        ("Deepak", "Raj", "deepak@example.com", "Morgan Stanley", "DevOps & Cloud Lead", 2020, mit_id),
        ("Surya", "Prakash", "surya@example.com", "Qualcomm", "Systems Architecture Lead", 2019, ceg_id),
        ("Karthik", "Subramanian", "karthik@example.com", "Nvidia", "AI Research Scientist", 2018, mit_id),
        ("Divya", "Bharathi", "divya@example.com", "Salesforce", "Staff Software Engineer", 2020, ceg_id),
        ("Manish", "Verma", "manish@example.com", "Adobe", "Lead UI/UX Architect", 2017, ceg_id),
        ("Rahul", "Dravid", "rahul@example.com", "Cisco Systems", "Principal Network Engineer", 2015, mit_id),
        ("Aravind", "Swamy", "aravind@example.com", "Freshworks", "Frontend Lead Developer", 2021, ceg_id),
        ("Harish", "Kannan", "harish@example.com", "Tata Consultancy Services (TCS)", "Technical Lead", 2019, mit_id),
        ("Naveen", "Kumar", "naveen@example.com", "Infosys", "Enterprise Solutions Architect", 2018, ceg_id),
        ("Swetha", "Rajan", "swetha@example.com", "Accenture", "Senior Management Consultant", 2020, mit_id),
        ("Dinesh", "Karthik", "dinesh@example.com", "Cognizant", "Full Stack Architect", 2021, ceg_id),
        ("Logeshwaran", "M", "logesh@example.com", "Wells Fargo", "Backend Engineer - Payments", 2022, ceg_id),
        ("Nitin", "Sundar", "nitin@example.com", "Amazon", "SDE - Logistics Telemetry", 2020, mit_id),
        ("Aakash", "Deep", "aakash@example.com", "Goldman Sachs", "Risk Technology Analyst", 2019, ceg_id),
        ("Suresh", "Raina", "suresh@example.com", "Microsoft", "Site Reliability Engineer", 2018, mit_id),
        ("Vikram", "Prabhu", "vikram@example.com", "Nvidia", "Deep Learning Acceleration Engineer", 2017, ceg_id),
        ("Rajesh", "Kannan", "rajesh@example.com", "Google", "Software Engineering Director", 2014, ceg_id),
        ("Anitha", "Ramesh", "anitha@example.com", "PayPal", "Lead Product Manager", 2019, mit_id),
        ("Madhan", "Mohan", "madhan@example.com", "Wells Fargo", "Cybersecurity Threat Lead", 2018, ceg_id)
    ]

    print("Populating Alumni Profiles...")
    alumni_user_ids = []
    for idx, (fname, lname, email, comp, title, grad_yr, c_id) in enumerate(alumni_data, start=101):
        user_res = execute_query("SELECT id FROM users WHERE email = %s", (email,))
        if user_res:
            uid = user_res[0]['id']
        else:
            uid = execute_query("""
                INSERT INTO users (email, password_hash, role_id, status) VALUES (%s, %s, 2, 'active')
            """, (email, password_hash), fetch=False)
        
        if uid:
            alumni_user_ids.append(uid)
            stu_num = f"20{grad_yr - 4:02d}115{idx:03d}"
            phone_num = f"98401{idx:05d}"
            deg = random.choice(list(degree_dict.values()))
            execute_query("""
                INSERT INTO alumni_profiles 
                (user_id, first_name, last_name, student_id, phone, degree_id, campus_id, graduation_year, current_company, current_job_title)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE first_name=VALUES(first_name), last_name=VALUES(last_name), current_company=VALUES(current_company), current_job_title=VALUES(current_job_title)
            """, (uid, fname, lname, stu_num, phone_num, deg, c_id, grad_yr, comp, title), fetch=False)

    # 20 Authentic Student Juniors (CEG & MIT)
    student_data = [
        ("Ananya", "Rao", "ananya@example.com", 2025, "7th Semester", ceg_id),
        ("Preeti", "Singh", "preeti@example.com", 2026, "5th Semester", mit_id),
        ("Rohan", "Mehta", "rohan@example.com", 2025, "7th Semester", ceg_id),
        ("Suresh", "Chandran", "suresh.student@example.com", 2026, "5th Semester", mit_id),
        ("Kavya", "Madhavan", "kavya@example.com", 2027, "3rd Semester", ceg_id),
        ("Vijay", "Sethupathi", "vijay@example.com", 2025, "7th Semester", mit_id),
        ("Ramesh", "Babu", "ramesh@example.com", 2026, "5th Semester", ceg_id),
        ("Srinivasan", "M", "srini@example.com", 2025, "7th Semester", mit_id),
        ("Varun", "Tej", "varun@example.com", 2027, "3rd Semester", ceg_id),
        ("Meena", "Kumari", "meena@example.com", 2026, "5th Semester", mit_id),
        ("Pooja", "Hegde", "pooja@example.com", 2025, "7th Semester", ceg_id),
        ("Ashwin", "Kumar", "ashwin@example.com", 2026, "5th Semester", mit_id),
        ("Ganesh", "Venkat", "ganesh@example.com", 2025, "7th Semester", ceg_id),
        ("Bhavana", "Reddy", "bhavana@example.com", 2027, "3rd Semester", actech_id),
        ("Chetan", "Bhagat", "chetan@example.com", 2026, "5th Semester", ceg_id),
        ("Dhanush", "K", "dhanush@example.com", 2025, "7th Semester", mit_id),
        ("Elango", "V", "elango@example.com", 2026, "5th Semester", ceg_id),
        ("Farhan", "Akhtar", "farhan@example.com", 2027, "3rd Semester", sap_id),
        ("Gautam", "Gambhir", "gautam@example.com", 2025, "7th Semester", mit_id),
        ("Hemant", "Soren", "hemant@example.com", 2026, "5th Semester", ceg_id)
    ]

    print("Populating Student Profiles...")
    student_user_ids = []
    for idx, (fname, lname, email, exp_grad, sem, c_id) in enumerate(student_data, start=201):
        user_res = execute_query("SELECT id FROM users WHERE email = %s", (email,))
        if user_res:
            uid = user_res[0]['id']
        else:
            uid = execute_query("""
                INSERT INTO users (email, password_hash, role_id, status) VALUES (%s, %s, 3, 'active')
            """, (email, password_hash), fetch=False)
        
        if uid:
            student_user_ids.append(uid)
            stu_num = f"2022115{idx:03d}"
            phone_num = f"98402{idx:05d}"
            deg = random.choice(list(degree_dict.values()))
            execute_query("""
                INSERT INTO student_profiles 
                (user_id, first_name, last_name, student_id, phone, degree_id, campus_id, expected_graduation_year, current_semester)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE first_name=VALUES(first_name), last_name=VALUES(last_name), current_semester=VALUES(current_semester)
            """, (uid, fname, lname, stu_num, phone_num, deg, c_id, exp_grad, sem), fetch=False)

    print("Populating Top MNC Job Openings (Wells Fargo, Amazon, Google, Microsoft, Goldman Sachs, Zoho)...")
    jobs = [
        ("Software Development Engineer (SDE I)", "Wells Fargo", "full_time", "Chennai (Ramanujan IT City) / Hyderabad", "Wells Fargo Technology is hiring SDE I for Core Banking & Financial Services platform development.", "Java, Spring Boot, Microservices, SQL, Problem Solving", 1200000, 1800000),
        ("Software Development Engineer I (SDE-1)", "Amazon", "full_time", "Chennai / Bangalore", "Join Amazon Consumer Technology team. Build high-scale distributed backend microservices.", "C++, Java, Python, Data Structures & Algorithms", 1400000, 2200000),
        ("Software Engineer (Cloud & Infrastructure)", "Google", "full_time", "Bangalore / Remote", "Develop next-gen Google Cloud infrastructure, distributed storage systems, and networking solutions.", "Python, Go, C++, Distributed Systems, OS", 1800000, 2800000),
        ("Member of Technical Staff (MTS)", "Zoho Corporation", "full_time", "Chennai / Tenkasi", "Build scalable cloud SaaS solutions, database query engines, and web applications.", "Java, C++, JavaScript, SQL, Linux", 700000, 1200000),
        ("Summer Technology Analyst Intern 2026", "Goldman Sachs", "internship", "Bangalore / Hyderabad", "Exclusive 2-month summer internship for pre-final year students in quantitative engineering & software architecture.", "Python, C++, Financial Algorithms, Data Structures", 75000, 100000),
        ("Cloud & DevOps Engineer", "Microsoft", "full_time", "Hyderabad / Bangalore", "Manage Azure Cloud deployment automation, Kubernetes clusters, and enterprise CI/CD security pipelines.", "Docker, Kubernetes, Azure, PowerShell, Python", 1500000, 2400000),
        ("Graduate Software Engineer Trainee", "Wells Fargo", "full_time", "Chennai Campus Drive", "Entry-level engineering role for fresh graduates. Structured 6-month training program in enterprise software design.", "Java, Python, SQL, Computer Science Fundamentals", 850000, 1200000),
        ("Associate Financial Software Engineer", "JPMorgan Chase & Co.", "full_time", "Bengaluru", "Develop high-frequency trading platform tools and risk assessment microservices.", "Java, Python, SQL, React, Cloud", 1300000, 2000000),
        ("Frontend Developer (React / TypeScript)", "Freshworks", "full_time", "Chennai (Perungudi)", "Create slick, responsive customer support UI components using React, Redux, and TypeScript.", "React, JavaScript, HTML5/CSS3, REST APIs", 800000, 1400000),
        ("AI & Machine Learning Acceleration Intern", "Nvidia", "internship", "Bangalore", "Research GPU kernel optimization for PyTorch models and computer vision pipelines.", "Python, PyTorch, C++, CUDA", 50000, 80000)
    ]
    for idx, (title, comp, jtype, loc, desc, reqs, smin, smax) in enumerate(jobs):
        poster_id = alumni_user_ids[idx % len(alumni_user_ids)] if alumni_user_ids else 1
        execute_query("""
            INSERT INTO job_postings (posted_by, title, company_name, job_type, location, description, requirements, salary_min, salary_max, target_audience, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'all', 'open')
            ON DUPLICATE KEY UPDATE title=VALUES(title), company_name=VALUES(company_name), description=VALUES(description)
        """, (poster_id, title, comp, jtype, loc, desc, reqs, smin, smax), fetch=False)

    print("Populating CEG & MIT Reunions & Tech Summits...")
    events = [
        ("CEG & MIT Grand Alumni Reunion 2026", "ceg-mit-grand-alumni-reunion-2026", "Annual grand reunion bringing together CEG, MIT, ACTech & SAP alumni from across the globe. Networking, keynotes, and gala dinner.", 30, "10:00:00", "Vivekananda Auditorium, CEG Campus"),
        ("Tech Summit: Cracking Product & MNC Interviews", "tech-summit-mnc-interviews", "Arun Kumar (Wells Fargo) and Arjun Ram (Amazon) conduct interactive session on cracking top SDE & Financial Tech interviews.", 15, "18:00:00", "Tag Auditorium, CEG Guindy"),
        ("Annual Campus Recruitment & Placement Expo 2026", "annual-placement-expo-2026", "Over 40 top MNCs including Wells Fargo, Amazon, Google, Microsoft, and Zoho conducting on-campus placements.", 45, "09:00:00", "Rajam Hall, MIT Chromepet"),
        ("24-Hour Hackathon: Smart India & AI Solutions", "hackathon-ai-solutions-2026", "Inter-college hackathon sponsored by Wells Fargo & Zoho. Cash prizes worth ₹2,00,000 for winning student teams.", 20, "10:00:00", "CUIC Building, Anna University"),
        ("Alumni Mentorship & Career Guidance Dinner", "alumni-mentorship-dinner", "One-on-one mentorship networking dinner matching senior MNC engineers with final year students.", 60, "19:00:00", "The Park Hotel, Nungambakkam, Chennai"),
        ("Anna University Alumni Trophy Cricket Tournament", "alumni-trophy-cricket-2026", "Annual T20 cricket tournament featuring CEG Alumni XI vs MIT Alumni XI.", 75, "08:30:00", "Anna University Sports Grounds")
    ]
    for title, slug, desc, days_offset, time_str, venue in events:
        creator = alumni_user_ids[0] if alumni_user_ids else 1
        execute_query("""
            INSERT INTO events (title, slug, description, start_date, start_time, venue, visibility, status, created_by)
            VALUES (%s, %s, %s, CURDATE() + INTERVAL %s DAY, %s, %s, 'all', 'published', %s)
            ON DUPLICATE KEY UPDATE title=VALUES(title), description=VALUES(description)
        """, (title, slug, desc, days_offset, time_str, venue, creator), fetch=False)

    print("Populating Official Announcements...")
    announcements = [
        ("🚀 Welcome to CEG & MIT Alumni Sync Portal!", "We are proud to launch the official Alumni Sync Portal connecting CEG, MIT, ACTech and SAP graduates with current students worldwide."),
        ("💼 Wells Fargo & Amazon Campus Placement Drive", "Eligible 7th & 8th semester students can now apply for exclusive referral positions posted by alumni under the Jobs tab."),
        ("🏆 Outstanding Alumni Excellence Award 2026 Nominations", "Submit nominations for alumni achievements in Technology, Finance, Entrepreneurship, and Research.")
    ]
    for title, content in announcements:
        creator = alumni_user_ids[0] if alumni_user_ids else 1
        execute_query("""
            INSERT INTO announcements (title, content, target_audience, status, created_by)
            VALUES (%s, %s, 'all', 'published', %s)
            ON DUPLICATE KEY UPDATE title=VALUES(title), content=VALUES(content)
        """, (title, content, creator), fetch=False)

    print("Data population complete! CEG & MIT Alumni (Wells Fargo, Amazon, Google, Microsoft, Goldman Sachs) successfully created.")

if __name__ == "__main__":
    populate_data()
