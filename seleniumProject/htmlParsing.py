from bs4 import BeautifulSoup
import csv

"""
#debug
file = open('output.txt', "r")
html = file.read()
file.close()
"""

def htmlParsing(html):
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
      
    #dati 
    dati = [[td.text for td in row.find_all('td')] for row in table.select("tr")] 
    

    for a in range(0, len(dati)):
        for j in range(len(dati[a])):
            dati[a][j] = dati[a][j].strip().replace("\n", "")   
            dati[a][j] = " ".join(dati[a][j].split())        
            if (dati[a][j] == '-'):
                dati[a][j] = ''
   
     

      
    #write a csv file
    with open("hmtlSel.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerow(new_row)        
        wr.writerows(dati) 
    f.close()
    return


#htmlParsing(html)
