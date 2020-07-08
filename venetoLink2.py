from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re
import csv

url_base = "https://www.arpa.veneto.it/bollettini/storico/"
url = "https://www.arpa.veneto.it/bollettini/storico/Mappa_2020_PREC.htm?t=RG"
session = HTMLSession()

resP = session.get(url)
resP.html.render()
soupP = BeautifulSoup(resP.html.html, "html.parser")
link_res = []

for link in soupP.find_all('a', href=re.compile("^\\d")): #Tutti i link che iniziano con un numero 
    link_res.append( link.get('href'))
    



link1 = link_res[2]

link_result = url_base + link1

result = session.get(link_result)

soup = BeautifulSoup(result.html.html, "html.parser")
#print(soup.prettify)


table = soup.select_one("table")

headers = [th for th in table.select("tr")]
row1 = [th.text for th in headers[0].select("th")]
row1 = row1[:13]

#dati
dati = [[td.text.strip() for td in row.find_all('td')] for row in table.select("tr + tr")] 

for i in range(5):
    dati.pop(0)


for i in range(4):
    dati.pop(len(dati)-1)


for i in range(len(dati)):
    for j in range(len(dati[i])):       
        if (dati[i][j] == '>>'):
            dati[i][j] = ''

for i in range(31):
    dati[i].insert(0,i+1)
    
    
#scrittura su file
filename = "venetoLink2.csv"
with open(filename, "w") as f:
    wr = csv.writer(f)
    wr.writerow(row1)        
    wr.writerows(dati) 
f.close

print(filename)