import fitz # PyMuPDF

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extract raw text from a PDF provided as bytes.
    Returns a single string containing text from all pages.
    """

    document = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()
        text += "\n"

    document.close()

    return text
