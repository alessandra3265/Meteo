# aereoRegione.py and aereoStazione.py
Scripts for the website: http://clima.meteoam.it/RichiestaDatiGenerica.php.

## dependencies:
- Selenium
- BeautifulSoup
- urllib

see: https://github.com/alessandra3265/Meteo#prerequisites.

# aereoRegione.py
this script allows you to get regional data from http://clima.meteoam.it/RichiestaDatiGenerica.php
specifying Parameter Region and a time interval 

## how to run:
- run `aereoRegione.py p` to get the list of parameters
- run `aereoRegione.py parameter region start_day start_month start_year end_day end_month end_year`</br>
- run `aereoRegione.py parameter tutte start_day start_month start_year end_day end_month end_year` to get data from *all* regions.


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




