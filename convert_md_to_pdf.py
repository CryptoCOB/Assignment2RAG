"""
Helper script to convert markdown requirements to PDF for RAG system input.
Student: Marc Harty (300818959)
"""
import markdown
from weasyprint import HTML
from pathlib import Path

def convert_md_to_pdf():
    """Convert the requirements markdown to PDF."""
    md_file = Path("AI Systems Design (SEC. 403).md")
    output_pdf = Path("data/requirements_document.pdf")
    
    # Read markdown content (first 446 lines - NFR sections)
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()[:446]
        md_content = ''.join(lines)
    
    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    
    # Add CSS for better formatting
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
                font-weight: bold;
            }}
            h1, h2, h3 {{
                color: #333;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Convert HTML to PDF
    HTML(string=styled_html).write_pdf(output_pdf)
    print(f"✓ PDF created: {output_pdf}")
    print(f"  File size: {output_pdf.stat().st_size / 1024:.2f} KB")

if __name__ == "__main__":
    # Check if weasyprint is installed
    try:
        convert_md_to_pdf()
    except ImportError:
        print("ERROR: weasyprint not installed.")
        print("Install with: uv pip install markdown weasyprint")
