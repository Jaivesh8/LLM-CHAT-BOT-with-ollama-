# utils/pdf_loader.py

import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using PyMuPDF.
    Args:
        pdf_path (str): Full path to the PDF file.
    Returns:
        str: The extracted text.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"No file found at: {pdf_path}")

    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()

    return text.strip()

