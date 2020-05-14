# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:43:06 2020

@author: Dell
"""

import sqlite3
import json
import numpy as np

connection = sqlite3.connect("rozklady.sqlite3") 
    
crsr = connection.cursor() 
numberLine=crsr.execute("SELECT DISTINCT LineName from StopDepartures ASC;")

returnNumbersLine= crsr.fetchall()  

lineNumbers=[]
for i in returnNumbersLine:
    lineNumbers.append(str(i)[2:-3])
    
#print(lineNumbers)

graf = dict()

#Zapis JEDNOKROTNY słownika do pliku: {nr liniii: kolejne przystanki}
for line in lineNumbers:
    busStop=crsr.execute("SELECT s.StopName FROM StopDepartures s JOIN variants v using(LineName) where s.LineName=? group by s.PointId order by s.No ",(line,))
    returnBusStops= crsr.fetchall()  
    graf[line]=returnBusStops
    json.dump( graf, open( 'graf.json', 'w' ,encoding='utf8'),ensure_ascii=False )






