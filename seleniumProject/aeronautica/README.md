# aereoRegione.py and aereoStazione.py


## dependencies:
- Selenium
- BeautifulSoup
- urllib

### to install Selenium:
run in comand line:
- `pip install selenium`
- download the driver for your browser:

Chrome: 	https://sites.google.com/a/chromium.org/chromedriver/downloads </br>
Edge: 	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ </br>
Firefox: 	https://github.com/mozilla/geckodriver/releases </br>
Safari: 	https://webkit.org/blog/6900/webdriver-support-in-safari-10/ </br>

- extract the directory 
- copy and paste the *driver_name.exe* in the directory ***SeleniumProject***.

For example, if you use **Chrome**:</br>

- copy the chormedriver.exe file in the directory ***SeleniumProject***.

if you use **Mozilla Firefox**:
- copy the geckodriver.exe file in the directory ***SeleniumProject***.

### to install BeautifulSoup:
run in comand line:
`pip install beautifulsoup4`

### to install urllib:
run in comand line:
`pip install urllib`

# aereoRegione.py
this script allows you to get regional data from http://clima.meteoam.it/RichiestaDatiGenerica.php
specifying Parameter Region and a time interval 

## how to run:
- run `aereoRegione.py p` to get the list of parameters
- run `aereoRegione.py parameter region start_day start_month start_year end_day end_month end_year`</br>

## for example: </br>

- to obtain rainfall data for the period from 1st January 2010 to 1st January 2011</br>
`aereoRegione.py Precipitazioni Lombardia 1 1 2010 1 1 2011`

- to obtain wind data for the period from 25th June 2020 to 1st July 2020</br>
`aereoRegione.py Vento Lazio 25 6 2020 1 7 2020`

# aereoStazione.py
this script allows you to get data relating to a city from http://clima.meteoam.it/RichiestaDatiGenerica.php </br>
specifying Parameter City and a time interval 
</br>
the list of available cities is on the website</br>

## how to run:
- run `aereoStazione.py p` to get the list of parameters
- run `aereoStazione.py parameter station start_day start_month start_year end_day end_month end_year`</br>

## examples
`aereoStazione.py Temperatura Pescara 4 5 2015 7 8 2019`




