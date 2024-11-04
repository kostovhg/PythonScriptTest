# Done with Microsoft Copilot

import pandas as pd  # Import the pandas library for reading Excel files
from PyPDF2 import PdfWriter, PdfReader  # Import PdfWriter and PdfReader from PyPDF2 for handling PDF files
from reportlab.pdfgen import canvas  # Import the canvas module from reportlab for creating PDF overlays
import tkinter as tk
from tkinter import ttk
import io  # Import the io module for handling in-memory byte streams
import sys  # Import the sys module for system-specific parameters and functions
from pandastable import Table

# Function to create a PDF canvas with the specified text
def create_annotation_canvas(text, x):
    packet = io.BytesIO()  # Create an in-memory byte stream
    can = canvas.Canvas(packet)  # Create a canvas object to draw on
    can.setPageSize((x, 200))  # Set the page size with width `x` and height 200
    can.setFont('Helvetica-BoldOblique', 18)  # Set the font and size
    can.drawString(x - 180, 160, text)  # Draw the string `text` at the specified position
    can.save()  # Save the canvas to the byte stream
    packet.seek(0)  # Move to the beginning of the byte stream
    return packet  # Return the byte stream

# Function to merge the annotation canvas with an existing PDF page
# The function takes a `page` object and a `packet` object as input
# and returns the modified `page` object
def merge_annotation(page, packet):
    new_pdf = PdfReader(packet)  # Read the byte stream as a PDF
    overlay_page = new_pdf.pages[0]  # Get the first page of the new PDF
    page.merge_page(overlay_page)  # Merge the new page with the existing page
    return page  # Return the merged page

# Function to save the modified PDF to a new file
def save_pdf(reader, output_pdf):
    writer = PdfWriter()  # Create a PDF writer object
    for page in reader.pages:  # Loop through all pages in the reader
        writer.add_page(page)  # Add each page to the writer
    with open(output_pdf, 'wb') as output_file:  # Open the output file in write-binary mode
        writer.write(output_file)  # Write the modified PDF to the output file

# Function to add an annotation to a specified PDF file
def add_annotation(pdf_path, text, page_number=0):
    with open(pdf_path, 'rb') as f:  # Open the PDF file in read-binary mode
        reader = PdfReader(f)  # Read the PDF file
        page = reader.pages[page_number]  # Get the specified page
        x = int(page.mediabox.upper_right[0])  # Get the width of the page
        packet = create_annotation_canvas(text, x)  # Create the annotation canvas
        page = merge_annotation(page, packet)  # Merge the annotation with the page
        output_pdf = pdf_path.replace('.pdf', '_a.pdf')  # Define the output PDF file name
        save_pdf(reader, output_pdf)  # Save the modified PDF
        print(f"Annotation added to {output_pdf}")  # Print a success message

# Function to modify PDFs based on an Excel file
def modify_pdfs_from_excel(excel_path, text):
    df = pd.read_excel(excel_path)  # Read the specified columns from the Excel file
    for index, row in df.iterrows():  # Loop through each row in the DataFrame
        filename = '%0*d' % (6, row[0]) + '.pdf'  # Format the filename based on the 'count' column
        ann = f"{row[1]}       {text}"  # Create the annotation text 
        print(f"Adding annotation: {ann} to {filename}")
        add_annotation(filename, ann)  # Add the annotation to the PDF file

def read_excel(excel_path):
    df = pd.read_excel(excel_path, usecols=[0, 1, 2])
    df['PART NUMBER'] = df['PART NUMBER'].apply(lambda x: f"{x:06}")
    return df

def display_table(data):
    root = tk.Tk()
    root.title("PDF Files list")

    f = tk.Frame(root)
    f.pack(fill='both', expand=1)

    pt = Table(f, dataframe=data, width=200, maxcellwidth=1500)
    pt.adjustColumnWidths(limit=30)
    pt.show()

    # tree = ttk.Treeview(root)
    # tree['columns'] = list(data.columns)
    # tree['show'] = "headings"

    # for column in data.columns:
    #     tree.heading(column, text=column)
    #     tree.column(column, width=150)

    
    # for index, row in data.iterrows():
    #     tree.insert('','end', values=list(row))

    # tree.pack(expand=True, fill='both')
    root.mainloop()

if __name__ == "__main__":  # If the script is executed directly
    excel_path = "./08_Milling_OT.xlsx"  # Define the path to the Excel file
    text = "J.24.021-02"
    display_table(read_excel(excel_path))
    #modify_pdfs_from_excel(excel_path, text)  # Call the function to modify PDFs based on the Excel file


