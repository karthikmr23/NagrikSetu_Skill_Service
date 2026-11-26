# -*- coding: utf-8 -*-
"""Generate Simplified Report 2: 02_Functional_Requirements.docx (5-8 pages) using simple, natural student words."""
import os, sys
sys.path.append(r"C:\Users\karth\OneDrive\Documents\NagrikSetu_Skill_Development_FINAL")
from generate_docs_base import (
    docx, OUT_DIR, setup_page, create_title_page,
    add_h1, add_h2, add_p, add_bullet, build_table
)

def generate_report_2_simplified():
    doc = docx.Document()
    setup_page(doc, "Functional Requirements")
    create_title_page(
        doc,
        doc_title="Functional Requirements Specification",
        subtitle="A Simple and Complete Guide to What the Software Does, User Roles, Main Features, How Data Moves, and Error Rules",
        doc_ref="SDS-RPT-02-FRS"
    )

    # Document Overview & TOC
    add_h1(doc, "Document Overview & Quick Table of Contents")
    add_p(doc, "This Functional Requirements Specification (FRS) explains in clear, simple terms exactly what the NagrikSetu Skill Development Service software does. It describes each user role, every main feature, how data is saved in the database, and what happens when an error occurs.")
    add_p(doc, "All explanations are written in straightforward, natural English suitable for a second-year college student. Confusing technical jargon has been kept to a minimum so that any examiner can review the document without finding overly complex theory.")

    toc_data = [
        ["Chapter / Topic", "What is Explained in this Section", "Section"],
        ["1. Introduction to Requirements", "What this software does and why functional requirements matter", "Section 1"],
        ["2. User Roles and Permissions", "The 4 real user roles: Citizen, Student, Centre Admin, and State Admin", "Section 2"],
        ["3. Detailed Functional Requirements", "Simple list of features (FR-01 to FR-14) that actually exist in the software", "Section 3"],
        ["4. User Registration and Login", "How citizens sign up and how students log in using their email or Student ID", "Section 4"],
        ["5. Main Features and Modules", "Catalogue search, centre locator, application form, student portal, attendance", "Section 5"],
        ["6. Step-by-Step User Workflows", "How an application moves from Pending to Approved, Enrolled, and Completed", "Section 6"],
        ["7. Admin and Centre Controls", "How centre managers handle batches and why state admin has view-only access", "Section 7"],
        ["8. Database Tables & Information", "The main MySQL tables: users, skills, centres, enrollments, and attendance", "Section 8"],
        ["9. Input and Output Examples", "What a user enters on the screen and what the system shows in return", "Section 9"],
        ["10. Error Handling Rules", "How the website handles wrong passwords, full batches, or unauthorized access", "Section 10"],
        ["11. Project Conclusion", "Final engineering summary of the system requirements", "Section 11"]
    ]
    build_table(doc, toc_data[0], toc_data[1:], [2.2, 3.3, 1.0])

    # 1. Introduction
    add_h1(doc, "1. Introduction to System Requirements")
    add_p(doc, "The NagrikSetu Skill Development Service is a web application built to connect students across Karnataka with free, government-sponsored practical training courses. To make sure the application works reliably for thousands of citizens, we need clear functional requirements.")
    add_p(doc, "A functional requirement simply describes what the software must do when a user performs an action—for example, when a citizen searches for a course, submits an application, or when a teacher marks attendance. Every requirement listed in this document is actually implemented in the running Python (FastAPI) backend and React frontend.")

    # 2. User Roles
    add_h1(doc, "2. User Roles and Access Permissions")
    add_p(doc, "To keep the system organized and secure, different users see different screens based on their role:")
    
    roles_table = [
        ["Role Name", "Who This User Is", "What They Can See & Do", "Access Restrictions"],
        ["Public Citizen", "Any resident or learner", "Can browse courses, search centres, check skill gaps, and apply for open batches.", "Cannot see student portals or edit centre records."],
        ["Enrolled Student", "Admitted trainee (with Student ID)", "Can log in via email OR Student ID, view batch schedule, attendance %, topic checklist, and certificate.", "Cannot access other students' private records or admin screens."],
        ["Faculty Trainer", "Appointed classroom instructor", "Views assigned batches, marks daily attendance, and checks off topics as students learn.", "Can only see batches assigned to them."],
        ["Training Centre Admin", "Centre manager (e.g. CTR-0001)", "Reviews applications, approves or rejects seats, views local batch lists and enrolled trainees.", "Can ONLY see their own centre's data (strictly isolated)."],
        ["State / Platform Admin", "Skill Department director", "Supervises statewide performance, checks centre directories, reviews logs and counts.", "Strictly VIEW-ONLY; cannot alter or delete live operational data."]
    ]
    build_table(doc, roles_table[0], roles_table[1:], [1.6, 1.5, 2.2, 1.4])

    # 3. Core Functional Requirements
    add_h1(doc, "3. Detailed Functional Requirements (FR-01 to FR-14)")
    add_p(doc, "The following requirements define exactly what features the software provides:")
    
    fr_data = [
        ["Req ID", "Requirement Title", "Simple Description of What the Feature Does"],
        ["FR-01", "Citizen Account Registration", "New users can create an account by entering their full name, email address, phone number, and password. The system checks for valid email format and securely encrypts passwords."],
        ["FR-02", "Dual-Identifier Login", "Enrolled students can log in using either their registered email address OR their unique Student ID (e.g. STU-2026-000104) along with their password."],
        ["FR-03", "Standard Course Catalogue", "The website displays all 208 active courses neatly organized into 7 categories. Users can filter by category or difficulty level, and see actual database-backed student counts."],
        ["FR-04", "Course Syllabus and Details", "Clicking on any course opens a detailed page showing total hours, prerequisites, key learning topics, and which training centres are currently offering the course."],
        ["FR-05", "Training Centre Locator", "Users can search for approved training centres by district or location, viewing complete addresses, phone numbers, and available batches."],
        ["FR-06", "Online Application Form", "Citizens can apply for an open batch with a single click. The system verifies that seats are available before accepting the application and gives an application ID."],
        ["FR-07", "Application Review System", "Centre admins review pending applications, verify candidate details, and either approve or reject them with clear remarks."],
        ["FR-08", "Permanent Student ID Generation", "When a student is approved and enrolled for the first time, the system generates a permanent Student ID (e.g. STU-2026-000104) that stays with them forever."],
        ["FR-09", "Student Portal Dashboard", "Enrolled students have a dedicated portal showing their current batch timing, trainer name, daily attendance percentage, and course completion progress."],
        ["FR-10", "Daily Attendance Tracking", "Trainers mark student attendance online. The system automatically calculates attendance percentages and shows a warning if attendance falls below 75%."],
        ["FR-11", "Topic Progress Checklist", "The student portal shows a green checklist of syllabus topics. As the teacher covers each practical lesson, topics are marked complete."],
        ["FR-12", "Skill-Gap Analysis Tool", "Citizens can select their education and desired job to see a match score and get recommendations on which courses will help them qualify."],
        ["FR-13", "Centre Data Privacy", "A training centre administrator can only see students and batches belonging to their own centre. They cannot view or modify another centre's data."],
        ["FR-14", "State Admin Safety Guard", "The state administrator dashboard is strictly view-only to prevent accidental deletion or alteration of active training records."]
    ]
    build_table(doc, fr_data[0], fr_data[1:], [1.0, 2.0, 3.7])

    # 4. User Registration and Login
    add_h1(doc, "4. User Registration and Login Workflows")
    add_p(doc, "Joining the platform is designed to be simple for any citizen, even if they have limited computer experience:")
    add_p(doc, "1. Registration: A citizen clicks 'Sign Up', types their full name, valid email, 10-digit mobile number, and sets a password. The system checks that the email is not already registered and saves the account securely.")
    add_p(doc, "2. Citizen Login: A citizen can log in using their email and password. Upon login, the system creates a secure session token (JWT) that remembers who they are.")
    add_p(doc, "3. Student ID Login: Once a student is officially enrolled in a training programme, the system issues them a unique Student ID (e.g. STU-2026-000104). The student can now type either their email or their Student ID into the login box. The system automatically detects whether a Student ID or an email was typed, looks up the account, checks the password, and opens the Student Portal directly.")

    # 5. Main Functional Modules
    add_h1(doc, "5. Main Functional Modules of the Application")
    add_p(doc, "The software is divided into five core functional modules that work together smoothly:")
    
    add_h2(doc, "Module 1: Skill Catalogue and Course Browser")
    add_p(doc, "This module lets users browse the 208 active courses. It includes a search bar to find courses by name, category filter buttons, and clean cards displaying course duration and active enrolments.")

    add_h2(doc, "Module 2: Training Centre Directory")
    add_p(doc, "This module lists the 10 approved training centres in Karnataka. It provides complete contact information, phone numbers, emails, and active courses offered at each centre.")

    add_h2(doc, "Module 3: Application & Admission Engine")
    add_p(doc, "This module handles online applications. It checks seat limits automatically so that batches never exceed physical lab capacity. It tracks status changes from Pending to Approved.")

    add_h2(doc, "Module 4: Student Learning Portal")
    add_p(doc, "The personal dashboard for enrolled students. It displays their batch schedule, teacher contact details, real-time attendance percentage, and the topic checklist.")

    add_h2(doc, "Module 5: Centre & Administrative Portal")
    add_p(doc, "The management interface for centre administrators to review applications and verify attendance, and for state administrators to oversee statewide statistics.")

    # 6. User Workflows
    add_h1(doc, "6. Step-by-Step User Workflows")
    add_p(doc, "The application lifecycle follows a clean, sequential workflow from start to finish:")
    add_bullet(doc, "Status 1 - PENDING:", "When a citizen clicks 'Apply Now', an application record is created with the status 'PENDING'. The applicant can see this in 'My Applications'.")
    add_bullet(doc, "Status 2 - UNDER_REVIEW:", "The centre manager opens their portal and marks the application 'UNDER_REVIEW' while checking minimum educational qualifications.")
    add_bullet(doc, "Status 3 - APPROVED:", "If qualifications are verified and seats are open, the status becomes 'APPROVED'. The student receives an admission notification.")
    add_bullet(doc, "Status 4 - ENROLLED:", "The student is assigned a permanent Student ID (e.g. STU-2026-000104), added to the batch roster, and can now open the Student Portal.")
    add_bullet(doc, "Status 5 - IN_PROGRESS:", "Classes begin. The student attends daily sessions, and the trainer marks attendance and topic completions.")
    add_bullet(doc, "Status 6 - COMPLETED:", "The student finishes all topics, maintains at least 75% attendance, passes the practical test, and receives their course certificate.")

    # 7. Admin Controls
    add_h1(doc, "7. Admin and Centre Controls")
    add_p(doc, "To prevent unauthorized changes and protect student data, the software enforces two important rules:")
    add_bullet(doc, "1. Centre Privacy (Horizontal Isolation):", "A centre administrator logged in at Shivamogga (CTR-0010) can only view and manage students enrolled in Shivamogga. If they try to look up or modify a student in Bengaluru (CTR-0001), the system blocks the request with an HTTP 403 Forbidden error.")
    add_bullet(doc, "2. State Admin View-Only Safety Guard:", "The State / Platform Admin dashboard provides high-level monitoring across all 10 centres. To prevent accidental loss of operational data or unintended modifications, all administrative endpoints in this view are strictly read-only.")

    # 8. Database Tables
    add_h1(doc, "8. Relational Database Tables")
    add_p(doc, "All system information is stored safely in a MySQL 8.4 relational database across five main tables:")
    
    db_table = [
        ["Table Name", "What It Stores", "Key Columns in Simple Terms"],
        ["accounts", "All user logins and profiles", "id, citizen_ref, full_name, email, phone, hashed_password, role, student_id, is_student"],
        ["skills", "The 208 active training courses", "id, skill_code, name, category, subcategory, duration_hours, difficulty_level, is_active"],
        ["training_centres", "The 10 approved government centres", "id, centre_code, name, district, address, contact_phone, contact_email, is_approved"],
        ["training_batches", "Class batches and seat limits", "id, batch_code, skill_id, centre_id, trainer_name, total_seats, enrolled_count, start_date"],
        ["enrollments", "Student course applications", "id, citizen_ref, batch_id, status (PENDING, ENROLLED, etc.), created_at, remarks"]
    ]
    build_table(doc, db_table[0], db_table[1:], [1.6, 2.3, 2.8])

    # 9. Input and Output Examples
    add_h1(doc, "9. Input and Output Examples")
    add_p(doc, "Here is an example of what information enters the system and what comes out:")
    add_bullet(doc, "Input - Student Course Application:", "The student submits their Citizen Reference (`CITIZEN-00104`), the requested Batch Code (`BTC-PY-001`), and their preferred training centre (`CTR-0010`).")
    add_bullet(doc, "Output - Application Confirmation:", "The system responds with HTTP 201 Created, returning an Application Tracking Number (`APP-2026-9042`), current status `PENDING`, and remaining batch seats.")

    # 10. Error Handling Rules
    add_h1(doc, "10. Error Handling Rules")
    add_p(doc, "When something goes wrong, the website provides clear, helpful messages instead of crashing:")
    add_bullet(doc, "Wrong Password or Email (HTTP 401):", "Shows: 'Invalid email/Student ID or password. Please check your credentials.'")
    add_bullet(doc, "Batch is Full (HTTP 400):", "Shows: 'This batch has reached its maximum seat limit. Please select another upcoming batch.'")
    add_bullet(doc, "Access Denied (HTTP 403):", "Shows: 'You do not have permission to view or edit this training centre's records.'")
    add_bullet(doc, "Course Not Found (HTTP 404):", "Shows: 'The requested course does not exist or is currently inactive.'")

    # 11. Conclusion
    add_h1(doc, "11. Conclusion")
    add_p(doc, "This Functional Requirements Specification clearly defines all operational capabilities of the NagrikSetu Skill Development Service. By establishing clear user roles, automatic seat counting, transparent online applications, daily attendance rules, and secure student records, the system provides a dependable software foundation for vocational education across Karnataka.")

    out_path = os.path.join(OUT_DIR, "02_Functional_Requirements.docx")
    doc.save(out_path)
    print(f"[OK] Report 2 generated: {out_path}")

if __name__ == "__main__":
    generate_report_2_simplified()
