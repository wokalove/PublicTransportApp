# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:43:06 2020

@author: Dell
"""

import sqlite3
import json

connection = sqlite3.connect("rozklady.sqlite3") 
    
crsr = connection.cursor() 

line_numbers=[]


for (line_number,) in crsr.execute("SELECT DISTINCT LineName from StopDepartures ASC;"):
    line_numbers.append(line_number)

graf = {}
for line in line_numbers:
    for (Stopname,) in crsr.execute("SELECT s.StopName FROM StopDepartures s JOIN variants v using(LineName) where s.LineName=? group by s.PointId order by s.No ",(line,)):
        graf[line]=Stopname
        json.dump( graf, open( 'graf.json', 'w' ,encoding='utf8'),ensure_ascii=False )






