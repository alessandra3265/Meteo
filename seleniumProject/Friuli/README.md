## FiuliAll.py
FriuliAll.py is a script for the site: https://www.osmer.fvg.it/archivio.php?ln=&p=dati
of the region Friuli Venezia Giulia

to obtain information specifying  *day month year*  for daily data or

 _month year_  for montly data 

of all available meteorological stations.

## Dependencies:
- selenium
- BeautifulSoup

see: https://github.com/alessandra3265/Meteo#prerequisites.

## How to run:
After installing the dependencies:
1.  Start a command prompt
2.  write `py friuliAll.py anno mese`

Example:
 - to get monthly data for June 2020 write: 
    `py friuliAll.py 2020 6`

- to get daily data for 2nd June 2020 write: 
    `py friuliAll.py 2020 6 2`

# results:
The script write a csv file in the working directory.
