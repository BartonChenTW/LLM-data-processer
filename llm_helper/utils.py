

def read_pdf2text(pdf_path: str) -> str:
    """
    Read a PDF file and extract its text content.
    This function opens a PDF file using pdfplumber and extracts all text content
    from each page sequentially, concatenating them with newline separators.
    Args:
        pdf_path (str): The file path to the PDF document to be read.
    Returns:
        str: A string containing all extracted text from the PDF, with each page's
             content separated by a newline character.
    Raises:
        FileNotFoundError: If the specified PDF file does not exist.
        pdfplumber.exceptions.PDFSyntaxError: If the PDF file is corrupted or invalid.
    Example:
        >>> text = read_pdf2text("/path/to/document.pdf")
        >>> print(text[:100])  # Print first 100 characters
    """
    """Read a PDF file and extract its text content."""
    import pdfplumber

    pdf_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            pdf_text += page.extract_text() + "\n"

    return pdf_text