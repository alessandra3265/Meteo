from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import sys

"""
VERSIONE CHE PRODUCE DATI IN MANIERA NON DETERMINISTICA
"""


driver_path = "C:\\Users\\Alessandra\\Documents\\meteo\\Meteo\\seleniumProject\\geckodriver"
url = 'https://www.osmer.fvg.it/archivio.php?ln=&p=dati'

ari = 'ARI@Ariis@syn@45.878300@13.090000@13'

optionsFire = Options()
optionsFire.add_argument('--headless')
webdriver = webdriver.Firefox(executable_path=driver_path, options=optionsFire)

with webdriver as driver:

    wait = WebDriverWait(driver, 20)
    

    # retrive url in headless browser
    driver.get(url)
    form = driver.find_element_by_id("frmStazDati")

    #nomi e valori delle stazioni meteo
    stazione = form.find_element_by_id("stazione")
    all_options = stazione.find_elements_by_tag_name("option")
    stazioni_value = [s.get_attribute("value") for s in all_options[1:]] 
    
    stazioni = {}    
    stazioni_name = [s.text for s in all_options[1:]]   

    for i in range(len(stazioni_value)):
        stazioni[stazioni_name[i]] = stazioni_value[i]    

    #data fields 
    anno = driver.find_element_by_id("anno")
    mese = driver.find_element_by_id("mese")
    giorno = driver.find_element_by_id("giorno")
    tipo = driver.find_element_by_name("tipo")

    #fill form   
    target_stazione = stazioni_value[0]    
    anno.send_keys("2020")
    mese.send_keys('2')
    stazione.send_keys(target_stazione)  
    tipo.send_keys('H_3')    

    #wait 
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="visualizza"]')))

    #click 
    driver.find_element_by_id("confnote").click()
    driver.find_element_by_id("visualizza").click()

    #wait
    #wait.until(EC.visibility_of_all_elements_located((By.ID, "dati")))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="salvaDatiPdf"]')))

    #result page
    result = driver.find_element_by_id("dati")
    print(result.text)
    driver.close()
   

