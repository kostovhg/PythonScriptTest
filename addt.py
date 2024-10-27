from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

def create_text_pdf(input_pdf, text):
    # Create a new PDF in memory
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    width, height = A4
    c.rotate(90)
    c.drawString(height - 50, 20, text)
    c.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)

    # Read the existing PDF
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()

    # Read the text PDF in memory
    text_reader = PdfReader(packet)

    # Merge the new text with the existing PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        if page_num == 0:
            page.merge_page(text_reader.pages[0])
        pdf_writer.add_page(page)

    # Save the new PDF
    with open('_' + input_pdf, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    input_pdf = 'OriginalPdf.pdf'  # path to the original PDF

    create_text_pdf(input_pdf, "2          J.24.021-02")