import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import re
from robobrowser import RoboBrowser
from urllib import request
import csv

url = "http://meteo.astropa.unipa.it/public/"
br = RoboBrowser(parser="html.parser")

def query (avgtype, timespan, day, month, year, dayend, monthend, yearend, filename) :

    br.open(url)
    form = br.get_form()

    form['avgtype'] = avgtype #medie 
    form['timespan'] = timespan #intervallo di tempo
    form['day'] = day    
    form['month'] = month #mese inizio
    form['year'] = year
    form['dayend'] = dayend
    form['monthend'] = monthend #mese fine
    form['yearend'] = yearend

    br.submit_form(form)

    soup = br.parsed
    table = soup.select_one("table")

    headers = [th for th in table.select("tr")]
    #print(headers[0].text)
    #print(headers[1].text)
    
    #Anno Mese Temperatura...
    row1 = [th.text for th in headers[0].select("th")]
    
   # row1 = row1[:index] + ['Temperatura'] + row1[index:]
    t = row1[2]
    u = row1[3]
    p = row1[4]
    v = row1[5]
    row1.insert(3, t)
    row1.insert(5, u)
    row1.insert(7, p)
    row1.insert(9, v)
    
    #/s /s Min Max...
    row2 = [th.text for th in headers[1].select("th")]

    for i in range(len(row2)):
        if not row2[i].strip():
            row2[i] = ""

    for i in range(len(row1)):
        row1[i] = row1[i] + ' ' + row2[i]

    #print(row1)
        
    #dati
    dati = [[td.text for td in row.find_all('td')] for row in table.select("tr + tr")] 
    #print(dati])

    #scrittura su file
    with open(filename, "w") as f:
        wr = csv.writer(f)
        wr.writerow(row1)        
        wr.writerows(dati) 
    f.close
    return 
