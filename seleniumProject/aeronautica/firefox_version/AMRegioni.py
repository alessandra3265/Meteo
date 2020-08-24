from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import sys
from parsePerRegioni3 import finalParsing
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from urllib import request
from pathlib import Path
import os

"""
script per interrogazione del sito dell'Aeronautica Militare
accetta in ingresso:
arametro Regione giorno mese anno giorno mese anno
Dato un parametro trova tutti i sottoparametri e scrive su file
seleziona le stazioni a gruppi di 25 
"""
path_src = os.path.dirname(os.path.realpath(__file__))        
path_result = os.path.join(path_src,"result")

def aeronatutica(parametro, gi, mi, ai, gf, mf, af,html_list, citylist, tentativo, time_sleep):      
    
    webdrivers = webdriver.Firefox(executable_path=driver_path, options=optionsFire)
    
    with webdrivers as driver:

        wait = WebDriverWait(driver, 25)  
        driver.get(url)

        #apro il menu "Parametri: Seleziona la categoria"
        categoria = driver.find_element_by_xpath('/html/body/div[2]/div/section/div/section[2]/div[2]/form/fieldset/div/button')
        categoria.click()
        
        #click sul prametro scelto 
        precip = driver.find_element_by_link_text(parametro)
        precip.click() 

        #apertura il menu "Dettaglio parametri"
        param_xpath = '/html/body/div[2]/div/section/div/section[2]/div[2]/form/fieldset[2]/div/button/span[1]'
        wait.until(EC.element_to_be_clickable((By.XPATH, param_xpath)))
        param = driver.find_element_by_xpath(param_xpath)
        param.click()
        
        #trova tutti i dettagli parametri 
        select = Select(driver.find_element_by_id('parametri_input_id'))
        all_option  = select.options
        dettagli_text = []
        for e in all_option:
            dettagli_text.append(e.text)
           
        #clicco su tutti i dettagli del parametro scelto 
        for i in range(len(dettagli_text)):
            dettaglio = driver.find_element_by_link_text(dettagli_text[i])
            dettaglio.click() 
        
        param.click() #chiudo il menu "Dettaglio Parametri"           

        #apro il menu "Stazione: Seleziona una o più stazioni"
        stazione_xpath = '/html/body/div[2]/div/section/div/section[2]/div[2]/form/div[1]/fieldset/div/button/span[1]'
        formx = "/html/body/div[2]/div/section/div/section[2]/div[2]/form/div[1]/fieldset/div/div/div/input"
        wait.until(EC.element_to_be_clickable((By.XPATH, stazione_xpath)))    
        stazione = driver.find_element_by_xpath(stazione_xpath)
        stazione.click()
        form = driver.find_element_by_xpath(formx)
        

        #seleziono una stazione      
        for city in citylist:
            form.clear()
            form.send_keys(city + Keys.ENTER)  
                
        #chiudo il menu stazione
        stazione.click()               

       #scrollo la pagina
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button_xpath = '//*[@id="visualizzaMessaggi_id"]'
        wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        #inserisco periodo d'interesse
        periodo_xpath = '/html/body/div[2]/div/section/div/section[2]/div[2]/form/div[2]/input[9]'        
        periodo = driver.find_element_by_xpath(periodo_xpath)
        periodo.click()
        periodo.clear()
        periodo_string = '' + gi + '/' + mi + '/' + ai + ' - ' + gf + '/' + mf + '/' + af
        periodo.send_keys(periodo_string + Keys.ENTER) #inserisco il periodo e premo invio
                
        #submit all   
        wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))      
        button = driver.find_element_by_xpath(button_xpath)
        button.click()

        #wait
        print('finish')       
        time.sleep(time_sleep)
        #aspetta che compaia il bottone 'visualizza preventivo'
        try: 
            wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/section/div/section[2]/div[2]/form/div[2]/input")))
        except TimeoutException as e:
            if (tentativo == 1):
                print(e)
                print('dati non presenti')
                driver.quit() #quando i dati non sono disponibili 
                return
            else:
                print('riprovo')
                aeronatutica(parametro, gi, mi, ai, gf, mf, af,html_list, citylist,1, 20)

        #result    
        html = driver.page_source
        html_list.append(html)
        driver.quit()
        
    
def find_city_in_region():
    url = "http://clima.meteoam.it/RichiestaDatiGenerica.php"
    #build dictonary region : citylist
    regioni = {}
    resp = request.urlopen(url)
    data = resp.read()
    html = data.decode("UTF-8")
    soup = BeautifulSoup(html, 'html.parser')    
    cityList = soup.find_all('optgroup')
    for e in cityList:
        regione = e['label']
        opzioni = e.find_all('option')
        cityList = []
        for m in opzioni:            
            cityList.append(m.string)        
        regioni[regione] = cityList
    return regioni    

#built the filename result based on anno 
def getFilenameResult(parametro, regione_name, ai, af) :
    return parametro + regione_name + ai + af + '.csv'     

#check if a file is already in result directory
#if true print his path
def is_file_in_cache(parametro, regione_name, ai, af):
    filename = getFilenameResult(parametro, regione_name, ai, af)
    arr = os.listdir(path_result)
    for file_name in arr:
        if (filename == file_name): 
            print(file_name)        
            return True

    
if __name__ == "__main__":  
    region_dict = find_city_in_region()    
    if (len(sys.argv)==9):   
        regione_name = sys.argv[2] 
        parametro = sys.argv[1]
        gi = sys.argv[3]
        mi = sys.argv[4]
        ai = sys.argv[5]
        gf = sys.argv[6]
        mf = sys.argv[7]
        af = sys.argv[8]
        list_of_city_list = []

        if (is_file_in_cache(parametro, regione_name, ai, af)):
            exit()

        if ((int(af) - int(ai)) > 5) :
            print('intervallo max: 4 anni')
            sys.exit()

        if (sys.argv[2] == 'tutte'):            
            last = 0
            first = 0
            i = 1
            values = []
            for e in list(region_dict.values()):
                for x in e:
                    values.append(x)
            while (True):  
                last = (i)*8  
                if (last > len(values)):
                    city_list = values[first:len(values)]  
                    list_of_city_list.append(city_list)  
                    break      
                city_list = values[first:last]  
                list_of_city_list.append(city_list)   
                first = last 
                i += 1    
        else:
            list_of_city_list.append( region_dict[regione_name])
    else:
        print('specifica: Parametro Regione giorno mese anno giorno mese anno')
        sys.exit()
        regione_name = 'Lombardia'
        parametro = 'Precipitazioni'
        gi='1' 
        mi='1' 
        ai='2016'
        gf='3' 
        mf='8' 
        af='2020' 
        
        list_of_city_list = []
        last = 0
        first = 0
        i = 1
        values = []
        for e in list(region_dict.values()):
            for x in e:
                values.append(x)
        while (True):  
            last = (i)*25  
            if (last > len(values)):
                city_list = values[first:len(values)]  
                list_of_city_list.append(city_list)  
                break      
            city_list = values[first:last]  
            list_of_city_list.append(city_list)   
            first = last 
            i += 1   
        
    
    url = "http://clima.meteoam.it/RichiestaDatiGenerica.php"
    p = Path(os.path.realpath(__file__))
    parent = p.parent.parent.parent
    driver_path = os.path.join(parent,"geckodriver")
    optionsFire = Options()
    optionsFire.add_argument('--headless')
    html_list = []   
   
    for cityList in list_of_city_list: 
        print(cityList)            
        aeronatutica(parametro, gi, mi, ai, gf, mf, af, html_list, cityList,0,3)                              
    
    if (len(html_list) != 0):        
        filename = parametro + regione_name + ai + af + '.csv'
        filename = os.path.join(path_result, filename)  
        finalParsing(html_list, filename)
    
    