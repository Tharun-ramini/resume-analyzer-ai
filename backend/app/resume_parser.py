import PyPDF2

def extract_text_from_pdf(pdf_file_path: str) -> str:
    """
    Extracts text from a PDF file using PyPDF2.
    """
    try:
        with open(pdf_file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        return text

    except Exception as e:
        return f"Error reading PDF: {str(e)}"



    

