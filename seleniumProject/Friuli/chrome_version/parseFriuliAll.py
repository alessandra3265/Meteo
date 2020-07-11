from bs4 import BeautifulSoup
import csv

"""
#debug
file = open('output.txt', "r")
html = file.read()
file.close()
"""

def write_header(html):
    #print(html)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.select_one("table")
    #print(table)
    headers = [th for th in table.select("tr")]
        
    # mese, giorno, pioggia mm, ...
    row = [th.text.strip() for th in headers[0].select("th")]
    new_row = []
    for i in range(len(row)):
        row[i].strip().replace("\n", "")        
        new_row.append(" ".join(row[i].split()))
    new_row.append("Stazione")
    new_row.append("Anno")
    return new_row    

def write_dati(html,anno):
    
    soup = BeautifulSoup(html, 'html.parser')
    #nome della stazione
    div = soup.find('div', id = "dati")
    nome = div.find('b')
    nome = nome.text
    table = soup.select_one("table")      
    #dati 
    dati = [[td.text for td in row.find_all('td')] for row in table.select("tr")]     
    dati.pop(0)
    for a in range(0, len(dati)):
        for j in range(len(dati[a])):
            dati[a][j] = dati[a][j].strip().replace("\n", "")   
            dati[a][j] = " ".join(dati[a][j].split())        
            if (dati[a][j] == '-'):
                dati[a][j] = ''  
        dati[a].append(nome)  #aggiungo il nome della stazione
        dati[a].append(anno)
    return dati


def final_parsing(html_list,anno):
    if (len(html_list) == 0):
        print('nessun risultato')
        return
    header = write_header(html_list[0]) 
    dati = []
    for e in html_list:
        dati = dati + write_dati(e,anno)        
    
    #scrittura su file
    with open("friuliAll.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerow(header)        
        wr.writerows(dati) 
    f.close()