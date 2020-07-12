from urllib import request
from bs4 import BeautifulSoup
import re
import camelot
import sys
import os 
"""
param è idro oppure termo
anni da 2004 al 2017 per idro
anni da 2006 a 2016 per termo
"""
url_base = "http://www.idrografico.regione.lazio.it/"
html_homepage = request.urlopen('http://www.idrografico.regione.lazio.it/std_page.aspx-Page=bollettini.htm')
soup_homepage = BeautifulSoup(html_homepage, 'html.parser')
dir_path = os.path.dirname(os.path.realpath(__file__))

def query(param, anno, mese):    
    #trovo tutti i link alle pagine che contengono i bolletti idrologici dei vari anni 
    for e in soup_homepage.findAll('a'):
        link = e.get('href')
        if (param in link and anno in link):
            target_anno_link = link

    target_link = url_base + target_anno_link    

    #apro la pagina di un bollettino di un anno (es 2004)
    html_page = request.urlopen(target_link)
    soup2 = BeautifulSoup(html_page, 'html.parser')

    for e in soup2.findAll('a'):
        link = e.get('href')
        if ("Bollettini" in link and mese in link):
            #Documenti/Bollettini/Bollettini Idrologici/Anno 2004/01 - Gennaio.pdf
            link = link.replace(' ','%20')
            target_mese_link = link
    target_mese_link = url_base + target_mese_link   

    tables = camelot.read_pdf(target_mese_link,pages='1', multiple_tables = False, flavor='stream', strip_text='\n')
    filename = dir_path + "\\result\\" + param + anno +mese + ".csv"
    tables[0].to_csv(filename)

def mese_from_link(link_str):
    #funzione che decuce l'anno e il mese dal link
    #del tipo "Documenti/Bollettini/Bollettini%Idrologici/Anno%2004/01%-%Gennaio.pdf"
    stringhe = link_str.split('/')
    for s in stringhe:              
        #deduco il mese che precede sempre .pdf
        if ('.pdf' in s):
            mese = s.split('%')[0]
            return mese
     
def anno_from_link(link_str):
    #funzione che decuce l'anno e il mese dal link
    #del tipo "Documenti/Bollettini/Bollettini Idrologici/Anno%202004/01 - Gennaio.pdf"
    stringhe = link_str.split('/')
    for s in stringhe:              
        if ('Anno%20' in s):
            anno = s.split('%20')[1]
            return anno

def query_pa(param, anno):
    #trovo tutti i link alle pagine che contengono i bolletti idrologici dei vari anni 
    for e in soup_homepage.findAll('a'):
        link = e.get('href')
        if (param in link and anno in link):
            target_anno_link = link

    target_anno_link = url_base + target_anno_link   

    #vado sulla pagina dell'anno 
    html_page = request.urlopen(target_anno_link)
    soup2 = BeautifulSoup(html_page, 'html.parser')
    target_links = []
    for e in soup2.findAll('a'):
        link = e.get('href')
        if ("Bollettini" in link):
            #Documenti/Bollettini/Bollettini Idrologici/Anno 2004/01 - Gennaio.pdf
            link = link.replace(' ','%20')
            target_links.append(url_base+ link)
    
    target_links.pop() #tolgo l'ultimo link (riepilogo semestre)
    target_links.pop() #tolgo l'ultimo link (riepilogo annuale)

    for l in target_links:
        mese = mese_from_link(l)   
        tables = camelot.read_pdf(l,pages='1', multiple_tables = False, flavor='stream', strip_text='\n')
        filename = dir_path + "\\result\\" + param + anno +mese + ".csv"
        tables[0].to_csv(filename)
        
    
    
    
def query_p(param):
    if (param == 'idro'):
        param = "boll_idro"
    if (param == 'termo'):
        param = "boll_termo"
    #versione in cui specifico solo il parametro 
    target_anni_link = []
    for e in soup_homepage.findAll('a'):
        link = e.get('href')
        if (param in link):
            link = url_base + link
            target_anni_link.append(link)
    
    for lk in target_anni_link:
        html_page = request.urlopen(lk)
        soup2 = BeautifulSoup(html_page, 'html.parser')
        target_links = []
        for e in soup2.findAll('a'):
            link = e.get('href')
            if ("Bollettini" in link and 'pdf' in link):
                #Documenti/Bollettini/Bollettini Idrologici/Anno 2004/01 - Gennaio.pdf
                link = link.replace(' ','%20')
                target_links.append(url_base+ link)
        if (len(target_links) == 0):
            break #if no result

        target_links.pop() #tolgo l'ultimo link (riepilogo semestre)
        target_links.pop() #tolgo l'ultimo link (riepilogo annuale)

        for l in target_links:            
            mese = mese_from_link(l) 
            anno = anno_from_link(l)       
            
            tables = camelot.read_pdf(l,pages='1', multiple_tables = False, flavor='stream', strip_text='\n')
            filename = dir_path + "\\result" + param + mese+anno + ".csv"
            tables[0].to_csv(filename)
            

def verifica_dispon(p,a):
    a = int(a)
    if (p == "idro"):
        if (a > 2003 and a < 2018):
            return True
        else:
            print('spefica un anno compreso tra 2004 e 2017') 
    if (p == "termo"):        
        if (a > 2005 and a < 2017):            
            return True
        else:
            print('spefica un anno compreso tra 2006 e 2016') 

if __name__ == "__main__":  
    if (len(sys.argv) == 1):
        print('specifica parametro anno mese')
        exit()

    elif (len(sys.argv) == 4):
        param = sys.argv[1]
        anno = sys.argv[2]
        mese = sys.argv[3]
        print(param)
        if(verifica_dispon(param,anno)):
            query(param, anno, mese)

    elif (len(sys.argv) == 3):
        param = sys.argv[1]
        anno = sys.argv[2]   
        if(verifica_dispon(param,anno)):
            query_pa(param, anno)
    elif (len(sys.argv) == 2):
        param = sys.argv[1]                
        query_p(param)
