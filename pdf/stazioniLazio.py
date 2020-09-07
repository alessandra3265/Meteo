import requests
import csv 
import os
import json 

"""
scrive in un file csv il nome della stazione meteoreologica, comune, provincia, regione, indirizzo, cap, quota, coordinate 
tramite API presente al link
http://dati.lazio.it/catalog/api/action/datastore_search?resource_id=c556a2a6-930e-4b7a-b5e6-e1e05a8657b6
"""


url_base = "http://dati.lazio.it/catalog"
url = "http://dati.lazio.it/catalog/it/dataset/rete-di-stazioni-di-monitoraggio-idro-termo-pluviometrica/resource/c556a2a6-930e-4b7a-b5e6-e1e05a8657b6"
url2 = "http://dati.lazio.it/catalog/api/action/preview"
link = "http://dati.lazio.it/catalog/api/action/datastore_search?resource_id=c556a2a6-930e-4b7a-b5e6-e1e05a8657b6"
all_values = []
table_head = []
while True:
    response = requests.get(link)
    data = response.json()
    results = data["result"]     
    record = results["records"] #list of dicts
    if not record:
        break     #end of the data
    values = [[value for value in dict_rec.values()] for dict_rec in record]
    all_values += values
    if not table_head: #ceck if list is empy, fill table_head only first time
        table_head = [key for key in record[0]] #comune, indirizzo, provincia, ...
    links = results["_links"]
    link = url_base + links['next']
response.close()
#print(table_head)
#print(all_values)

#scrittura su file
path_src = os.path.dirname(os.path.realpath(__file__)) #path del file sorgente
filename = "stazioniLazio.csv" 
path_result = os.path.join(path_src,filename)
with open(path_result, "w") as f:
    wr = csv.writer(f, delimiter =";", escapechar = '\n', quoting = csv.QUOTE_MINIMAL)  
    wr.writerow(table_head)             
    wr.writerows(all_values) 
f.close

"""
usare la ',' come delimiter causa dei problemi in fase
 di lettura del csv delimitato da ',' 
in quanto c'è un indirizzo che presenta al suo interno una virgola 
che verebbe letto come due campi invece di uno
"""