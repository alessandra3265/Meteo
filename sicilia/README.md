# Sicilia

Script that queries the site: http://meteo.astropa.unipa.it/public/

## Requirement:
* RoboBrowser
* urllib

## how to run:

* first parameter:    average type (1 hourly, 2 for daily, 3 monthly)
* second parameter:   Type of time interval (Insert 4 for choose start and end of interval)
* third parameter:    start of time interval in format gg mm aaaa
* fourth parameter:   end of time interval in format gg mm aaaa

## Examples:

`sicilia.py 3 4 1 1 2012 1 1 2020`
gets monthly data from 1st January 2012 to 1st January 2020

`sicilia.py 3 4 25 12 2012 14 2 2020`
gets daily data from 25th Dicember 2012 to 14th February 2020

## result: 

Write data in a csv file called sicilia.csv
