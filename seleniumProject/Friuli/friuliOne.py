from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import sys
from bs4 import BeautifulSoup
from htmlParsing import htmlParsing

"""
script per il friuli 
esecuzione per dati mensili: py seleniumMeteo2.py anno mese             (es: py seleniumMeteo2.py 2020 6)
esecuzione per dati orari: py seleniumMeteo2.py anno mese giorno        (es: py seleniumMeteo2.py 2020 6 20)

scrive i risultati in un file csv hmtlSel.csv
"""

driver_path = "C:\\Users\\Alessandra\\Documents\\meteo\\Meteo\\seleniumProject\\geckodriver"
url = 'https://www.osmer.fvg.it/archivio.php?ln=&p=dati'

optionsFire = Options()
optionsFire.add_argument('--headless')
webdriver = webdriver.Firefox(executable_path=driver_path, options=optionsFire)

def query (type, year, month, s, day):
    
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

        #tipo ricerca: giornaliero o orario
        xpath_giornalieri = '//*[@id="giornalieri"]'
        xpath_orari = '//*[@id="orari"]'        
       
        if (type == 'giorno'):
            xpath_type = xpath_giornalieri
        else:
            xpath_type = xpath_orari        

        #anno        
        anno_target = 2021 - int(year) #in questo modo 2020->1, 2019->2, 2018->3 ... 
        anno_target_xpath = '/html/body/div[1]/div[1]/div/div/div[2]/form/div/div[1]/div/select[1]/option[' + str(anno_target) + ']'
        
        #mese 
        mese_target_xpath = '/html/body/div[1]/div[1]/div/div/div[2]/form/div/div[1]/div/select[2]/option[' + str(month) + ']'
        
        #giorno      
        giorno_target_xpath = '/html/body/div[1]/div[1]/div/div/div[2]/form/div/div[1]/div/select[3]/option['  + str(day) + ']' 

        #fill the form 
        anno.find_element_by_xpath(anno_target_xpath).click()
        mese.find_element_by_xpath(mese_target_xpath).click()
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/form/div/div[2]/div/select/option['+str(s)+']').click() #stazione
        tipo.find_element_by_xpath(xpath_type).click()

        #clicco sul giorno scelto 
        if (type == 'orari'):
            giorno.find_element_by_xpath(giorno_target_xpath).click()

        #wait 
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="visualizza"]')))

        #click 
        driver.find_element_by_id("confnote").click()
        driver.find_element_by_id("visualizza").click()

        #wait
        #wait.until(EC.visibility_of_all_elements_located((By.ID, "dati")))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="salvaDatiPdf"]')))
                
        #HTML parsing e scrittura su file     
        html = driver.page_source
        driver.quit()
        htmlParsing(html)
        
   
        
if __name__ == "__main__":    
    if(len(sys.argv) == 4):
        print('hai scelto dati mensili')
        query('giorno', sys.argv[1], sys.argv[2],sys.argv[3], 1)
    elif(len(sys.argv) == 4):
        print('hai scelto dati orari')
        query('orari', sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4])
    else:
        query('giorno', 2020, 6,2, 1)
        


    