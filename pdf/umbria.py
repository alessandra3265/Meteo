import camelot
import sys
import os
"""
importa tutti i dati della pioggia del Umbria dal 2014 al 2020
eseguire: umbria.py 2020            dati del 2020
          umbria.py 2015 2018       dati dal 2015 al 2018
          umbria.py tutti           tutti gli anni disponibili - dal 2014 al 2020

solo le prime 5 stazioni su 87
stampa il percoso dei file dei risultati 
"""

url_list = []
url_list.append("https://www.regione.umbria.it/documents/18/8536600/pioggia+2014/adfd95a0-71df-4619-a49b-8a317dfad3bd") #2014
url_list.append("https://www.regione.umbria.it/documents/18/8536600/pioggia+2015/5c11cf8d-3e83-4334-99fb-e2239958d586") #2015
url_list.append("https://www.regione.umbria.it/documents/18/7110267/Dati+di+pioggia+gennaio-settembre+2016/b24c122c-1a4c-40dd-bf17-1fdc9713b8b6") #2016
url_list.append("https://www.regione.umbria.it/documents/18/8536600/Dati+pioggia+gennaio-aprile+2017/54b95f6f-088d-4576-b516-70d05cad7b17") #2017
url_list.append("https://www.regione.umbria.it/documents/18/7110267/Dati+pioggia+2018/7e1f11e3-0342-43ad-8709-8d4472c0ef90") #2018
url_list.append("https://www.regione.umbria.it/documents/18/7110267/DATI+PIOGGIA+2019/c6db2485-09a1-4808-90a4-f65cbec67e68") #2019
url_list.append("https://www.regione.umbria.it/documents/18/7110267/DATI+PIOGGIA+2020+.pdf/cad0f440-8ace-4646-a67d-9d6ef4cf4395") #2020

path_src = os.path.dirname(os.path.realpath(__file__)) #path del file sorgente
path_result = os.path.join(path_src,"umbria_result") #path cartella dei risultati nella stessa directory del sorgente

def all_data() :
    i = 0
    for url in url_list:       
        tables = camelot.read_pdf(url, flavor='stream', strip_text='\n', pages='1-5') #prime 30 stazioni  
        filename = os.path.join(path_result, 'umbria' + str(i) + '.xlsx')   
        i += 1 
        tables.export(filename, f='excel', compress=False) # export the list of tables

def year_data(anno): 
    #print(anno)  
    if (is_file_in_cache(anno)):
        return
    for url in url_list:        
        if (anno in url):   
            #print(url)         
            tables = camelot.read_pdf(url, flavor='stream', strip_text='\n', pages='1-3')
            filename = getFilenameResult(anno) #\Meteo\pdf\umbria_result\umbria2014.xlsx            
            tables.export(filename, f='csv', compress=False)
            print(filename)

#built the filename result based on anno 
def getFilenameResult(anno) :
    return os.path.join(path_result, 'pioggia' + anno + '.csv') #\Meteo\pdf\umbria_result\umbria2014.xlsx 

#check if a file is already in result directory
#if true print his path
def is_file_in_cache(anno):
    arr = os.listdir(path_result)
    for file_name in arr:
        if (anno in file_name):            
            print(getFilenameResult(anno))
            return True

if __name__ == "__main__":  
    if (len(sys.argv) == 1):
        print('inserisce un anno in formato aaaa')
        exit()

    if (sys.argv[1] == "tutti"):
        all_data()
    if (len(sys.argv) == 2):
        year = int(sys.argv[1])
        if (year < 2014 or year > 2020): #verifica che intervallo anno sia valido 
            print('inserisci un anno tra 2014 e 2020')
        else:            
            year_data(sys.argv[1])
    if (len(sys.argv) == 3):
        year_start = int(sys.argv[1])
        year_end = int(sys.argv[2])
        if (year_start < 2014 or year_end < 2014 or year_start > 2020 or year_end > 2020):
            print('inserisci un anno tra 2014 e 2020')
        else:
            for i in range(year_start, year_end + 1):
                year_data(str(i))