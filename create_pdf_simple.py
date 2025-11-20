"""
Helper script to extract NFR sections and save as text-based PDF sized to yield ~12 chunks
with chunk_size=1000 and chunk_overlap=100 (≈ 10,900 characters of text).
Student: Marc Harty (300818959)
"""
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

TARGET_CHARS = 10900  # ≈ 12 chunks for 1000/100 splitter


def create_requirements_pdf():
    """Create PDF from the NFR sections of the markdown file sized for ~12 chunks."""
    md_file = Path("AI Systems Design (SEC. 403).md")
    output_pdf = Path("data/requirements_document.pdf")

    # Read progressively until we reach TARGET_CHARS (fallback to full file if shorter)
    with open(md_file, "r", encoding="utf-8") as f:
        all_lines = f.readlines()

    selected_lines = []
    char_count = 0
    for line in all_lines:
        selected_lines.append(line)
        char_count += len(line)
        if char_count >= TARGET_CHARS:
            break

    # Create PDF
    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )

    elements = []
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Body", leading=14))

    for line in selected_lines:
        text = line.strip()
        if text:
            elements.append(Paragraph(text, styles["Body"]))
            elements.append(Spacer(1, 0.12 * inch))

    # Build PDF
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc.build(elements)
    print(f"✓ PDF created: {output_pdf}")
    print(f"  File size: {output_pdf.stat().st_size / 1024:.2f} KB")
    print(f"  Lines included: {len(selected_lines)} | Characters: {char_count}")


if __name__ == "__main__":
    try:
        create_requirements_pdf()
    except ImportError:
        print("ERROR: reportlab not installed.")
        print("Install with: uv pip install reportlab")
