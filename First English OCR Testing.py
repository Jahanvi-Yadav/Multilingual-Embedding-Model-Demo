!pip install pymupdf
from google.colab import files
uploaded = files.upload()
import fitz  # PyMuPDF

# Replace with your uploaded file name
pdf_path = "trimantra.pdf"  #"YOUR_FILE_NAME.pdf"

doc = fitz.open(pdf_path)

for page_num in range(3):  # First 3 pages only
    page = doc[page_num]
    text = page.get_text()
    print(f"\n--- Page {page_num+1} ---\n")
    print(text)
#total num of pages
import fitz

pdf_path = "trimantra.pdf"
doc = fitz.open(pdf_path)

print("Total Pages:", len(doc))
