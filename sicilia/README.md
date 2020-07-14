# Sicilia

Script that queries the site: http://meteo.astropa.unipa.it/public/

## Requirement:
* RoboBrowser
* urllib

## how to run:

* first parameter:    medie/estremi (1 per orari, 2 per giornalieri, 3 per mensili)
* second parameter:   Type of time interval (Insert 4 for choose start and end of interval)
* third parameter:    start of time interval in format gg mm aaaa
* fourth parameter:   end of time interval in format gg mm aaaa

## Examples:

`sicilia.py 3 4 1 1 2012 1 1 2020`
gets monthly data from 1st January 2012 to 1st January 2020

`sicilia.py 3 4 25 12 2012 14 2 2020`
gets dayly data from 25th Dicember 2012 to 14th February 2020

## result: 

Write data in a csv file called sicilia.csv
