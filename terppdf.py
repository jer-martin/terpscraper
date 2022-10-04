import PyPDF2
import glob
import os

filelist = glob.glob("*.pdf")

outfile = open("outpdf.txt", "w")
# creating a pdf file object
for file in filelist:
    size = os.path.getsize(file)
    if (size == 0): continue
    pdfFileObj = open(file, 'rb')

# creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
#print(pdfReader.numPages)

# creating a page object
    pageObj = pdfReader.getPage(0)

# extracting text from page
#print(pageObj.extractText())
    outfile.write(pageObj.extractText())

# closing the pdf file object
    pdfFileObj.close()
