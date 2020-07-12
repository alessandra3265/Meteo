# lazio_web.py
lazio_web.py reads tables contained in pdf files from the Lazio region website and converts them to csv files

http://www.idrografico.regione.lazio.it/std_page.aspx-Page=bollettini.htm

##  Prerequisites:
- Camelot

## install camelot using conda:

miniconda is a package manager

1. install miniconda3:

install from : https://conda.io/en/latest/miniconda.html

2. run `conda install -c conda-forge camelot-py`

more information about how to install camelot: https://pypi.org/project/camelot-py/

## how to run lazio_web.py:

the site provides hydrological and thermometric data.

In script execution:

write ***idro*** for hydrological data or 

write ***termo*** for hydrological data

instead of parameter.

The script can work in three modes

1. specifying a parameter one year and one month:

    run `py lazio_web.py param year month`

    ### example 1:
    `py lazio_web.py idro 2004 6`

2. specifying a parameter one year: 

    run `py lazio_web.py param year `

    ### example 2:
    `py lazio_web.py idro 2007`

    returns data for all the months of the year 

3. specifying only a parameter:

    run `py lazio_web.py param year `

    ### example 3:

    `py lazio_web.py termo`

    returns data for all years

## result:

the results are saved in a csv file, one for each month, called as the chosen month, year and parameter




