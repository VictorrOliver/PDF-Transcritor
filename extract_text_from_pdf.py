from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text


