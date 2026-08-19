import pymupdf


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from all pages of a PDF resume.
    """
    try:
        document = pymupdf.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text.strip()

    except Exception as e:
        raise RuntimeError(f"Failed to read PDF: {e}")


if __name__ == "__main__":
    pdf_path = "resumes/test_resume.pdf"

    text = extract_text_from_pdf(pdf_path)

    print("========== RESUME TEXT ==========")
    print(text)
