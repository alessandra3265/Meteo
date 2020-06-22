from requests_html import HTMLSession
from bs4 import BeautifulSoup

url_home = "https://www.arpa.veneto.it/bollettini/meteo60gg/"
urlParent = "https://www.arpa.veneto.it/bollettini/meteo60gg/Mappa_PREC.htm?t=RG"
url = "https://www.arpa.veneto.it/bollettini/meteo60gg/Staz_248.htm"

session = HTMLSession()

resP = session.get(urlParent)
resP.html.render()
soupP = BeautifulSoup(resP.html.html, "html.parser")

#trovo tutti i link alle pagine delle singole stazioni
list = soupP.find_all('area')

url_stazione1 = list[0]['href']
url_stazione1 = url_home + url_stazione1

res_stazione1 = session.get(url_stazione1)
res_stazione1.html.render()
soup = BeautifulSoup(res_stazione1.html.html, "html.parser")

table = soup.find("table", class_="plain")

headers = [th for th in table.select("tr")]
#data temp pioggia(mm)...
row1 = [th.text for th in headers[0].select("th")]
"""print(row1)"""
row2 = [th.text for th in headers[1].select("th")]
"""print(row2)"""
#dati
dati = [[td.text for td in row.find_all('td')] for row in table.select("tr + tr")] 
print(dati)


"""
res = session.get(url)

res.html.render()
soup = BeautifulSoup(res.html.html, "html.parser")
print(soup.text)
"""