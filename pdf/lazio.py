import camelot

path = "http://www.idrografico.regione.lazio.it/Documenti/Bollettini/Bollettini%20Idrologici/Anno%202004/12%20-%20Dicembre.pdf"
tables = camelot.read_pdf(path,pages='1', multiple_tables = False, flavor='stream', strip_text='\n')

print(tables[0].df)