from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv
import os 

"""
script che accetta html relativo a un anno e a una stazione
"""


def parse(html, anno, parametro, provincia, rows): 
    html = html.replace('<th>&#160;</th>', '<td> </td>')
    
    soup = BeautifulSoup(html, "html.parser") 

    #trovo pannello con 3 tabelle
    div = soup.find('div', id = "meteostorico")
    tables = div.find_all('table')

    #trovo la stazione dalla prima tabella 
    table = tables[0]
    headers = table.select_one('tr')
    stazione = headers.select_one('b').text

    #dati dalla seconda tabella 
    table = tables[1]
    dati = [[td.text.strip() for td in row.find_all('td')] for row in table.select("tr")]

    for lista in dati:
        if (len(lista) < 12):
            dati.remove(lista)

    for lines in dati:
        for a in range(0, len(lines)):
            if (lines[a] == '>>'):
                lines[a] = '0'

    #estraggo l'intestazione head
    headers = [tr for tr in table.select("tr")]
    #head = [th.text for th in headers[0].find_all('th')]

    #estrae la prima colonna 
    first_col = []
    for i in range (1, len(headers)):
        day = headers[i].find('th')
        if (day != None):
            first_col.append(day.text)

    #mette il giorno a fianco i dati
    for j in range(0, len(first_col)):
        dati[j].insert(0, first_col[j])
        dati[j].append(anno)
        dati[j].append(parametro)
        dati[j].append(provincia)
        dati[j].append(stazione)

    rows += dati    
    return
    
def final_parsing(html_list, anno,parametro,provincia, filename):
    headers = ['Giorno','GEN','FEB','MAR','APR','MAG','GIU','LUG','AGO','SET','NOV','OTT','DIC','anno','parametro','provincia','stazione']
    rows = []
   
    for html in html_list:         
        try:
            parse(html,anno,parametro,provincia, rows)
        except AttributeError as e:
            print('errore')
            print(e)

    
    
    with open (filename, "w") as f:
            wr = csv.writer(f)
            wr.writerow(headers)        
            wr.writerows(rows) 
            f.close()
    
