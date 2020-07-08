Dependencies
FriuliAll requires selenium library:
Detailed instructions for Windows users

1.  Install Python 3.6 using the MSI available in python.org download page.

2.  Start a command prompt using the cmd.exe program and run the pip command as given below to install selenium.

    C:\Python35\Scripts\pip.exe install selenium

Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.
Chrome: 	https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge: 	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox: 	https://github.com/mozilla/geckodriver/releases
Safari: 	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

more information: https://selenium-python.readthedocs.io/installation.html#


How to use:
1.  Start a command prompt
2.  write py friuliAll.py anno mese 
for example to get monthly data for June 2020 write: py friuliAll.py 2020 6
to get daily data for 2nd June 2020 : py friuliAll.py 2020 6 2