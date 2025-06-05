import markdown
import pdfkit
import os

# Read the markdown file
with open('README.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Convert markdown to HTML
html_content = markdown.markdown(markdown_content)

# Add some basic styling
styled_html = f'''
<html>
<head>
<style>
body {{ font-family: Arial, sans-serif; margin: 40px; }}
h1 {{ color: #2c3e50; }}
h2 {{ color: #34495e; }}
code {{ background-color: #f7f9fa; padding: 2px 5px; border-radius: 3px; }}
pre {{ background-color: #f7f9fa; padding: 15px; border-radius: 5px; }}
</style>
</head>
<body>
{html_content}
</body>
</html>
'''

# Write the HTML file
with open('README.html', 'w', encoding='utf-8') as f:
    f.write(styled_html)

# Convert HTML to PDF using pdfkit
try:
    pdfkit.from_file('README.html', 'README.pdf')
except Exception as e:
    print(f"Error converting to PDF: {e}")
    print("Please install wkhtmltopdf from: https://wkhtmltopdf.org/downloads.html")
