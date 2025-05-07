import pdfplumber //install pdfplumber
import re

def extract_pdf_headings_to_text(pdf_path, txt_path, heading_size_threshold=13):
    """
    Extracts text from a PDF file, inserts a blank line whenever a line has a 
    font size >= `heading_size_threshold`, and uses a regex to separate numbered
    section labels from immediately adjacent text (e.g. '1.1Programming' -> '1.1 Programming').
    """
    # A small vertical tolerance to decide if characters belong on the same line
    VERTICAL_TOLERANCE = 3
    
    # Regex pattern to capture sequences like 1.1 or 1.2.3 (etc.) 
    # which are directly followed by non-whitespace characters
    pattern = r'(\d+(?:\.\d+)+)(?=[^\s])'

    with pdfplumber.open(pdf_path) as pdf, open(txt_path, "w", encoding="utf-8") as out_file:
        for page in pdf.pages:
            chars = page.chars

            # Sort characters top-to-bottom, then left-to-right 
            # (pdfplumber's default sort might suffice, but let's be explicit)
            chars.sort(key=lambda c: (round(c["top"]), c["x0"]))

            # We'll group characters into lines by comparing their 'top' coordinate
            lines = []
            current_line = []
            if not chars:
                continue  # skip pages that have no characters

            # Initialize line grouping
            current_top = chars[0]["top"]

            for c in chars:
                # If this character is on a "different enough" line from the current line
                if abs(c["top"] - current_top) > VERTICAL_TOLERANCE:
                    # We reached a new line, so store the old line and reset
                    lines.append(current_line)
                    current_line = [c]
                    current_top = c["top"]
                else:
                    # Belongs to current line
                    current_line.append(c)

            # Don't forget the last line
            if current_line:
                lines.append(current_line)

            # Now, for each line, check if the font size meets or exceeds the threshold
            for line in lines:
                max_font_size = max(float(char["size"]) for char in line)
                
                # Sort left-to-right for printing the actual text
                line.sort(key=lambda x: x["x0"])
                line_text = "".join(char["text"] for char in line)

                # POST-PROCESSING: fix "1.1Programming" -> "1.1 Programming"
                line_text = re.sub(pattern, r'\1 ', line_text)

                # If the line meets the heading size threshold, prepend a blank line
                if max_font_size >= heading_size_threshold:
                    out_file.write("\n\n" + line_text + "\n")
                else:
                    out_file.write(line_text + "\n")


if __name__ == "__main__":
    pdf_file = r""  # Replace with your PDF file path
    text_file = r"" # Replace with your output text file path
    
    extract_pdf_headings_to_text(pdf_file, text_file, heading_size_threshold=13)
