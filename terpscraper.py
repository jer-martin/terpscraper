import requests
import fileinput
import re
from bs4 import BeautifulSoup

urlList = list()
list = list()




for URL in fileinput.input(files = 'outlinks.txt'):
        urlString = str(URL)
        urlList.append(urlString[0:-1])


#make this loop through the trulieve flower page

for URL in urlList:
    page = requests.get(URL)

    #this is the scraper that grabs the coa


    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="maincontent")

    coalink = results.find_all("div", class_="view-coa")
    for link in results.find_all('a',
            attrs={'href': re.compile("^https://www.trulieve.com/files")}):
    # display the actual urls
    #print(link.get('href'))
        thisurl = link.get('href')
        if thisurl in list:
            continue
        list.append(thisurl)

#print(coalink)
with open('coalist.txt','w') as coalist:
    coalist.write( '\n'.join( list ) )

print(list)
