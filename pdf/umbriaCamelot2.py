import camelot

url = "https://www.regione.umbria.it/documents/18/7110267/DATI+PIOGGIA+2020+.pdf/cad0f440-8ace-4646-a67d-9d6ef4cf4395"
tables = camelot.read_pdf(url, flavor='stream', strip_text='\n', pages='1-3')
print(tables)
csv_filepath = 'u2020.csv'
tables.export(csv_filepath, f='csv', compress=True) # export the list of tables
