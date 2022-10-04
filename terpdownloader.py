import PyPDF2
import urllib
import urllib.request
import requests
from pathlib import Path
import fileinput
from PyPDF2 import PdfMerger

count = 0
for line in fileinput.input(files = "../coalist.txt"):
    url = line.strip()
    out = 'terps'
    response = requests.get(url)
    pdf = open(out+str(count)+'.pdf', 'wb')
    pdf.write(response.content)
    count = count + 1


pdf.close()
