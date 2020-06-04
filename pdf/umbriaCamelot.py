import camelot

path = ".\\DATI PIOGGIA 2019.pdf"
tables = camelot.read_pdf(path,pages='1', multiple_tables = True, flavor='stream', strip_text='\n')
print(tables)
print(tables[0].df)
tables[0].to_excel('umbria2019.xlsx')
#tables[0].to_csv('umbria2019.csv')




