from bs4 import BeautifulSoup

f = open('aereoOut.txt', 'r')
html = f.read()
f.close()
#print(html)

def parseTable(table, citta):
    headers = [th for th in table.select("tr")]
    row = [th.text.strip() for th in headers[0].select("th")]
    row.remove('')
    row.insert(0, 'Parametro')
    row.append('Stazione')
    dati = [[td.text for td in row.find_all('td')] for row in table.select("tr + tr")]
    dati.append(citta)
    print(row)
    print(dati)
    return

soup = BeautifulSoup(html, 'html.parser')

sezione = soup.find('div', class_="col-sm-12 col-xs-12 col-md-9 col-lg-9")

h4 = sezione.find_all('h4')
print(len(h4))
table_count = 0
for i in range(len(h4)):
    if (i % 2 == 0): 
        print(i)
        text = h4[i].text
        print(text)
        result = h4[i+1]
        if (result.text == 'Non ci sono dati per il tipo di richiesta effettuata.'):
            print(result)
        else:
            stazione = text.split('Risultati disponibilità bollettini per la stazione di ')
            print(stazione[1])
            table = soup.find_all('div', class_="table-responsive")
            parseTable(table[table_count], stazione[1])
            table_count += 1




    