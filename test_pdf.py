from utils.pdf_loader import extract_text_from_pdf

text = extract_text_from_pdf("documents/jee_marksheet.pdf")

print(text[:500])  # Print first 500 characters
