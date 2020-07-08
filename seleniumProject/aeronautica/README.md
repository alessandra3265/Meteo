# aereoRegione.py
this script allows you to get regional data from http://clima.meteoam.it/RichiestaDatiGenerica.php
specifying Parameter Region and a time interval 

### how to run:
- run `aereoRegione.py p` to get the list of parameters
- run `aereoRegione.py parameter region start_day start_month start_year end_day end_month end_year`</br>

### for example: </br>

- to obtain rainfall data for the period from 1st January 2010 to 1st January 2011</br>
`aereoRegione.py Precipitazioni Lombardia 1 1 2010 1 1 2011`
</br>
- to obtain wind data for the period from 25th June 2020 to 1st July 2020</br>
`aereoRegione.py Wind Lazio 25 6 2020 1 7 2020`

</br>
</br>
## aereoStazione.py 
</br>
this script allows you to get data relating to a city from http://clima.meteoam.it/RichiestaDatiGenerica.php </br>
specifying Parameter City and a time interval 
</br>
the list of available cities is on the website</br>

## examples
`aereoStazione.py Temperatura Pescara 4 5 2015 7 8 2019`




