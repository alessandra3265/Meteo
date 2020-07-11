from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv
"""
script che accetta html relativo a un anno e a una stazione
"""


def parse(html, anno,parametro,provincia, rows): 
     
    soup = BeautifulSoup(html, "html.parser")  
    #trovo pannello con 3 tabelle
    div = soup.find('div', id = "meteostorico")
    tables = div.find_all('table')

    #trovo la stazione dalla prima tabella 
    table = tables[0]
    headers = table.select_one('tr')
    stazione = headers.select_one('b').text

    #trovo i dati dalla seconda tabella
    table = tables[1]
    dati = [[td.text.strip() for td in row.find_all('td')] for row in table.select("tr + tr")] 
    for i in range(3):
        dati.pop(len(dati)-1)
    #tolgo i '>>'
    for i in range(len(dati)):
        for j in range(len(dati[i])):       
            if (dati[i][j] == '>>'):
                dati[i][j] = ''

   
        
    #uniformo tutte le righe affinchè siano lunghe uguali
    for i in range(len(dati)):
        if (len(dati[i]) < 14):
            while(len(dati[i]) != 13):
                dati[i].append('')
    
    #inserisco i giorni dell'anno
    for i in range(len(dati)):
        dati[i].insert(0,i+1)     
    
    #aggiungo il parametro e la stazione provincia a ogni riga
    for i in range(len(dati)):
        dati[i].append(anno)
        dati[i].append(parametro)
        dati[i].append(provincia)
        dati[i].append(stazione)
    
    rows += dati
    
    
def final_parsing(html_list, anno,parametro,provincia, filename):
    headers = ['Giorno','GEN','FEB','MAR','APR','MAG','GIU','LUG','AGO','SET','NOV','DIC','anno','parametro','provincia','stazione']
    rows = []
   
    for html in html_list:         
        try:
            parse(html,anno,parametro,provincia, rows)
        except AttributeError as e:
            print('errore')
            print(e)
        
    
    with open(filename, "w") as f:
            wr = csv.writer(f)
            wr.writerow(headers)        
            wr.writerows(rows) 
            f.close()
    

