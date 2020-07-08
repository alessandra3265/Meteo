from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import sys
from parsePerRegioni import finalParsing
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from urllib import request


"""
Versione in cui specifico una regione 
Dato un parametro trova tutti i sottoparametri e scrive su file
TODO: memorizza tutte le stazioni di una regione
      aggiustare il parsing che non supporta più anni 

url = "http://clima.meteoam.it/RichiestaDatiGenerica.php"
driver_path = "C:\\Users\\Alessandra\\Documents\\meteo\\Meteo\\seleniumProject\\geckodriver"
optionsFire = Options()
optionsFire.add_argument('--headless') 
"""

#global webdriver
#webdriver = webdriver.Firefox(executable_path=driver_path, options=optionsFire)

def aeronatutica(parametro, city, gi, mi, ai, gf, mf, af,html_list):  
   # url = "http://clima.meteoam.it/RichiestaDatiGenerica.php"
   # driver_path = "C:\\Users\\Alessandra\\Documents\\meteo\\Meteo\\seleniumProject\\geckodriver"
   # optionsFire = Options()
   # optionsFire.add_argument('--headless')
   # global webdrivers   
    webdrivers = webdriver.Firefox(executable_path=driver_path, options=optionsFire)
    
    with webdrivers as driver:

        wait = WebDriverWait(driver, 10)        

        # retrive url in headless browser
        driver.get(url)

        #apro il menu "Parametri: Seleziona la categoria"
        categoria = driver.find_element_by_xpath('/html/body/div[2]/div/section/div/section[2]/div[2]/form/fieldset/div/button')
        categoria.click()
        
        #clicco sul prametro scelto 
        precip = driver.find_element_by_link_text(parametro)
        precip.click() 

        #apro il menu "Dettaglio parametri"
        param_xpath = '/html/body/div[2]/div/section/div/section[2]/div[2]/form/fieldset[2]/div/button/span[1]'
        wait.until(EC.element_to_be_clickable((By.XPATH, param_xpath)))
        param = driver.find_element_by_xpath(param_xpath)
        param.click()

        #trovo tutti i parametri (Temperatura, Nuvolosità...) 
        #select = Select(driver.find_element_by_id('categoria'))
        #all_option  = select.options
        #for e in all_option:
           # print(e.text)


        #trovo tutti i dettagli parametri 
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
        wait.until(EC.element_to_be_clickable((By.XPATH, stazione_xpath)))    
        stazione = driver.find_element_by_xpath(stazione_xpath)
        stazione.click()

        #seleziono una stazione        
        choice = driver.find_element_by_link_text(city)
        choice.click() 
        
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
        periodo.send_keys(periodo_string + Keys.ENTER)
        
        
        #submit all   
        wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))      
        button = driver.find_element_by_xpath(button_xpath)
        button.click()

        #wait
        print('finish')       
        time.sleep(3)
        #aspetto che compaia il bottone 'visualizza preventivo'
        try: 
            wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/section/div/section[2]/div[2]/form/div[2]/input")))
        except TimeoutException as e:
            print(e)
            print('Non ci sono dati per: ' + city)
            driver.quit() #quando i dati non sono disponibili 
            return

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
        if (sys.argv[1] == 'tutte'):
            city_list = []
            for e in region_dict.values():
                city_list = city_list + e            
        else:
            city_list = region_dict[regione_name]
    else:
        print('specifica: Parametro Regione giorno mese anno giorno mese anno')
        sys.exit()
        regione_name = 'Lombardia'
        parametro = 'Precipitazioni'
        gi='1' 
        mi='1' 
        ai='2010'
        gf='1' 
        mf='1' 
        af='2011' 
        city_list = region_dict['Lombardia']
    
    
    url = "http://clima.meteoam.it/RichiestaDatiGenerica.php"
    driver_path = "C:\\Users\\Alessandra\\Documents\\meteo\\Meteo\\seleniumProject\\geckodriver"
    optionsFire = Options()
    optionsFire.add_argument('--headless')
    html_list = []
   
    for c in city_list:
        print('controllo ' + c)         
        aeronatutica(parametro, c, gi, mi, ai, gf, mf, af, html_list)               
        

    if (len(html_list) != 0):
        filename = regione_name + '.csv'
        finalParsing(html_list, filename)
        print('ci sono risultati')
    