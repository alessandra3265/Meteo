from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import sys
from htmlParseAereoMultiData import htmlParse
from selenium.webdriver.support.ui import Select
import os
"""
Script in cui specifico nome di una stazione 
Dato un parametro trova tutti i sottoparametri e scrive su file csv
"""
url = "http://clima.meteoam.it/RichiestaDatiGenerica.php"
dir_path = os.path.dirname(os.path.realpath(__file__))
driver_path = dir_path + "\\chromedriver"
optionsFire = Options()
optionsFire.add_argument('--headless')
webdriver = webdriver.Chrome(executable_path=driver_path, options=optionsFire)

def aeronatutica(parametro, city, gi, mi, ai, gf, mf, af):   

    with webdriver as driver:

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
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/section/div/section[2]/div[2]/form/div[2]/input")))

        #result    
        html = driver.page_source

        #close the browser
        driver.quit()
        
        #parsing
        filename = city+'.csv'
        htmlParse(html, filename)       


def getParametri():
    with webdriver as driver:
        #wait = WebDriverWait(driver, 10)      

        # retrive url in headless browser
        driver.get(url)       

        #trovo tutti i parametri (Temperatura, Nuvolosità...) 
        select = Select(driver.find_element_by_id('categoria'))
        all_option  = select.options
        for e in all_option:
            print(e.text)

        #close the browser
        driver.quit()
        return


if __name__ == "__main__":  
    if (len (sys.argv) == 9):
        aeronatutica(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
    elif(len(sys.argv) == 1):
        #se non ci scrivono parametri da riga di comando 
        print('scrivi p per avere elenco parametri disponibili')
        print('specifica Parametro Città giorno mese anno giorno mese anno')
        aeronatutica('Precipitazioni','Pescara', '1','1','2008','1','6','2020')
        
    elif(len(sys.argv) == 2 and sys.argv[1] == 'p'):
        getParametri()

