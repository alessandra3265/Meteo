# venetoTutte.py 
Scripts for the website: https://www.arpa.veneto.it/bollettini/storico/Mappa_2020_TEMP.htm.

## dependencies:
- requests_html
- BeautifulSoup
- urllib

this script allows you to get data of all stations of Veneto
specifying Parameter Years of interest.


## how to run: 
- run `venetoTutte.py parametro anno` to get results </br> 

### multiple years can be specified:

- run `venetoProvince.py parametro anno_inizio anno_fine` to get data from year to year

## for example: </br>

- to obtain 2020 rainfall data from all stations </br>
`venetoTutte.py PREC 2020`

- to obtain t2018 temperature data from all stations  </br>
`venetoTutte.py TEMP 2018`

- to obtain all pressure data from 2015 to 2020 </br>
`venetoTutte.py PRESS 2015 2020`

# venetoProvince.py and venetoStazione.py
Scripts for the website: https://www.arpa.veneto.it/bollettini/storico/Mappa_2020_TEMP.htm.

## dependencies:
- Selenium
- BeautifulSoup
- urllib

see: https://github.com/alessandra3265/Meteo#prerequisites.

# venetoProvince.py
this script allows you to get data of the provinces of Veneto
specifying Parameter Province Year of interest.

You can also obtain ***data of all provinces*** specifying *tutte* instead of province.

## how to run: 
- run `venetoProvince.py parametro Provincia anno` to get results </br> 
- you can also run `venetoProvince.py p` to get the list of all parameters 

### multiple years can be specified:

- run `venetoProvince.py parametro Provincia anno_inizio anno_fine` to get data from year to year

## for example: </br>

- to obtain rainfall data for all stations in the province of Padova</br>
`venetoProvince.py PREC Padova 2020`

- to obtain temperature data for all stations in the province of Venice </br>
`venetoProvince.py TEMP Venezia 2018`

- to obtain all pressure data of the region </br>
`venetoProvince.py PRESS tutte 2020`

- to obtain all speed wind data of the province of Vicenza from 2015 to 2020 </br>
`venetoProvince.py VVENTO Vicenza 2015 2020`

# venetoStazione.py
this script allows you to get data relating to a city 


## how to run:
- run `venetoStazione.py parametro stazione anno` to get results
- you can also run `venetoStazione.py s parametro anno` to get the list of available stations for that particular year for that parameter
- you can also run `venetoStazione.py p` to get the list of all parameters
- multiple years can be specified

### examples 1:

`venetoStazione.py 2017 VENTO Conegliano` to obtain Conegliano's wind data for 2017.

### examples 2:

`venetoStazione.py 2019 RADSOL s`

to obtain all the stations where solar radiation data are available in the year 2019.




