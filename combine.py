#!/usr/bin/env python3
import fitz  # PyMuPDF
import os
from pypdf import PdfWriter

# List all PDF files in the current directory and sort them by name
pdf_files = sorted([f for f in os.listdir('.') if f.endswith('compressed.pdf')])

# Create a new PDF document
combined_pdf = fitz.open()

# Iterate through each sorted PDF file
for pdf_file in pdf_files:
    # Open the current PDF file
    current_pdf = fitz.open(pdf_file)
    # Append each page to the combined PDF
    for page_num in range(current_pdf.page_count):
        combined_pdf.insert_pdf(current_pdf, from_page=page_num, to_page=page_num)

# create .output folder if it doesn't exist
if not os.path.exists('.output'):
    os.makedirs('.output')
# Save the combined PDF document
output_path = "./.output/combined.pdf"
combined_pdf.save(output_path)