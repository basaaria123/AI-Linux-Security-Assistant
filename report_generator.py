from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf_report(content, filename="security_report.pdf"):
    report_dir = "reports"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    filepath = os.path.join(report_dir, filename)
    c = canvas.Canvas(filepath, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, height - 72, "AI Linux Security Assistant - Report")
    
    c.setFont("Helvetica", 12)
    y = height - 100
    
    for line in content.split('\n'):
        if y < 72:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 72
        c.drawString(72, y, line)
        y -= 15
    
    c.save()
    return filepath
