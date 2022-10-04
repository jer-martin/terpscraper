import PyPDF2

outfile = open("outpdf.txt", "w")
# creating a pdf file object
pdfFileObj = open('28312_0002440840.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())
outfile.write(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
