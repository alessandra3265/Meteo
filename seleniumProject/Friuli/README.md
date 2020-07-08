## FiuliAll.py
FriuliAll.py is a script for the site: https://www.osmer.fvg.it/archivio.php?ln=&p=dati

of the region Friuli Venezia Giulia

to obtain information specifying * *day month year* * for daily data or

_ _month year_ _ for montly data 

of all available meteorological stations 

## Dependencies:
FriuliAll requires ***Selenium*** library:
Detailed instructions for Windows users

1.  Install Python 3.6 using the MSI available in python.org download page.

2.  Start a command prompt using the cmd.exe program and run the pip command as given below to install selenium.

    `C:\Python35\Scripts\pip.exe install selenium`

Selenium requires a ***driver*** to interface with the chosen browser. 
Firefox, for example, requires geckodriver, which needs to be installed before the script can be run. 
Make sure it’s in your PATH.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

Other supported browsers will have their own drivers available. 
Links to some of the more popular browser drivers follow.
Chrome:     https://sites.google.com/a/chromium.org/chromedriver/downloads

Edge: 	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox: 	https://github.com/mozilla/geckodriver/releases

Safari: 	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

more information: https://selenium-python.readthedocs.io/installation.html#


## How to run:
After installing the dependencies:
1.  Start a command prompt
2.  write `py friuliAll.py anno mese`
Example:
 to get monthly data for June 2020 write: 
 `py friuliAll.py 2020 6`

to get daily data for 2nd June 2020 write: 
`py friuliAll.py 2020 6 2`

# results:
The script write a csv file in the working directory
