from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import sys

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from urllib import request
from pathlib import Path
import os

"""
Versione regionale
"""
urlPunto = "http://www.cartografiarl.regione.liguria.it/SiraQualMeteo/script/PubAccessoDatiMeteo12.asp"
urlScheda = "http://www.cartografiarl.regione.liguria.it/SiraQualMeteo/script/PubAccessoDatiMeteo13.asp"
driver_path = "C:\\Users\\Alessandra\\Documents\\meteo\\Meteo\\seleniumProject\\geckodriver"
optionsFire = Options()
optionsFire.add_argument('--headless')
def web():  
      
    webdrivers = webdriver.Firefox(executable_path=driver_path, options=optionsFire)
    
    with webdrivers as driver:

        wait = WebDriverWait(driver, 10)        

        # retrive url in headless browser
        driver.get(urlPunto)       
        
        html = driver.page_source
        
        #apro il menu "Tipo dato"
        frequenza = driver.find_element_by_xpath('/html/body/form/div[4]/table/tbody/tr/td[2]/select')
        frequenza.click()
        
        #clicco sul prametro scelto 
        freq = frequenza.find_elements_by_xpath('/html/body/form/div[4]/table/tbody/tr/td[2]/select/option[3]')
        
        #chiudo il menu
        frequenza.click()
        
        #cambio pagina
        driver.get(urlScheda)
        #scelgo il parametro 
        precip = driver.find_element_by_xpath('/html/body/form/div[1]/table/tbody/tr/td[2]/select/option[1]')
        #/html/body/form/div[1]/table/tbody/tr/td[2]/select/option[1]
       
        """ 
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
        """
                     
        """
       #scrollo la pagina
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button_xpath = '//*[@id="visualizzaMessaggi_id"]'
        wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        """
        #inserisco periodo d'interesse
        #periodo_xpath = '/html/body/div[2]/div/section/div/section[2]/div[2]/form/div[2]/input[9]'        
        #periodo = driver.find_element_by_xpath(periodo_xpath)
        #periodo.click()
        #periodo.clear()
        #periodo_string = '' + gi + '/' + mi + '/' + ai + ' - ' + gf + '/' + mf + '/' + af
        #periodo.send_keys(periodo_string + Keys.ENTER)
        
        
        #submit all 
        button_xpath = "/html/body/form/div[3]/table/tbody/tr/td[1]/a"  
        wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))      
        button = driver.find_element_by_xpath(button_xpath)
        button.click()

        #wait
        print('finish')       
        time.sleep(10)
        #aspetto che compaia il bottone 'visualizza preventivo'
        win_after = driver.window_handles[1]
        driver.switch_to_window(win_after)

        try: 
            wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/form/table[1]/tbody/tr/td/img")))
        except TimeoutException as e:                               
            print(e)            
            driver.quit() #quando i dati non sono disponibili 
            return

        #result    
        html = driver.page_source
        
        driver.quit()
        print(html)

   
    
if __name__ == "__main__":  
    web()