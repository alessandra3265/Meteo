from requests_html import HTMLSession
from bs4 import BeautifulSoup
import csv
import os 
"""
scrive in stazioniAM.csv l'elenco delle stazioni e le relative
province dell'Aeronautica Militare
"""
url = "http://www.meteoam.it/page/elenco-stazioni-totale"
with HTMLSession() as session: 

    r = session.get(url)
    r.html.render()
    table = r.html.find('table')
    rows = table[0].find('tr')

    data = []
    for row in rows:
        cols = row.find('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    data[0].insert(0, 'N')

path_src = os.path.dirname(os.path.realpath(__file__))        
path_result = os.path.join(path_src,"result")
filename = os.path.join(path_result, "stazioniAM.csv")
    
f = open(filename, "w")
wr = csv.writer(f)
wr.writerows(data)
f.close()
    