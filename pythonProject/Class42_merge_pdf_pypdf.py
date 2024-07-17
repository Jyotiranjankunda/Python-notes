from pypdf import PdfWriter
import os

merger = PdfWriter()
folder = "files"
myfiles = os.listdir(folder)

for file in myfiles:
    if(file.endswith(".pdf")):
        path = os.path.join(folder, file)
        merger.append(path)

merger.write("files/merged-pdf.pdf")
merger.close()