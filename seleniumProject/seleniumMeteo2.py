from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import sys

driver_path = "C:\\Users\\Alessandra\\Documents\\meteo\\Meteo\\seleniumProject\\geckodriver"
url = 'https://www.osmer.fvg.it/archivio.php?ln=&p=dati'

optionsFire = Options()
optionsFire.add_argument('--headless')
webdriver = webdriver.Firefox(executable_path=driver_path, options=optionsFire)

"""
type specificare 'giorno' per dati giornalieri, 
     specificare 'orari' per dati orari 

esempio esecuzione: py seleniumMeteo2.py giorno 2020 6 22
"""


def query (type, year, month, day):
    
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
        
        """
        anno.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/form/div/div[1]/div/select[1]/option[1]').click()
        mese.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/form/div/div[1]/div/select[2]/option[6]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/form/div/div[2]/div/select/option[2]').click() #stazione
        tipo.find_element_by_xpath(xpath_type).click()
        """ 
        
        #fill the form 
        anno.find_element_by_xpath(anno_target_xpath).click()
        mese.find_element_by_xpath(mese_target_xpath).click()
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/form/div/div[2]/div/select/option[2]').click() #stazione
        tipo.find_element_by_xpath(xpath_type).click()

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
        

        #HTML parsing 
        print(result.text)
        driver.close()
   
        
if __name__ == "__main__":
    print(len(sys.argv))
    if(len(sys.argv) > 4):
        query(sys.argv[1], sys.argv[2], sys.argv[3], 1)
    else:
        query('giorno', 2020, 6, 22)
        


    