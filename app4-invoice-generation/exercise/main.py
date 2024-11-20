import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("text_files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()

    filename = Path(filepath).stem
    title = str(filename).title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=title, ln=1)

pdf.output(f"PDFs/output.pdf")