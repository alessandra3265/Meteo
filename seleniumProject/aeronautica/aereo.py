from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import sys



url = "http://clima.meteoam.it/RichiestaDatiGenerica.php"
driver_path = "C:\\Users\\Alessandra\\Documents\\meteo\\Meteo\\seleniumProject\\geckodriver"

optionsFire = Options()
optionsFire.add_argument('--headless')
webdriver = webdriver.Firefox(executable_path=driver_path, options=optionsFire)

def aeronatutica(parametro, dettaglio, gi, mi, ai, gf, mf, af): 
    dettaglio = dettaglio.replace('_', ' ')

    with webdriver as driver:

        wait = WebDriverWait(driver, 20)        

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

        #clicco sul dettaglio parametro scelto 
        prec_cumulata = driver.find_element_by_link_text(dettaglio)
        prec_cumulata.click() 
        param.click()

        #apro il menu "Stazione: Seleziona una o più stazioni"
        stazione_xpath = '/html/body/div[2]/div/section/div/section[2]/div[2]/form/div[1]/fieldset/div/button/span[1]'
        wait.until(EC.element_to_be_clickable((By.XPATH, stazione_xpath)))    
        stazione = driver.find_element_by_xpath(stazione_xpath)
        stazione.click()

        #seleziono una stazione
        form = driver.find_element_by_class_name('form-control')
        form.send_keys("Pescara" + Keys.ENTER)   
        

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
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.select_one("table")
        
        headers = [th for th in table.select("tr")]
        row = [th.text.strip() for th in headers[0].select("th")]
        
        
        #dati
        #dati = [[td.text for td in row.find_all('td')] for row in table.select("tr")] 
        dati = []
        for rows in table.select("tr"):
            for td in rows.find_all('td'):
                dati.append(td.text)

        print(row)
        print(dati)

if __name__ == "__main__":  
    if (len (sys.argv) == 9):
        aeronatutica(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
    else:
        aeronatutica('Precipitazioni','Precipitazione_cumulata', 2,5,2020,2,6,2020)

    