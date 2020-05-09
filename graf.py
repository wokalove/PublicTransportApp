# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:43:06 2020

@author: Dell
"""

import sqlite3
import json

connection = sqlite3.connect("rozklady.sqlite3") 
    
crsr = connection.cursor() 
numberLine=crsr.execute("SELECT DISTINCT LineName from StopDepartures ASC;")

returnNumbersLine= crsr.fetchall()  

lineNumbers=[]
for i in returnNumbersLine:
    lineNumbers.append(str(i)[2:-3])
    
#print(lineNumbers)

graf = dict()


'''
Zapis JEDNOKROTNY słownika do pliku: {nr liniii: kolejne przystanki}
for line in lineNumbers:
    busStop=crsr.execute("SELECT s.StopName FROM StopDepartures s JOIN variants v using(LineName) where s.LineName=? group by s.PointId order by s.No ",(line,))
    returnBusStops= crsr.fetchall()  
    graf[line]=returnBusStops
    json.dump( graf, open( 'graf.json', 'w' ,encoding='utf8'),ensure_ascii=False )
'''

#print(graf)

with open('graf.json',encoding="utf8") as json_file:
    data = json.load(json_file)

print(data)

'''
dataRead=[]
for d in data:
    dataRead.append(str(i)[2:-3])
'''
def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(str(newpath)[2:-3])
        return paths
find_all_paths(graf,"kolwiek","Nowy Kleparz")
#print(p[0])