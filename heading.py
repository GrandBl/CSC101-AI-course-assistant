import fitz  # PyMuPDF
import re

def find_headings(pdf_path):
    """
    Scan the PDF for text matching the pattern: digit(s).digit(s).
    For each match, print the heading text and its font size.
    """
    # Compile a regex for headings like "1.1", "2.10", etc.
    heading_pattern = re.compile(r"^(\d+)\.(\d+)(\s|$)")

    doc = fitz.open(pdf_path)

    for page_index, page in enumerate(doc, start=1):
        # Extract text blocks as a dictionary
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    if heading_pattern.match(text):
                        # Print the heading candidate and its font size
                        print(f"Page {page_index}: Found heading candidate '{text}' "
                              f"with font size {span['size']}")

if __name__ == "__main__":
    # Replace with the path to your PDF file
    pdf_path = r"" //enter your directory of file
    find_headings(pdf_path)
