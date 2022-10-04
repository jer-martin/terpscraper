import fileinput

linelist = list()
midlist = list()
outlist = list()
outfile = open("outlinks.txt", "a")

for line in fileinput.input(files = 'links.txt'):
    if "product-item-link" not in line:
         continue
    linelist.extend(line.split('"'))

#linelist = line.split('"')

for line2 in linelist:
    if "shop.trulieve.com/" not in line2:
         continue
    outlist.append(line2)
    outfile.write(line2)
    outfile.write("\n")


print(*outlist, sep = "\n")
