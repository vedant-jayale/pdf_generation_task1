# pdf_generation_task1

This project automates the generation of personalized PDF report cards for students based on data from an Excel file. It reads student information, calculates total and average scores, and generates a formatted PDF report for each student. The report includes their name, total score, average score, and a subject-wise score table.

Approach:
Reading Data: I used the pandas library to read data from the provided Excel file (student_scores.xlsx). I also implemented error handling to manage missing or invalid data and ensured that the necessary columns (StudentID, Name, Subject, and SubjectScore) are present.

Processing Scores: After loading the data, I grouped it by StudentID and calculated each student’s total score and average score across subjects. This data is used to create a personalized report card for each student.

PDF Generation: Using the ReportLab library, I generated a PDF report card for each student. The PDF contains the following details:

Student Name
Total Score
Average Score
A table displaying subject-wise scores
Error Handling: The script includes checks to ensure that all required columns are present in the Excel file. It also handles any missing or invalid data gracefully.

Saving Reports: The generated report cards are saved as individual PDFs, named with the format report_card_<StudentID>.pdf, where <StudentID> is replaced with the student's unique identifier.

Libraries Used:
pandas: For reading, processing, and manipulating the Excel data.
ReportLab: For creating and formatting the PDF report cards.
