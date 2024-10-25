import pandas as pd
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
import io

def create_annotation_canvas(text, x):
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    can.setPageSize((x, 200))
    can.setFont('Helvetica-BoldOblique', 18)
    can.drawString(x - 180, 160, text)
    can.save()
    packet.seek(0)
    return packet

def merge_annotation(page, packet):
    new_pdf = PdfReader(packet)
    overlay_page = new_pdf.pages[0]
    page.merge_page(overlay_page)
    return page

def save_pdf(reader, output_pdf):
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

def add_annotation(pdf_path, text, page_number=0):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        page = reader.pages[page_number]
        x = int(page.mediabox.upper_right[0])
        packet = create_annotation_canvas(text, x)
        page = merge_annotation(page, packet)
        output_pdf = pdf_path.replace('.pdf', '_a.pdf')
        save_pdf(reader, output_pdf)
        print(f"Annotation added to {output_pdf}")

def modify_pdfs_from_excel(excel_path):
    df = pd.read_excel(excel_path, usecols=[0, 1, 2])
    for index, row in df.iterrows():
        filename = '%0*d' % (6, row['No']) + '.pdf'
        text = f"{row['Count']}       {row['Module']}"
        add_annotation(filename, text)

if __name__ == "__main__":
    excel_path = "./naming.xlsx"
    modify_pdfs_from_excel(excel_path)
