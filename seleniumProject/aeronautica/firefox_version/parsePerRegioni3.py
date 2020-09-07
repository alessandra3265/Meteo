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
    tables = sezione.find_all('div', class_="table-responsive")
    if (tables == None):
        print(' no dati')
        return

    tagList = sezione.find_all(['h4','table'])
    
    idx = 0
    while (idx < len(tagList) - 1):
        first_item = tagList[idx] #h4 stazione
        second_item = tagList[idx + 1] #h4 anno 
        if (idx + 2 < len(tagList)):
            third_item = tagList[idx + 2] #table

        if 'Non ci sono' in second_item.text:
            idx += 2
            continue
        elif (third_item.name == 'table'):
            if (first_item.name == 'h4'): #nuova stazione
                stazione = first_item.text.split('Risultati disponibilità bollettini per la stazione di ')[1]
            #anno
                anno = second_item.text 
                dati = parseDatiTable(third_item, stazione, anno)
                rows.append(dati)
                idx += 3
        else:
            anno = first_item.text 
            dati = parseDatiTable(second_item, stazione, anno)
            rows.append(dati)
            idx += 2
        
    
def finalParsing(htlm_list,filename):
    #costruisco intestazione
    row = ['Parametro', 'Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic', 'anno', 'Stazione']

    rows = []

    for e in htlm_list :
        htmlParse(e, rows)
    
    
    #scrittura su file csv 
    with open(filename, "w") as f:
        wr = csv.writer(f)
        wr.writerow(row)        
        for e in rows:
            if e:
                wr.writerows(e)
    f.close()
    
if __name__ == "__main__": 
    
    f = open('C:\\Users\\Alessandra\\Documents\\meteo\\Meteo\\cityListhtml.txt', "r")
    html = f.read()    
    f.close()
    html_list = []
    html_list.append(html)
    finalParsing(html_list, "Precipitazioni.csv")


    