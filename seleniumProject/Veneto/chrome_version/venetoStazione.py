from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
eseguire     py venetoStazione.py p     per avere l'elenco dei parametri disponibili
eseguire     py venetoStazione.py s anno parametro     per avere elenco delle stazioni 
eseguire     py venetoStazione.py anno parametro stazione per avere i dati relativi 
lo script scrive un file NomeStazione.csv con i risultati 
"""

url_base = "https://www.arpa.veneto.it/bollettini/storico/"
p = Path(os.path.realpath(__file__))
parent = p.parent.parent.parent
driver_path = os.path.join(parent,"chromedriver")

optionsFire = Options()
optionsFire.add_argument('--headless')
webdriver = webdriver.Chrome(executable_path=driver_path, options=optionsFire)

""" 
nel html a ogni stazione è associato un numero 
costruisce un dizionario che associa il nome di
ogni stazione con il numero 
"""
def getDictonaryStation(anno, parametro, city): 
    url = "https://www.arpa.veneto.it/bollettini/storico/Mappa_2020_" + parametro + ".htm?t=RG"
    with webdriver as driver:
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
def getStationResult(anno, parametro, city):
    stazioniDict = getDictonaryStation(anno, parametro, city)

    #costuisco il link della singola stazione
    codice = stazioniDict[city]
        
    link = anno + '/' + codice + '_' + anno + '_' + parametro + '.htm'
    link_result = url_base + link
    print(link_result)
    #surf to pagina dati
    session = HTMLSession()
    result = session.get(link_result)
    html= result.html.html
    html_list = []
    html_list.append(html)
    session.close()
    
    #parsing e scrittura su file
    filename = city + '.csv'
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
def getStazioni(anno, parametro):
    stazioni = getDictonaryStation(anno, parametro,'')
    print(stazioni.keys())


if __name__ == "__main__":     
    if(len(sys.argv) == 4): 
        if (sys.argv[1] == 's'):
            getStazioni(sys.argv[2],sys.argv[3])
        else:
            getStationResult(sys.argv[1],sys.argv[2],sys.argv[3])
    elif(len(sys.argv) == 2):
        if(sys.argv[1] == 'p'):
            getParametri()
        
    else:
        # se non si speficano parametri sulla riga di comando 
        getStationResult('2020','PREC','Padova')

       
       