import fileinput
outfile = open("outterp.txt", "w")



for line in fileinput.input("outpdf.txt"):
    if "Tru" in line or "Flower" in line or "Flowr" in line or "Ground" in line:
        outfile.write(line)
    if "0." in line and "%" in line:
        outfile.write(line)
