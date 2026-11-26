# -*- coding: utf-8 -*-
"""Generate Simplified Report 3: 03_Problem_Statement_and_Business.docx using plain, easy student words."""
import os, sys
sys.path.append(r"C:\Users\karth\OneDrive\Documents\NagrikSetu_Skill_Development_FINAL")
from generate_docs_base import (
    docx, OUT_DIR, setup_page, create_title_page,
    add_h1, add_h2, add_p, add_bullet, build_table
)

def generate_report_3_simplified():
    doc = docx.Document()
    setup_page(doc, "Problem Statement & Business")
    create_title_page(
        doc,
        doc_title="Problem Statement & Business",
        subtitle="A Simple and Clear Study of Real Problems in Job Training, How NagrikSetu Solves Them, and Direct Benefits for Students and Training Centres",
        doc_ref="SDS-RPT-03-BUSINESS"
    )

    # Document Overview
    add_h1(doc, "Document Overview & Quick Table of Contents")
    add_p(doc, "This report explains why the NagrikSetu Skill Development Service was created, what problems students and training centres faced before this website, and how the new system makes joining and completing training courses simple and clear.")
    add_p(doc, "All explanations in this report are written in plain, direct English suitable for a second-year college student. Difficult corporate words, unnecessary technical jargon, and confusing theory have been removed so that any reader or examiner can understand the project easily without asking tricky questions.")

    toc_data = [
        ["Chapter / Topic", "What is Explained in this Section", "Section"],
        ["1. Background of the Problem", "Why young people in Karnataka need practical training to get jobs", "Section 1"],
        ["2. Problems in the Old System", "Real issues like travel costs, paperwork, brokers, and lack of course details", "Section 2"],
        ["3. Simple Problem Statement", "A clear 2-sentence summary of the main problem we solved", "Section 3"],
        ["4. How NagrikSetu Solves It", "The website solution: courses list, centre search, online forms, student ID", "Section 4"],
        ["5. Main Project Objectives", "Simple goals: transparent seats, regular attendance, verified certificates", "Section 5"],
        ["6. Who Gets Benefits", "Clear benefits for students, training centres, teachers, and government", "Section 6"],
        ["7. Old Process vs New Process", "A simple table showing how things worked before and how they work now", "Section 7"],
        ["8. What Good Things Happen", "Better jobs, fair chances for girls, skills for rural youth", "Section 8"],
        ["9. Real Examples from the Project", "Story of a student joining a course and a centre managing its seats", "Section 9"],
        ["10. Simple Conclusion", "Final summary of how the website helps students build careers", "Section 10"]
    ]
    build_table(doc, toc_data[0], toc_data[1:], [2.2, 3.3, 1.0])

    # 1. Background of the Problem
    add_h1(doc, "1. Background of the Problem")
    add_p(doc, "Karnataka is one of the fastest-growing states in India. Big cities like Bengaluru, Mysuru, Hubballi, and Mangaluru have thousands of companies working in computer software, electronics, hospitals, hotels, car making, and modern farming. These companies want to hire workers who know how to do practical work, like writing code, fixing machines, running lab equipment, or managing accounts.")
    add_p(doc, "At the same time, thousands of young boys and girls finish their 10th standard, 12th standard, ITI, or diploma courses every year. Many of them live in towns and villages like Davanagere, Shivamogga, Belagavi, or Kalaburagi. They want to work and support their families, but they do not have the exact practical skills that companies ask for.")
    add_p(doc, "College books usually teach theory, but companies want hands-on experience. Private coaching institutes charge very high fees—often 20,000 to 50,000 rupees—which poor families cannot afford. The Karnataka government already runs many free or low-cost training courses to help young people learn these skills, but people did not know where or how to join them.")

    # 2. Existing Problems
    add_h1(doc, "2. Problems in the Old System (Before NagrikSetu)")
    add_p(doc, "Before this project was built, getting into a government training course was very difficult for a normal person. Here are the real problems that happened:")
    add_bullet(doc, "1. Nobody Knew Which Courses Were Open:", "Information was printed in local newspapers or stuck on notice boards inside government offices. If a student lived in a village 20 kilometers away, they had no way of knowing when a new batch was starting or what courses were available.")
    add_bullet(doc, "2. Too Much Paperwork and Travel:", "To submit an application form, a student had to make photocopies of marks cards, get caste and income certificates, travel by bus to the district office, wait in long lines, and submit paper files. This cost poor families money and wasted days of time.")
    add_bullet(doc, "3. Cheating by Middlemen and Brokers:", "Because paper rules were confusing, local brokers and agents hung around government offices. They told poor students, 'Pay me 1,000 rupees and I will guarantee your free seat.' In reality, the courses were already free, and brokers were cheating students.")
    add_bullet(doc, "4. Full Batches and Wasted Trips:", "Centres had only 25 or 30 seats per computer lab. But because there was no computer system to count seats, centres kept taking paper forms even when seats were full. Students waited for weeks only to be told that the batch was already closed.")
    add_bullet(doc, "5. Fake Attendance on Paper Registers:", "Teachers marked attendance on paper notebooks. Sometimes students came for only two days, but their names stayed on paper registers so the centre could claim government money. Real, interested students were denied seats.")
    add_bullet(doc, "6. Easy-to-Lose Paper Certificates:", "When students completed a course, they got a simple paper certificate. If it was lost or damaged in rain, getting a copy took months. Also, employers could not easily verify if the paper was genuine.")

    # 3. Simple Problem Statement
    add_h1(doc, "3. Simple Problem Statement")
    add_p(doc, "The problem we set out to solve can be stated in very simple terms:")
    add_p(doc, "\"Students in Karnataka who want job training could not easily find courses, faced too much paperwork and cheating by middlemen, and had no clear way to track their admission or certificates. Training centres also had no simple way to manage their seat limits, track daily attendance, and report real student progress to the government.\"")

    # 4. Proposed Solution
    add_h1(doc, "4. The Solution: NagrikSetu Skill Development Service")
    add_p(doc, "NagrikSetu Skill Development Service solves all these problems by putting the entire system on a clean, simple website. Here is how it works in real life:")
    add_bullet(doc, "1. Open Online Course List:", "A student can open the website from any mobile phone or computer. They can clearly see all 208 active courses neatly divided into 7 simple areas: Computers & IT, Business, Health, Technical Trades, Agriculture, Media, and Hotels/Tourism.")
    add_bullet(doc, "2. Real Training Centre Search:", "Students can type their city or district—like Bengaluru, Mysuru, or Shivamogga—and immediately see real government-approved training centres, their real addresses, phone numbers, and available courses.")
    add_bullet(doc, "3. Direct Online Application:", "No paper forms. A citizen creates a simple account with their name, mobile number, and email. They click on a course, pick an open batch, and click 'Apply Now.'")
    add_bullet(doc, "4. Automatic Seat Counting:", "Every batch has a fixed number of seats (like 30 seats). When a student is admitted, the system automatically subtracts 1 seat. When 0 seats are left, the website clearly shows the batch is full, so nobody is misled.")
    add_bullet(doc, "5. One Permanent Student ID:", "When a student joins their first course, the system gives them one permanent Student ID (like STU-2026-000104). Even if they take another course next year, their Student ID stays the same, keeping all their history safe in one place.")
    add_bullet(doc, "6. Student Portal Dashboard:", "After logging in, students have their own personal dashboard. They can see their course name, teacher name, attendance percentage, topic checklist, and download their certificate.")

    # 5. Business Objectives
    add_h1(doc, "5. Main Project Objectives")
    add_p(doc, "We built this project to reach five straightforward goals:")
    
    obj_data = [
        ["Project Goal", "How We Measure It", "Why It Matters to Real People"],
        ["Equal Course Access", "208 active courses online", "Students in small villages see the exact same courses as students in Bengaluru."],
        ["Zero Overcrowded Batches", "Automatic seat limit per batch", "Every student gets a computer and proper equipment during practical classes."],
        ["Honest Attendance Tracking", "75% minimum attendance rule", "Only students who actually attend classes and learn can pass and get certificates."],
        ["One ID for One Student", "Unique Student ID in database", "Prevents fake duplicate names and keeps complete learning records clean."],
        ["No Middlemen Cheating", "Direct online self-apply button", "Students apply directly for free without paying bribes or agent fees."]
    ]
    build_table(doc, obj_data[0], obj_data[1:], [1.8, 1.8, 2.9])

    # 6. Who Gets Benefits
    add_h1(doc, "6. Target Users and Who Gets Benefits")
    add_bullet(doc, "Young Students and Job Seekers:", "They can browse courses for free, find nearby centres, apply in 2 minutes, see their daily attendance, and show verifiable online certificates to interviewers.")
    add_bullet(doc, "Training Centre Managers:", "They do not have to manage paper files. They log into their dashboard, see new applications, click 'Approve' or 'Reject' with clear reasons, and see their batch seats update automatically.")
    add_bullet(doc, "Course Teachers (Trainers):", "Teachers can see who is in their class, take attendance quickly, and mark off topics as they teach them.")
    add_bullet(doc, "Companies and Employers:", "Employers can trust that a student with a NagrikSetu certificate really completed the course, attended at least 75% of classes, and learned practical topics.")
    add_bullet(doc, "Government Department:", "State officers in Bengaluru can see clean numbers on their screen: total active centres (10), total courses (208), total programmes (125), and total students enrolled, without waiting for monthly paper reports.")

    # 7. Old Process vs New Process
    add_h1(doc, "7. Business Process Re-Engineering (Before vs. After)")
    add_p(doc, "The table below clearly compares the manual paper process with the new NagrikSetu website process:")
    
    compare_data = [
        ["Step in Process", "How It Worked Before (Old Way)", "How It Works in NagrikSetu (New Way)"],
        ["Finding Courses", "Word of mouth, old posters, asking friends", "Open website on phone; search all 208 courses instantly"],
        ["Finding Centres", "Walking to offices, asking around town", "Search by city, district, or GPS distance (1 to 25 km)"],
        ["Submitting Forms", "Paper forms, long lines, paying xerox money", "Fill simple online form in 2 minutes from home"],
        ["Seat Limits", "Nobody knew; batches got crowded or cancelled", "Live seat counter shows open seats; locks when full"],
        ["Student ID", "Different paper roll number for every class", "One permanent Student ID (e.g., STU-2026-000104)"],
        ["Checking Attendance", "Handwritten notebooks, easy to fake", "Recorded on database; shows clear percentage (e.g., 90%)"],
        ["Getting Certificate", "Paper paper printed weeks later, easy to lose", "Digital certificate saved in account, viewable anytime"],
        ["Admin Reports", "Calling district offices, counting paper sheets", "Live dashboard shows all 10 centres and real student counts"]
    ]
    build_table(doc, compare_data[0], compare_data[1:], [1.6, 2.4, 2.5])

    # 8. Expected Outcomes
    add_h1(doc, "8. Expected Outcomes and Real-World Value")
    add_bullet(doc, "1. More Young People Get Good Jobs:", "When students learn practical skills that companies actually need, they pass interviews faster and get better starting salaries.")
    add_bullet(doc, "2. Help for Rural and Poor Students:", "A student in a small village does not need to move to Bengaluru just to find out about technical training. They can learn at their nearest regional centre like Shivamogga, Belagavi, or Davanagere.")
    add_bullet(doc, "3. Fair Chances for Girls:", "Because applications are done online and centres are verified government locations, girls and their parents feel safe and confident applying for technical and computer courses.")
    add_bullet(doc, "4. 100% Tax Money Reaches Real Students:", "Because attendance is tracked and student IDs cannot be duplicated, government money goes only to real classrooms and real teachers.")

    # 9. Practical Use Cases
    add_h1(doc, "9. Practical Real-World Scenarios")
    
    add_h2(doc, "Scenario 1: A Student Joining a Python Course in Shivamogga")
    add_p(doc, "Karthik is a 20-year-old student living in a village near Shivamogga. He finished his diploma in computer engineering, but local colleges only taught basic theory. He opens http://localhost:5173 on his phone.")
    add_p(doc, "He searches for 'Python' and sees 'Django Enterprise Web Framework' (Program 19) offered at Shivamogga Malnad Skill Development Centre (CTR-0010). The centre is only 15 minutes away from his bus stand. He clicks 'Apply Now', writes a short note saying he wants to be a web developer, and submits.")
    add_p(doc, "The centre manager logs into their account, sees Karthik's application, checks his details, and clicks 'Enroll'. The system gives Karthik his permanent Student ID: STU-2026-000104.")
    add_p(doc, "When classes start, teacher Dr. Rajeshwar Sharma takes daily attendance. Karthik attends 18 out of 20 classes (90% attendance). On his Student Portal, Karthik sees all 5 modules get marked green as he finishes them. At the end, he gets an official digital certificate that he can show in company interviews.")

    add_h2(doc, "Scenario 2: A Centre Manager Managing 30 Seats in Bengaluru")
    add_p(doc, "The manager at Bengaluru Central Skill Hub (CTR-0001) in Rajajinagar starts a new batch for Web Development. The computer lab has 30 computers, so the batch capacity is set to 30.")
    add_p(doc, "Over two weeks, 45 students apply online. As the manager approves qualified students, the available seat counter drops: 30, 29, 28... down to 0.")
    add_p(doc, "When all 30 seats are filled, the website automatically shows 'Batch Full'. The remaining 15 students are not left in confusion; the system suggests they join the morning batch or look at nearby courses. No overcrowding happens in the lab, and every admitted student gets their own computer.")

    # 10. Conclusion
    add_h1(doc, "10. Conclusion")
    add_p(doc, "The NagrikSetu Skill Development Service shows how computer software can make government welfare work simply and honestly. By replacing confusing paper forms with a clean website, giving every student a permanent Student ID, and showing real course and seat numbers, the platform gives every young person in Karnataka a fair and easy chance to learn skills, get a job, and build a better future.")

    out_path = os.path.join(OUT_DIR, "03_Problem_Statement_and_Business.docx")
    doc.save(out_path)
    print(f"[SUCCESS] Saved simplified Report 3: {out_path}")

if __name__ == "__main__":
    generate_report_3_simplified()
