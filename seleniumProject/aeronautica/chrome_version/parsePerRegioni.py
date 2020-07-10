from bs4 import BeautifulSoup
import csv
"""
html parsing per sito aeronautica quando specifico una stazione ma più anni 
(la possibilità di più parametri non è implementata)

scrive sul file:
AereoMultiData.csv
"""

    
#funzione per il parsing solo dei dati 
def parseDatiTable(table, citta, anno):    
    dati = [[td.text.strip() for td in row.find_all('td')] for row in table.select("tr + tr")]
    for j in range(len(dati)):
        dati[j].append(anno)
        dati[j].append(citta)        
    #print(dati)
    return dati

    
def htmlParse(html, rows):
    soup = BeautifulSoup(html, 'html.parser')
    sezione = soup.find('div', class_="col-sm-12 col-xs-12 col-md-9 col-lg-9")

    h4 = sezione.find_all('h4')
    titolo_table = h4[0].text   
    
    stazione = titolo_table.split('Risultati disponibilità bollettini per la stazione di ')[1]
    #print(stazione)

    #trovo tutte le tabelle
    tables = sezione.find_all('div', class_="table-responsive")
    if (tables == None):
        print(stazione + ' no dati')
        return

    
    #trovo tutti gli anni
    anni = []
    for i in range (1, len(h4)):
        anni.append(h4[i].text)    
    
    #dati delle tabelle    
    for i in range(len(tables)):
        dati = parseDatiTable(tables[i], stazione,anni[i])
        rows.append(dati)
    #print(rows)    
    
def finalParsing(htlm_list,filename):
    #costruisco intestazione
    row = ['Parametro', 'Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Nov', 'Dic', 'anno', 'Stazione']

    rows = []

    for e in htlm_list :
        htmlParse(e, rows)
    
    #scrittura su file csv 
    with open(filename, "w") as f:
        wr = csv.writer(f)
        wr.writerow(row)        
        for e in rows:
            wr.writerows(e)
    f.close




    