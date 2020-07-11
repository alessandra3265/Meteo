# venetoProvince.py and venetoStazione.py
Scripts for the website: .

## dependencies:
- Selenium
- BeautifulSoup
- urllib

see: https://github.com/alessandra3265/Meteo#prerequisites.

# aereoProvince.py
this script allows you to get data of the provinces of Veneto
specifying Year Parameter Province of interest

## how to run:
- run `venetoProvince.py anno parametro Provincia` to get results </br> 
- you can also run `venetoProvince.py p` to get the list of all parameters 

## for example: </br>

- to obtain rainfall data for all stations in the province of Padova</br>
`venetoProvince.py 2020 PREC Padova`

- to obtain temperature data for all stations in the province of Venice </br>
`venetoProvince.py 2018 TEMP Venezia`

# venetoStazione.py
this script allows you to get data relating to a city 


## how to run:
- run `venetoStazione.py anno parametro stazione` to get results
- you can also run `venetoStazione.py s anno parametro` to get the list of available stations for that particular year for that parameter
- you can also run `venetoStazione.py p` to get the list of all parameters

## examples
`venetoStazione.py 2017 VENTO Conegliano` to obtain Conigliano's data.

`venetoStazione.py 2019 RADSOL s`

to obtain all the stations where solar radiation data are available in the year 2019.




