import fileinput
import glob
import os

pdflist = glob.glob("*.pdf")
outfile = open("outterp.txt", "w", encoding="utf-8")



for line in fileinput.input("outpdf.txt", encoding="utf-8"):
    if "Trulieve" in line or "Total" in line or "Plants" in line or "plant" in line or "Matrix" in line:
        continue
    if "Tru" in line or "Flower" in line or "Flowr" in line or "Ground" in line:
        outfile.write('\n')
        outfile.write(line)
        outfile.write('\n')
    if "%" in line and "." in line:
        outfile.write(line)


for file in pdflist:
    os.remove(file)

os.remove('coalist.txt')
os.remove('outlinks.txt')
os.remove('outpdf.txt')
