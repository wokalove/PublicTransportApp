# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:43:06 2020

@author: Dell
"""

import sqlite3
import json
from collections import deque

connection = sqlite3.connect("rozklady.sqlite3") 
    
crsr = connection.cursor() 
numberLine=crsr.execute("SELECT DISTINCT LineName from StopDepartures ASC;")

returnNumbersLine= crsr.fetchall()  

lineNumbers=[]
for i in returnNumbersLine:
    lineNumbers.append(str(i)[2:-3])
    
#print(lineNumbers)

graf = dict()


queue = []



"""
#Zapis JEDNOKROTNY słownika do pliku: {nr liniii: kolejne przystanki}
for line in lineNumbers:
    busStop=crsr.execute("SELECT s.StopName FROM StopDepartures s JOIN variants v using(LineName) where s.LineName=? group by s.PointId order by s.No ",(line,))
    returnBusStops= crsr.fetchall()  
    graf[line]=returnBusStops
    json.dump( graf, open( 'graf.json', 'w' ,encoding='utf8'),ensure_ascii=False )
"""

#print(graf)

with open('graf.json',encoding="utf8") as json_file:
    data = json.load(json_file)




'''
dataRead=[]
for d in data:
    dataRead.append(str(i)[2:-3])
'''





def find_shortest_path(graph, start, end):
        dist = {start: [start]}
        queue.append(start)
        while queue:
            at = queue.pop(0)
            
            for next in graph[at]:
                if next not in dist:
                    dist[next] = [dist[at], next]
                    queue.append(next)
        return dist.get(end)



def making_graph_from_file_text(text):
    
    newdict = dict()
    
    
    for key,values in text.items():       
        
        for i in range(len(values) - 1):
            first = str(values[i])
            second = str(values[i+1])
            first = first.translate({ord(j): None for j in "[]'"})
            second = second.translate({ord(j): None for j in "[]'"})
            if first != second:
                if first in newdict:
                    if second in newdict[first]:
                        newdict[first][second].append(key)
                    else:
                        newdict[first].update({second:[key]})
                else:
                    newdict.update({first:{second:[key]}})
        if second not in newdict:
            newdict.update({second:{second:[key]}})
            
    return newdict

newdict = making_graph_from_file_text(data)


print("siema")

print(find_shortest_path(newdict, "Aleja Róż", "Elektromontaż"))

print("elo")


