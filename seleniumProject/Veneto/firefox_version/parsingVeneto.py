from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv
import os 

"""
script per il parsing della pagina dei
risultati dell'ARPA Veneto 
si occupa di scrivere il file csv 
"""


def parse(html, anno, parametro, provincia, rows): 
    html = html.replace('<th>&#160;</th>', '<td> </td>')
    
    soup = BeautifulSoup(html, "html.parser") 

    #trovo pannello con 3 tabelle
    div = soup.find('div', id = "meteostorico")
    tables = div.find_all('table')

    #trovo la stazione dalla prima tabella 
    table_h = tables[0]
    headers = table_h.find_all('tr')
    
    stazione = headers[0].select_one('b').text
    quota = headers[2].select_one('b').text
    comune_row = headers[5].select_one('b').text

    comune = comune_row.split(' (')[0]
    provincia_sigla = (comune_row.split('(')[1]).split(')')[0]

    #dati dalla seconda tabella o dalla quinta nel caso di temperatura media
    if (len(tables) > 3):
        table = tables[4]
    else:
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
        
        dati[j].append(stazione)
        dati[j].append(comune)
        dati[j].append(provincia_sigla)

    rows += dati    
    return
    
def final_parsing(html_list, anno,parametro,provincia, filename):
    headers = ['Giorno','GEN','FEB','MAR','APR','MAG','GIU','LUG','AGO','SET','OTT','NOV','DIC','anno','parametro','stazione','comune','provincia_sigla']
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
    
