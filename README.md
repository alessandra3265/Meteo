# Meteo

# Description:
This project collects scripts to extract meteorological data from 
the following site the following sites:

1) Site of "Aeronautica Militare": http://clima.meteoam.it/RichiestaDatiGenerica.php
go to SeleniumProject folder for details.
2) Site of "ARPA Veneto": https://www.arpa.veneto.it/bollettini/storico/Mappa_2020_TEMP.htm 
see SeleniumProject folder for details.
3) site of "Regione Lazio": http://www.idrografico.regione.lazio.it/std_page.aspx-Page=bollettini.htm
see pdf folder for details.
4) site of "Osservatorio Astronomico di Palermo": http://meteo.astropa.unipa.it/public/ 
see sicilia folder for details.

# Prerequisites:
### Python:
1. Download Python version >= 3.8 from:  https://www.python.org/downloads/
2. Make sure you add python to PATH during the installation of Python

### Install Selenium: 
1. Start a command prompt
2. change directory to python directory
3. Run `pip install selenium`

Selenium requires a ***driver*** to interface with the chosen browser. 

Firefox, for example, requires geckodriver. 

The scripts were written for the Firefox browser

The right driver is already present in the project folder seleniumProject.


selenium documentation: https://selenium-python.readthedocs.io/

### Install Beautiful Soup:
1. Start a command prompt
2. change directory to python directory
3. Run `pip install beautifulsoup4`

more information: https://pypi.org/project/beautifulsoup4/

### urllib:
1. urllib is a standard library,  you do not have to install it.


### Install robobrowser:
1. Start a command prompt
2. Run `pip install robobrowser`

robobrower's documentation: http://robobrowser.readthedocs.org/

