# pdf_report.py
from fpdf import FPDF
import io

def create_pdf(name, question, transcript, breakdown):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "VoiceHire AI - Interview Report", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.ln(5)
    pdf.cell(0, 10, f"Candidate: {name}", ln=True)
    pdf.cell(0, 10, f"Question: {question}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Transcript:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 6, transcript)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Analysis:", ln=True)

    pdf.set_font("Arial", size=11)
    for k,v in breakdown.items():
        pdf.cell(0, 8, f"{k}: {v}", ln=True)

    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer

