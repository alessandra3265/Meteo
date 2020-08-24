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
script per l'interrogazione relativa a una singola stazione, in un anno, per un dato parametro

eseguire     py venetoStazione.py p                         per avere l'elenco dei parametri disponibili
eseguire     py venetoStazione.py s parametro anno          per avere elenco delle stazioni 
eseguire     py venetoStazione.py parametro stazione anno   per avere i dati relativi 

lo script scrive un file NomeStazione.csv con i risultati 
"""

url_base = "https://www.arpa.veneto.it/bollettini/storico/"
p = Path(os.path.realpath(__file__))
parent = p.parent.parent.parent
driver_path = os.path.join(parent,"geckodriver")

optionsFire = Options()
optionsFire.add_argument('--headless')
#webdriver = webdriver.Firefox(executable_path=driver_path, options=optionsFire)

""" 
nel html a ogni stazione è associato un numero 
costruisce un dizionario che associa il nome di
ogni stazione con il numero 
"""
def getDictonaryStation(parametro,city, anno):     
    url = "https://www.arpa.veneto.it/bollettini/storico/Mappa_" + anno + "_" + parametro + ".htm?t=RG"
    #print(url)
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
        driver.quit() #calls driver.dispose and ends the session       
        soup = BeautifulSoup(html, 'html.parser')
        
        tabellaHtml = soup.find('div', id="divTabella")
        table = tabellaHtml.select_one("table")
       
        links = table.find_all('a', href=True)

        #costruisco un dizionario stazione - numero stazione
        stazioniDict = {}
        for e in links:
            name = e.text.split(' (')
            name = name[0]
            link = e.get('href')
            link = link.split('/')
            res = link[1].split('_', 1)
            link = res[0]
            stazioniDict[name] = link
    return stazioniDict


""" 
effettua l'interrogazione sulla pagina web 
"""
def getStationResult(parametro, city, anno):
    stazioniDict = getDictonaryStation(parametro, city,anno)

    #prendo il codice relativo alla città
    codice = stazioniDict[city]        
    link = anno + '/' + codice + '_' + anno + '_' + parametro + '.htm'
    link_result = url_base + link
    #print(link_result)
    #surf to pagina dati
    session = HTMLSession()
    result = session.get(link_result)
    html= result.html.html
    html_list = []
    html_list.append(html)
    session.close()
    
    #parsing e scrittura su file
    filename = city + anno + '.csv'
    final_parsing(html_list, anno,parametro,'', filename)

"""  
restituisce i parametri possibili
"""
def getParametri():
    parametri = ['TEMP', 'PREC', 'LIVIDRO', 'SUOLO', 'RADSOL', 'UMID','PORTATA','BFOGL','VENTO','PRESS','LIVNEVE']
    print(parametri)

"""
restituisce le stazioni disponibili in un dato per un dato parametro  
"""
def getStazioni(parametro, anno):
    stazioni = getDictonaryStation(parametro,'',anno)
    print(stazioni.keys())


if __name__ == "__main__":     
    if(len(sys.argv) == 4 and sys.argv[1] == 's'):         
        #s param anno         
        getStazioni(sys.argv[2],sys.argv[3])        
        exit()
    elif(len(sys.argv) == 4):
            #param citta anno
            getStationResult(sys.argv[1],sys.argv[2],sys.argv[3])
    elif(len(sys.argv) == 5):
        #param citta annoInizio annoFine
        annoInizio = int(sys.argv[3])
        annoFine = int(sys.argv[4])
        for anno in range (annoInizio, annoFine + 1):
            getStationResult(sys.argv[1],sys.argv[2],str(anno))
    elif(sys.argv[1] == 'p'):
        getParametri()
        exit()
    

       
       