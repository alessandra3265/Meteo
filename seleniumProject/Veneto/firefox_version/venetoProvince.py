from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from parsingVeneto import final_parsing
import sys
import os
from pathlib import Path

"""
script per interrogazione aggregata per province
eseguire    venetoProvince.py p                             per elenco parametri
eseguire    venetoProvince.py s param prov anno             per elenco parametri
eseguire    venetoProvince.py parametro Provincia anno      per i risultati di un solo anno 

eseguire    venetoProvince.py parametro Provincia anno_inizio anno_fine      
per i risultati da anno_inzio a anno_fine

"""

url_base = "https://www.arpa.veneto.it/bollettini/storico/"
p = Path(os.path.realpath(__file__))
parent = p.parent.parent.parent
driver_path = os.path.join(parent,"geckodriver")

path_src = os.path.dirname(os.path.realpath(__file__))
path_result = os.path.join(path_src, 'result')


optionsFire = Options()
optionsFire.add_argument('--headless')
#webdriver = webdriver.Firefox(executable_path=driver_path, options=optionsFire)

"""
nel html a ogni stazione è associato un numero 
resituisce un dizionario che associa il nome della pronvicia con
la lista di numero della stazione appartententi alle stazioni  
"""
def getDictProvince(parametro, provincia, anno):     
    url = "https://www.arpa.veneto.it/bollettini/storico/Mappa_" + anno + "_" +parametro + ".htm?t=RG"
    print(url)
    wdriver = webdriver.Firefox(executable_path=driver_path, options=optionsFire)
    with wdriver as driver:
        wait = WebDriverWait(driver, 20)        

        # retrive url in headless browser
        driver.get(url)

        #clicco su elenco stazioni
        driver.find_element_by_id("mnuTABELLA").click()
        wait.until(EC.visibility_of_element_located((By.ID, "divTabella")))
        
        #result    
        html = driver.page_source
        driver.close()        
        soup = BeautifulSoup(html, 'html.parser')
        
        tabellaHtml = soup.find('div', id="divTabella")
        table = tabellaHtml.select_one("table")
       
        headers = [th for th in table.select("tr")]
        
        #print(headers)
        regioni = []
        stazione = []
        dati = []
           
        for i in range(len(headers)):
            td = headers[i].find_all('a', href=True)
            if (len(td) != 0):
                for a in td:
                    a = a.get('href')
                    split = a.split('/')
                    res = split[1].split('_', 1)
                    dati.append(res[0])
                if (i == len(headers)-1):
                    stazione.append(dati)
            else:
                #non ci sono dati tra i <tr>
                regione = headers[i].select_one('th')
                list = ['nella provincia di ',' nell']
                if (regione != None):
                    regione = regione.text                
                    result = regione.split(list[0])
                    result = result[1].split(list[1])
                    regioni.append(result[0]) 
            
                #salvo i dati
                if (len(dati) != 0):
                    stazione.append(dati)
                    dati = []
               

        #costruisco il dizionario provincia - lista di codici 
        regioniDict = {}
        for i in range(len(regioni)):
            regioniDict[regioni[i]] = stazione[i]    
    return regioniDict

"""va sulla pagina web e scrive il file con i risultati"""
def getProvinciaResult(parametro, provincia,anno):
    regioniDict = getDictProvince(parametro, provincia, anno)
    stazioni_list = []
    filename = parametro + provincia + anno +'.csv'
    filename = os.path.join(path_result, filename)
    
    if (provincia == 'tutte'):
        provincia = ""
        valuesList = regioniDict.values()
        for codice_list in valuesList:
            for codice in codice_list:
                stazioni_list.append(codice)
        
    else:
        stazioni_list = regioniDict[provincia]
    html_list = []    
        
    #costruisco i link salvo html relativo
    session = HTMLSession()
    for e in stazioni_list:
        link = anno + '/' + e + '_' + anno + '_' + parametro + '.htm'
        link_result = url_base + link
        
        #surf to pagina dati           
        result = session.get(link_result)
        html_list.append(result.html.html)
        session.close()
        
        
    #parsing e scrittura su file    
    final_parsing(html_list, anno,parametro,provincia, filename)
    

"""resituisce elenco delle stazioni"""
def getStazioni(parametro, provincia, anno):
    regioniDict = getDictProvince(parametro,provincia,anno)
    print(regioniDict[provincia])

"""restituisce elenco parametri"""
def getParametri():
    parametri = ['TEMP', 'PREC', 'LIVIDRO', 'SUOLO', 'RADSOL', 'UMID','PORTATA','BFOGL','VVENTO','PRESS','LIVNEVE']
    print(parametri)

        
if __name__ == "__main__": 
    if(len(sys.argv) == 4):
        #param prov anno 
        getProvinciaResult(sys.argv[1],sys.argv[2],sys.argv[3])

    elif(len(sys.argv) == 5 and sys.argv[1] == 's'):
        #param prov anno s
        getStazioni(sys.argv[2],sys.argv[3],sys.argv[4])

    elif(len(sys.argv) == 2 and sys.argv[1] == 'p'):
        getParametri()
    
    elif (len(sys.argv) == 5):
        #param prov anno_inizio anno_fine
        param = sys.argv[1]
        prov = sys.argv[2]
        anno_list = []
        anno_inizio = int(sys.argv[3])
        anno_fine = int(sys.argv[4])
        for i in range (anno_inizio, anno_fine + 1):
            anno_list.append(str(i))
        for anno in anno_list:
            getProvinciaResult(param, prov, anno)
    else: 
        print('specifica parametro provincia anno')
        getProvinciaResult('TEMP', 'Padova', '2018')


       
       