from fsicilia import query


"""
Tester della funzione query

primo parametro:    medie/estremi
secondo parametro:  Intervallo temporale
terzo parametro:    Inizio
quarto parametro:   Fine

query scrive i risultati nel file filename.csv
"""


"""
TEST 1 
"""
medie = "3"         #mensili
intervallo = "4"    #a scelta
giorno = "1" 
mese = "1"          #gennaio
anno = "2020"
giornoFine = "1" 
meseFine = "3"      #marzo
annoFine = "2020" 

query(medie, intervallo, giorno, mese, anno, giornoFine, meseFine, annoFine, "test1.csv")

"""
TEST 2
"""
medie = "1"         #orari
intervallo = "2"    #ultimi 7 giorni

query(medie, intervallo, giorno, mese, anno, giornoFine, meseFine, annoFine, "test2.csv")

"""
TEST 3 
"""
medie = "2"         #giornalieri
intervallo = "3"    #ultimi 30 giorni

query(medie, intervallo, giorno, mese, anno, giornoFine, meseFine, annoFine, "test3.csv")

