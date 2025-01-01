import fitz


def read_pdf(pdf_path):
    """
    Extracts text from a PDF file using PyMuPDF.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    try:
        # Open the PDF file
        document = fitz.open(pdf_path)

        text = ""
        # Iterate through all the pages
        for page_num in range(len(document)):
            page = document[page_num]
            # Extract text from the page
            text += page.get_text()
        document.close()
        return text
    except Exception as e:
        return f"An error occurred: {e}"

def read_pdf_with_pages(pdf_path):
    """
    Extracts text from a PDF file using PyMuPDF.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    try:
        # Open the PDF file
        document = fitz.open(pdf_path)

        text = ""
        # Iterate through all the pages
        for page_num in range(len(document)):
            page = document[page_num]
            # Extract text from the page
            text += f"<|PAGE_START_{page_num+1}|>"+page.get_text()+f"<|PAGE_END_{page_num+1}|>"
        document.close()
        return text
    except Exception as e:
        return f"An error occurred: {e}"