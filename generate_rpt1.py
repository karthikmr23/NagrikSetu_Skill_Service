# -*- coding: utf-8 -*-
"""Generate Simplified Report 1: 01_About_the_Service.docx (5-8 pages) using simple, natural student words."""
import os, sys
sys.path.append(r"C:\Users\karth\OneDrive\Documents\NagrikSetu_Skill_Development_FINAL")
from generate_docs_base import (
    docx, OUT_DIR, setup_page, create_title_page,
    add_h1, add_h2, add_p, add_bullet, build_table
)

def generate_report_1_simplified():
    doc = docx.Document()
    setup_page(doc, "About the Service")
    create_title_page(
        doc,
        doc_title="About the Service",
        subtitle="A Simple and Complete Guide to the NagrikSetu Skill Development Service, Its Features, Training Centres, and How Students Learn Practical Job Skills",
        doc_ref="SDS-RPT-01-ABOUT"
    )

    # Document Overview & TOC
    add_h1(doc, "Document Overview & Quick Table of Contents")
    add_p(doc, "This project report gives a simple, complete explanation of the NagrikSetu Skill Development Service (SDS). Built for the Directorate of Skill Development, Entrepreneurship and Livelihood in Karnataka, this website helps young citizens find practical job-oriented courses, apply online, join batches at approved training centres, and track their attendance and certificates.")
    add_p(doc, "The report is written in clear, natural English suitable for a second-year college student. All complicated corporate jargon and heavy words have been replaced with easy words so that any reader or examiner can understand the project easily without asking difficult questions.")
    
    toc_data = [
        ["Chapter / Topic", "What is Explained in this Section", "Section"],
        ["1. Introduction to the Service", "What the website is, why it was created, and who it helps", "Section 1"],
        ["2. Problems the Service Solves", "Old problems like lack of course details, paper forms, travel costs, and middlemen", "Section 2"],
        ["3. Main Project Objectives", "Simple goals: open courses, fair seat limits, daily attendance, verified certificates", "Section 3"],
        ["4. Who Uses the System", "Citizens, students, teachers, training centre managers, and government admins", "Section 4"],
        ["5. Main Features of the Website", "7 skill categories, 208 active courses, search tools, and student dashboard", "Section 5"],
        ["6. Approved Training Centres", "Real centres in Karnataka like Bengaluru, Mysuru, Hubballi, and Shivamogga", "Section 6"],
        ["7. Step-by-Step How It Works", "The 4 simple steps from creating an account to downloading your certificate", "Section 7"],
        ["8. Good Things for Students & Society", "No fees, practical computer skills, jobs for rural youth, and equal chances", "Section 8"],
        ["9. Technology Stack Used", "Python with FastAPI, React for frontend, MySQL database, and Docker containers", "Section 9"],
        ["10. Simple Project Conclusion", "Final summary of how the service helps build youth careers", "Section 10"]
    ]
    build_table(doc, toc_data[0], toc_data[1:], [2.2, 3.3, 1.0])

    # 1. Introduction
    add_h1(doc, "1. Introduction to the Skill Development Service")
    add_p(doc, "The NagrikSetu Skill Development Service (SDS) is an official government website designed to help students and job seekers across Karnataka learn practical, job-ready skills. It is part of the larger NagrikSetu digital governance system created for the Directorate of Skill Development, Entrepreneurship and Livelihood, Government of Karnataka.")
    add_p(doc, "Every year, thousands of young boys and girls complete school, college, ITI, or diploma courses. However, many find it hard to get a good job because companies look for practical skills that are not taught in textbooks—such as writing computer programs, fixing electrical equipment, managing hospital patient records, operating modern farming machinery, or handling hotel guests.")
    add_p(doc, "Private training institutes often charge high fees of 20,000 to 50,000 rupees for these courses, which many poor and middle-class families cannot afford. The Karnataka government already runs many free or low-cost practical training courses, but in the past, students did not know where or when these courses were taking place.")
    add_p(doc, "The NagrikSetu Skill Development Service solves this by bringing all government-approved training courses onto a single, easy-to-use website. Any student with a mobile phone or computer can see all 208 active courses, find the nearest government training centre, apply online in two minutes, and track their daily learning progress until they receive their course certificate.")

    # 2. Problems Addressed
    add_h1(doc, "2. Problems the Service Solves")
    add_p(doc, "Before this website was created, the vocational training system in Karnataka faced five major difficulties that hurt students and caused waste in government funds:")
    add_bullet(doc, "1. Lack of Information in Villages and Towns:", "Course announcements were printed in small newspaper notices or pasted on walls inside district government offices. Students living in rural areas or small towns had no way of knowing when a new course was starting until admissions were already closed.")
    add_bullet(doc, "2. Wasted Money and Travel on Paper Forms:", "To apply for a simple computer course, a student had to travel by bus to the district capital, take photocopies of school marksheets and certificates, stand in long queues, and submit paper forms. This cost poor families hard-earned money and wasted several days.")
    add_bullet(doc, "3. Cheating by Middlemen and Brokers:", "Because paper rules were hard to understand, unauthorized agents hung around government offices. They cheated poor students by taking 1,000 to 2,000 rupees and promising them a 'guaranteed seat', even though government courses were completely free.")
    add_bullet(doc, "4. Overcrowded Classes and Full Batches:", "Training centres have physical limits—usually 25 or 30 computers in a lab. But without a shared database, centres continued accepting paper applications after batches were full. Many students waited weeks only to be turned away at the last minute.")
    add_bullet(doc, "5. Fake Attendance Registers:", "Paper attendance notebooks could be easily changed or signed falsely. Some centres marked fake student names to claim government grants. Honest students missed out on practical training.")

    # 3. Objectives
    add_h1(doc, "3. Main Project Objectives")
    add_p(doc, "We designed the NagrikSetu Skill Development Service with six practical, straightforward objectives:")
    add_bullet(doc, "1. Put All Courses Online:", "Show all 208 active courses openly on the website so any citizen can browse them without asking anyone or paying any money.")
    add_bullet(doc, "2. Real Training Centres Only:", "Connect all courses directly to 10 approved government training centres across Karnataka, showing real classroom locations, phone numbers, and trainer names.")
    add_bullet(doc, "3. Give Every Student One Permanent ID:", "Assign a single, unique Student ID (like STU-2026-000104) to each enrolled learner. This ID stays with the student forever, keeping all course history safe.")
    add_bullet(doc, "4. Clear User Roles:", "Give each user the exact right screen—students see their portal, centre managers see their local batches, and state admins supervise the entire system safely.")
    add_bullet(doc, "5. Honest Attendance Tracking:", "Enforce a strict 75% minimum attendance rule so only students who actually come to class and practice get course certificates.")
    add_bullet(doc, "6. Skill-Gap Help for Careers:", "Provide a simple tool where students can check what skills they need for specific jobs and see recommended courses to fill those gaps.")

    # 4. Target Users
    add_h1(doc, "4. Who Uses the System (Target Users)")
    add_p(doc, "The website is built to support five different groups of people, giving each group the exact tools they need:")
    
    users_data = [
        ["User Group", "How They Log In", "What They Can Do on the Website"],
        ["Public Citizen", "Mobile number or Email", "Can browse all 208 courses, search centres, check skill gaps, and apply for open batches."],
        ["Enrolled Student", "Email or Student ID (e.g. STU-2026-000104)", "Has a dedicated Student Portal to view batch schedule, trainer contact, daily attendance, topic checklist, and certificate."],
        ["Faculty Trainer", "Official staff email", "Conducts practical lab sessions, marks daily attendance, and checks off topics as students finish them."],
        ["Training Centre Admin", "Centre manager account", "Manages local batches, approves or rejects applications, verifies seat capacity, and views enrolled students."],
        ["State Admin", "Department admin account", "Views statewide statistics, audits centre performance, checks system logs, and oversees catalogue integrity in a safe view-only mode."]
    ]
    build_table(doc, users_data[0], users_data[1:], [1.6, 2.0, 3.1])

    # 5. Main Features
    add_h1(doc, "5. Main Features of the Website")
    add_p(doc, "The website includes several practical, well-tested features that make the skilling process simple and transparent:")
    
    add_h2(doc, "A. 7 Simple Skill Categories (208 Total Active Courses)")
    add_p(doc, "The course catalogue organizes all 208 active courses into seven practical economic areas that match real jobs in Karnataka:")
    
    cat_data = [
        ["Skill Category", "Active Courses", "Example Practical Courses Offered"],
        ["Information Technology & Computers", "48 courses", "Python Web Programming, Cloud Computing, Cyber Security, UI Design"],
        ["Business & Management", "32 courses", "Digital Marketing, Financial Accounting, GST Filing, Office Administration"],
        ["Healthcare & Medical Services", "26 courses", "Emergency Medical Technician, Phlebotomy, Patient Care Assistant"],
        ["Engineering, Electrical & Mechanical", "38 courses", "Electric Vehicle Technician, CNC Machine Operator, Solar Panel Installer"],
        ["Agriculture & Food Processing", "24 courses", "Precision Farming, Organic Food Processing, Cold Chain Management"],
        ["Media, Arts & Communication", "22 courses", "Video Editing, Digital Photography, Graphic Design, Animation"],
        ["Tourism, Hospitality & Catering", "18 courses", "Front Office Management, Culinary Arts, Bakery & Pastry Making"]
    ]
    build_table(doc, cat_data[0], cat_data[1:], [2.2, 1.2, 3.3])

    add_h2(doc, "B. Training Centre Search with Distance Details")
    add_p(doc, "Students do not have to guess where a course is taught. They can select their home district or type their town name to find nearby government training centres. The website shows the centre's street address, contact phone number, and open course batches.")

    add_h2(doc, "C. Automatic Seat Limit per Batch")
    add_p(doc, "Every batch has a fixed seat limit (such as 30 seats per computer lab). The website counts seats in real time from the database. When seats are available, students see 'Seats Available'. When the batch fills up, the button changes to 'Batch Full', preventing false promises.")

    add_h2(doc, "D. Dedicated Student Portal")
    add_p(doc, "Once admitted, a student can click on 'Student Portal' from the navigation bar. This clean screen shows their batch timing, trainer name and email, cumulative attendance percentage, a green topic checklist, and their final certificate.")

    # 6. Approved Training Centres
    add_h1(doc, "6. Approved Government Training Centres")
    add_p(doc, "The system connects directly to 10 approved government training centres located in key districts across Karnataka. Each centre has dedicated classrooms, practical equipment, qualified trainers, and an appointed centre administrator:")
    
    centres_data = [
        ["Centre Code", "Centre Name", "District", "Sample Courses Provided"],
        ["CTR-0001", "Bengaluru Central Skilling Institute", "Bengaluru Urban", "Python Programming, Cyber Security, Cloud Computing"],
        ["CTR-0002", "Mysuru Heritage Technical Training Centre", "Mysuru", "Hospitality Management, Bakery, Digital Marketing"],
        ["CTR-0003", "Hubballi-Dharwad Industrial Training Hub", "Dharwad", "CNC Machining, Electrical Maintenance, Welding"],
        ["CTR-0004", "Mangaluru Coastal Marine & IT Academy", "Dakshina Kannada", "Web Development, Export Logistics, Tourism"],
        ["CTR-0005", "Kalaburagi Regional Skill Development Centre", "Kalaburagi", "Solar Installation, Precision Farming, Office Tools"],
        ["CTR-0006", "Belagavi Advanced Manufacturing Institute", "Belagavi", "Automotive Repair, Tool Making, Accounting with Tally"],
        ["CTR-0007", "Ballari Mineral Belt Vocational Institute", "Ballari", "Heavy Machinery, Industrial Safety, Basic Electronics"],
        ["CTR-0008", "Davanagere Textile & Agro Skilling Centre", "Davanagere", "Garment Manufacturing, Food Processing, Retail Sales"],
        ["CTR-0009", "Tumakuru Engineering Trades Centre", "Tumakuru", "Electric Vehicle Servicing, Mobile Phone Repair, Plumbing"],
        ["CTR-0010", "Shivamogga Malnad Skill Academy", "Shivamogga", "Organic Farming, Python Basics, Patient Healthcare Support"]
    ]
    build_table(doc, centres_data[0], centres_data[1:], [1.1, 2.3, 1.3, 2.0])

    # 7. Step-by-Step How It Works
    add_h1(doc, "7. Step-by-Step How the Service Works")
    add_p(doc, "The entire journey from a citizen visiting the website to graduating with a certificate takes place in four simple, clear steps:")
    add_bullet(doc, "Step 1: Explore and Find a Course:", "The citizen opens the website on their phone or laptop. They browse the 208 courses by category, read what topics are taught, and check which nearby centre offers the course.")
    add_bullet(doc, "Step 2: Apply Online in Two Minutes:", "The citizen creates an account using their name, email, and phone number. They select an open batch at their preferred centre and click 'Submit Application'. The system immediately gives them an application tracking number.")
    add_bullet(doc, "Step 3: Centre Review and Admission:", "The training centre manager logs in and reviews the application. If the candidate meets the minimum requirements and seats are open, the manager clicks 'Approve'. The student is given their permanent Student ID (e.g. STU-2026-000104).")
    add_bullet(doc, "Step 4: Attend Classes and Earn Certificate:", "The student attends daily classes. The trainer marks attendance in the system. The student checks their portal to see their progress. Once they finish all topics and maintain at least 75% attendance, they complete the course and receive their verified certificate.")

    # 8. Benefits
    add_h1(doc, "8. Benefits for Students and Society")
    add_p(doc, "The NagrikSetu Skill Development Service provides real, measurable advantages to young people and the state government:")
    add_bullet(doc, "1. Zero Cost and No Middlemen:", "Courses are completely free. Because applications are submitted directly online, no broker or agent can cheat students.")
    add_bullet(doc, "2. Real Practical Skills for Employment:", "Courses are designed with industry inputs. Students spend time in labs working on computers and machinery, making them ready for immediate hiring.")
    add_bullet(doc, "3. Fair Opportunities for Rural Youth and Women:", "Students living in small towns and villages have the exact same access to course information as those in Bengaluru. Flexible batch timings encourage young women to join vocational training.")
    add_bullet(doc, "4. Efficient Use of Government Money:", "Because attendance is tracked daily and seats cannot be double-booked, government training budgets are spent only on genuine students who actively attend.")

    # 9. Technology Stack
    add_h1(doc, "9. Technology Stack Used in the Project")
    add_p(doc, "The project is built using modern, reliable open-source programming tools that run smoothly inside Docker containers:")
    
    tech_data = [
        ["Component", "Software / Framework", "Why We Used It in Simple Terms"],
        ["Backend API", "Python with FastAPI", "FastAPI is very fast, handles many requests easily, and makes writing clean REST APIs straightforward."],
        ["Frontend UI", "React 18 with Tailwind CSS", "Provides a clean, modern web interface that opens quickly on both mobile phones and desktop computers."],
        ["Database", "MySQL 8.4 Enterprise Relational DB", "Stores all user accounts, courses, centres, batches, and attendance safely with strong relational rules."],
        ["Security", "JWT (JSON Web Tokens) & Bcrypt", "Keeps passwords securely encrypted and ensures users can only see the screens they are allowed to see."],
        ["Deployment", "Docker & Docker Compose", "Packages the entire system into self-contained units so it runs identically on any computer or server."]
    ]
    build_table(doc, tech_data[0], tech_data[1:], [1.6, 2.1, 3.0])

    # 10. Conclusion
    add_h1(doc, "10. Conclusion")
    add_p(doc, "The NagrikSetu Skill Development Service provides a clean, modern, and transparent way for the Government of Karnataka to train young citizens for real jobs. By replacing paper forms and notice boards with an easy-to-use website, the system removes middlemen, stops overcrowded classrooms, tracks daily attendance honestly, and gives every student a permanent digital record of their achievements.")
    add_p(doc, "The project proves that when modern software engineering is applied to public governance, it creates direct, positive change in the lives of ordinary students, helping them build rewarding careers and support their families.")

    out_path = os.path.join(OUT_DIR, "01_About_the_Service.docx")
    doc.save(out_path)
    print(f"[OK] Report 1 generated: {out_path}")

if __name__ == "__main__":
    generate_report_1_simplified()
