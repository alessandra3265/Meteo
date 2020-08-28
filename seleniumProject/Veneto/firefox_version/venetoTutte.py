from bs4 import BeautifulSoup
from urllib import request
from parsingVeneto import final_parsing
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import sys
import os
from pathlib import Path

"""
script per interrogazione aggregata per province
eseguire    venetoTutte.py parametro anno                           per i risultati
eseguire    venetoProvince.py parametro anno_inizio anno_fine       per i risultati da anno_inzio a anno_fine
"""

url_base = "https://www.arpa.veneto.it/bollettini/storico/"
p = Path(os.path.realpath(__file__))
parent = p.parent.parent.parent


path_src = os.path.dirname(os.path.realpath(__file__))
path_result = os.path.join(path_src, 'result')

"""va sulla pagina web e scrive il file con i risultati"""
def getResult(parametro, anno):
    
    filename = parametro + 'tutte' + anno +'.csv'
    filename = os.path.join(path_result, filename)
    
    url = "https://www.arpa.veneto.it/bollettini/storico/Mappa_" + anno + "_" +parametro + ".htm?t=RG"
    print(url)  
    main_page = request.urlopen(url)
    main_page_html = main_page.read()
    main_page.close()
    soup = BeautifulSoup(main_page_html, 'html.parser')
        
    #costruisco i link salvo html relativo
    mappa = soup.find(id = 'STAZIONI')
    links = [link['href'] for link in mappa.find_all('area')]
    #print (links)
    html_list = []
    session = HTMLSession()
    for link in links:        
        link_result = url_base + link      
       
        #surf to pagina dati   
        result = session.get(link_result)
        html_list.append(result.html.html)
        session.close()
       
    #parsing e scrittura su file    
    final_parsing(html_list, anno,parametro,'tutte', filename)
    
        
if __name__ == "__main__": 
    parametri = ['TEMP', 'PREC', 'LIVIDRO', 'SUOLO', 'RADSOL', 'UMID','PORTATA','BFOGL','VVENTO','PRESS','LIVNEVE']
    if (len(sys.argv) > 1):
        if (sys.argv[1] not in parametri):
            print('parametro non corretto: ', sys.argv[1] )
            print('scegli un parametro tra:')
            print(parametri)
            exit()

    if(len(sys.argv) == 3):
        #param anno 
        getResult(sys.argv[1],sys.argv[2])
    elif(len(sys.argv) == 4):
        #param anno_inizio anno_fine
        anno_inizio = int(sys.argv[2])
        anno_fine = int(sys.argv[3])
        for anno in range (anno_inizio, anno_fine + 1):
            getResult(sys.argv[1], anno)
    else:
        getResult('TEMP', '2016')

    

       
       