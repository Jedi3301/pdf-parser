import fitz # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from each page of a PDF document.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        list: A list of strings, where each string is the text from a page.
    """
    document = fitz.open(pdf_path)
    text_per_page = []
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text_per_page.append(page.get_text())
    return text_per_page

if __name__ == "__main__":
    # This is a placeholder for your PDF file.
    # You will need to replace 'path/to/your/bill.pdf' with the actual path to your bill PDF.
    # For testing, you can use a sample PDF in your Bills_Data directory.
    pdf_file_path = "c:\\Users\\DARA JEDIDIAH\\Downloads\\Bills_Data\\Bills_Data\\sample.pdf" # Placeholder path
    
    # You need to ensure a sample.pdf exists in the specified path for testing.
    # If not, create one or update the path.

    extracted_text = extract_text_from_pdf(pdf_file_path)

    for i, text in enumerate(extracted_text):
        print(f"--- Page {i + 1} ---")
        print(text)
        print("\n" + "="*50 + "\n")