import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

def read_data(file_path):
    try:
        df = pd.read_excel(file_path)
        if 'StudentID' not in df.columns or 'Name' not in df.columns or 'Subject' not in df.columns or 'SubjectScore' not in df.columns:
            raise ValueError("Required columns missing in the Excel file.")
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None

def process_and_generate_reports(df):

    grouped = df.groupby('StudentID')

    for student_id, group in grouped:
        student_name = group['Name'].iloc[0]
        total_score = group['SubjectScore'].sum()
        average_score = group['SubjectScore'].mean()

        create_pdf(student_id, student_name, total_score, average_score, group)

def create_pdf(student_id, student_name, total_score, average_score, group):
    file_name = f"report_card_{student_id}.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)

    c.setFont("Helvetica", 14)
    c.drawString(30, 750, f"Student Name: {student_name}")
    
    c.setFont("Helvetica", 12)
    c.drawString(30, 730, f"Total Score: {total_score}")
    c.drawString(30, 710, f"Average Score: {average_score:.2f}")

    data = [['Subject', 'Score']]  
    for index, row in group.iterrows():
        data.append([row['Subject'], row['SubjectScore']])  

    table = Table(data, colWidths=[200, 100])

    table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)), 
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  
        ('BACKGROUND', (0, 0), (-1, 0), (0.7, 0.7, 0.7)),  
        ('GRID', (0, 0), (-1, -1), 0.5, (0, 0, 0)),  
    ]))

    table.wrapOn(c, 30, 500)  
    table.drawOn(c, 30, 450)  

    # Save the PDF
    c.save()
    
def main():
    file_path = 'student_scores.xlsx'  
    df = read_data(file_path)
    
    if df is not None:
        process_and_generate_reports(df)

if __name__ == "__main__":
    main()
