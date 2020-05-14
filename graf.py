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

queue = []

'''
#Zapis JEDNOKROTNY słownika do pliku: {nr liniii: kolejne przystanki}
for line in lineNumbers:
    busStop=crsr.execute("SELECT s.StopName FROM StopDepartures s JOIN variants v using(LineName) where s.LineName=? group by s.PointId order by s.No ",(line,))
    returnBusStops= crsr.fetchall()  
    graf[line]=returnBusStops
    json.dump( graf, open( 'graf.json', 'w' ,encoding='utf8'),ensure_ascii=False )
'''

with open('graf.json',encoding="utf8") as json_file:
    data = json.load(json_file)


#Same funckje:

def find_shortest_path(graph, start, end):
        dist = {start: [start]}
        queue.append(start)
        while queue:
            at = queue.pop(0)
            
            for next in graph[at]:
                if next not in dist:
                    dist[next] = [dist[at], next]
                    queue.append(next)
                    
        shortestWay = str(dist.get(end))
        shortestWay = shortestWay.translate({ord(i): None for i in "[]'"})
        return shortestWay
    


def path_with_correct_lines(path,graph):
    
    fullPath = {}
    
    path = path.split(', ')
    
    for i in range(len(path) - 1):
        findLn = graph[path[i]][path[i+1]]
        fullPath.update({path[i]:findLn})
    
    fullPath.update({path[i+1]:[]})
    
    return fullPath



def message(shortPath,longPath):
    print("Droga do Twojego przystanku:" , shortPath,"(droga posrednia)")
    print("\n\n")
    print("Dojedziesz tam dzięki liniom:")
    
    shortPath = shortPath.split(', ')
    shortPath = np.array(shortPath)
    From = shortPath[0]
    already = 0
    
    
    for i in range(len(shortPath)-1):
        
        
        if(already == 0):
            lines = np.intersect1d(longPath[shortPath[i]], longPath[shortPath[i+1]])
            cor = longPath[shortPath[i]]
        else:
            lines = np.intersect1d(lines, longPath[shortPath[i+1]])
            
            
        if (lines.size > 0):
            cor = lines
            already = 1
            continue
        
        already = 0
        To = shortPath[i+1]
        
        print(From," --> ",To," dzięki liniom: ",cor)
        print()
        
        From = shortPath[i+1]
            
        
def making_graph_from_file_text(text):
    
    newdict = dict()
    
    
    for key,values in text.items():       
        
        for i in range(len(values) - 1):
            first = str(values[i])
            second = str(values[i+1])
            first = first.translate({ord(i): None for i in "[]'"})
            second = second.translate({ord(i): None for i in "[]'"})
            if first != second:
                if first in newdict:
                    if second in newdict[first]:
                        newdict[first][second].append(key)
                    else:
                        newdict[first].update({second:[key]})
                else:
                    newdict.update({first:{second:[key]}})
        if second not in newdict:
            newdict.update({second:{}})
            
    return newdict


#koniec samych funkcji

#Main

newdict = making_graph_from_file_text(data)


From = input("Wpisz gdzie jestes? \n")
To = input("Dokąd chcesz się udać? \n")


shortestWay = find_shortest_path(newdict, From, To)
fullPath = path_with_correct_lines(shortestWay,newdict)
message(shortestWay,fullPath)






