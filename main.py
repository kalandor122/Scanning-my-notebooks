import sys
import os
from PyPDF2 import PdfMerger

if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    raise ValueError("No argument provided.")

base_path = r""

folder_paths = {
    "1": r"",
    "2": r"",
    "3": r"",
    "4": r"",
    "5": r"",
    "6": r"",
    "7": r""
}


merger = PdfMerger()

# Get the target PDF path
if arg not in folder_paths:
    raise ValueError(f"No PDF mapped for argument {arg}")
target_pdf = folder_paths[arg]

# Get all PDF files in base_path
pdf_files = [os.path.join(base_path, f) for f in os.listdir(base_path) if f.lower().endswith('.pdf')]
if not pdf_files:
    print("No PDFs found in base_path.")
    sys.exit(0)

# Add existing target PDF first (if exists and is not empty)
if os.path.exists(target_pdf):
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(target_pdf)
        if len(reader.pages) > 0:
            merger.append(target_pdf)
    except Exception as e:
        print(f"Warning: Could not append target PDF ({target_pdf}): {e}")

# Add all PDFs from base_path
for pdf in pdf_files:
    merger.append(pdf)

# Write merged PDF
merger.write(target_pdf)
merger.close()

# Delete merged PDFs from base_path
for pdf in pdf_files:
    os.remove(pdf)

print(f"Merged {len(pdf_files)} PDFs into {target_pdf} and cleaned base_path.")

