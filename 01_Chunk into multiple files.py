import fitz  # PyMuPDF
import os
import re

def sanitize_filename(name):
    """
    Replace characters not allowed in Windows file names with '_'.
    """
    return re.sub(r'[\\/*?:"<>|]', '_', name)

def extract_sections_by_font_threshold(pdf_path, output_dir, size_threshold=13.0):
    heading_pattern = re.compile(r"^(\d+)\.(\d+)(\s|$)")
    doc = fitz.open(pdf_path)

    sections = {}
    current_section_key = None
    current_section_text = []

    for page_index, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                line_text = ""
                heading_candidate = None
                heading_font = 0.0

                for span in line.get("spans", []):
                    text = span["text"].strip()
                    if not text:
                        continue

                    line_text += text + " "

                    # Check if this span's text matches "chapter.section" and meets font threshold.
                    if heading_pattern.match(text) and span["size"] >= size_threshold:
                        heading_candidate = text
                        heading_font = span["size"]

                line_text = line_text.strip()

                # If we found a heading in this line, start a new section.
                if heading_candidate:
                    # Save the previous section first.
                    if current_section_key and current_section_text:
                        sections[current_section_key] = "\n".join(current_section_text).strip()

                    # Begin a new section with the heading as the key.
                    current_section_key = heading_candidate
                    current_section_text = [
                        f"Section heading: {heading_candidate} "
                    ]
                else:
                    # If we're inside a section, accumulate the line text.
                    if current_section_key is not None:
                        current_section_text.append(line_text)

    # Store the last section if any
    if current_section_key and current_section_text:
        sections[current_section_key] = "\n".join(current_section_text).strip()

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write each section to its own text file, sanitizing the filename
    for heading_key, content in sections.items():
        # Replace invalid characters in the heading
        safe_heading_key = sanitize_filename(heading_key)
        file_name = f"{safe_heading_key}.txt"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    return sections

if __name__ == "__main__":
    pdf_path = r"" //enter your pdf file path
    output_dir = r"C" // enter your output path

    sections_extracted = extract_sections_by_font_threshold(pdf_path, output_dir, size_threshold=13.0)
    print("Extraction complete. Sections found:")
    for k in sections_extracted:
        print("  -", k)
