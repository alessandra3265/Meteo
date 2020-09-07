import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import re
from robobrowser import RoboBrowser
from urllib import request
import csv
import sys

"""
Script per il sito del unipa regione Sicilia

primo parametro:    medie/estremi (1 per orari, 2 per giornalieri, 3 per mensili)
secondo parametro:  Intervallo temporale
terzo parametro:    Inizio
quarto parametro:   Fine

"""

url = "http://meteo.astropa.unipa.it/public/"
br = RoboBrowser(parser="html.parser")

def query (avgtype, timespan, day, month, year, dayend, monthend, yearend) :

    br.open(url)
    form = br.get_form() #prende il form dalla pagina web
    form['avgtype'] = avgtype #medie 
    form['timespan'] = timespan #intervallo di tempo
    form['day'] = day    
    form['month'] = month #mese inizio
    form['year'] = year
    form['dayend'] = dayend
    form['monthend'] = monthend #mese fine
    form['yearend'] = yearend
    br.submit_form(form) #esegue metodo post 

    soup = br.parsed       
    table = soup.select_one("table")
    headers = [th for th in table.select("tr")]    
    #Anno Mese Temperatura...
    row1 = [th.text for th in headers[0].select("th")]
     
     # row1 = row1[:index] + ['Temperatura'] + row1[index:]
    row1_len = len(row1)
    t_pos = row1_len - 7
    u_pos = row1_len - 6
    t = row1[row1_len - 7] #settimo a partire dalla fine
    u = row1[row1_len - 6]
    p = row1[row1_len - 5]
    v = row1[row1_len - 4]    

    row1.insert(t_pos, t)
    u_pos = len(row1) - 6
    row1.insert(u_pos, u)
    p_pos = len(row1) - 5
    row1.insert(p_pos, p)
    v_pos = len(row1) - 4
    row1.insert(v_pos, v)
        
    #/s /s Min Max...
    row2 = [th.text for th in headers[1].select("th")]
    
    for i in range(len(row2)):
        if not row2[i].strip():
            row2[i] = ""
    
    for i in range(len(row1)):
        row1[i] = row1[i] + ' ' + row2[i]

    #dati
    dati = [[td.text for td in row.find_all('td')] for row in table.select("tr + tr")] 
   # print(dati)


    #scrittura su file
    filename = "sicilia" + avgtype + timespan + day + month + year + dayend + monthend + yearend + ".csv" 
    with open(filename, "w") as f:
        wr = csv.writer(f)
        wr.writerow(row1)        
        wr.writerows(dati) 
    f.close
    return 

if __name__ == "__main__":  
    if (len(sys.argv) == 1):
        print('Inserire tipo media (1 per orari, 2 per giornalieri, 3 per mensili)')
        print('Inserire intervallo temporale (4 per a scelta)')
        print('Inserire un intervallo in formato giorno mese anno giornoFine meseFine annoFine')
        #query(str(1), str(4), str(1), str(1), str(2020), str(1), str(3), str(2020))
    elif (len(sys.argv) == 9):
        #avgtype, timespan, day, month, year, dayend, monthend, yearend
        annoInizio = int(sys.argv[5])
        annoFine = int(sys.argv[8])
        if (annoInizio < 2012 or annoInizio > 2020 or annoFine < 2012 or annoFine > 2020):
            print('inserisci gli anni compresi tra 2012 e 2020')
            exit()
        query(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
        
