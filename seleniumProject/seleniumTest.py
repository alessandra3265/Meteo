from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys

driver_path = "C:\\Users\\Alessandra\\Documents\\meteo\\Meteo\\seleniumProject\\geckodriver"
url = 'https://www.brainyquote.com/'

optionsFire = Options()
optionsFire.add_argument('--headless')
webdriver = webdriver.Firefox(executable_path=driver_path, options=optionsFire)

search_query = "life"

with webdriver as driver:

    wait = WebDriverWait(driver, 10)

    # retrive url in headless browser
    driver.get(url)
    
    # find search box
    search = driver.find_element_by_id("hmSearch")
    search.send_keys(search_query + Keys.RETURN)
    
    wait.until(presence_of_element_located((By.ID, "quotesList")))
    # time.sleep(3)
    results = driver.find_elements_by_class_name('m-brick')

    for quote in results:
      quoteArr = quote.text.split('\n')
      print(quoteArr)
      print()

    # must close the driver after task finished
    driver.close()