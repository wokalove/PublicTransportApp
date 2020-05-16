import sqlite3 
import numpy as np
import json

# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class Traveler:
    adult=3.40
    student=1.70
    journeyCosts=[]
def checkInput(lineNumbers):
        chooseLine= input("Choose line from lines presented ABOVE:")
    
        if chooseLine not in lineNumbers:
            print("Wrong input!")
            return checkInput(lineNumbers)
        else:
            return chooseLine          
        
def getTicketCosts():
    finalCosts=np.sum(Traveler.journeyCosts)
    return finalCosts
def ticketCosts(choice):
    #choice=input("Are you a student? Type 'yes' or 'no'.\n").lower()   
    try:
        if(choice == "yes"):
            cost = Traveler.journeyCosts.append(Traveler.student)
        elif(choice=="no"):
           cost= Traveler.journeyCosts.append(Traveler.adult)
        else:
            raise Error
    except Error:
        print("Wrong input, try again!")
        ticketCosts(choice)
    if choice in ["yes","no"]:
        finalCosts=np.sum(Traveler.journeyCosts)
    
def busStopsDisplay(busStops,inpFrom,inpTo):
    fromIndex=busStops.index(inpFrom)
    toIndex=busStops.index(inpTo)
    finalStops=[]
    
    greater = max(fromIndex,toIndex)
    smaller=min(fromIndex,toIndex)
    
    for i in range(smaller,greater+1):
         finalStops.append(busStops[i])
    if fromIndex>toIndex:
        #w przypadku gdy index danego przystanku początkowego jest większy od końcowego to odwraca listę(jazda w drugą stronę)
        print(finalStops[::-1])
    else:
        print(finalStops)
          
def connectToData():    
    connection = sqlite3.connect("rozklady.sqlite3") 
    
    crsr = connection.cursor() 
    
    inpFrom = input("Give station from:")
    inpTo = input("Give station to:")
    
    #wykonuje zapytanie w sql
    numberLine=crsr.execute("SELECT DISTINCT LineName FROM StopDepartures WHERE StopName=? AND LineName IN (SELECT LineName from StopDepartures  where StopName=?) COLLATE NOCASE",(inpFrom,inpTo,))
    #zwraca wszystkie rekordy znalezione na wskutek zapytania
    returnNumberLine= crsr.fetchall()  
    
    #tablica do przechowywania numerów linii, które doprowadzą do celu
    lineNumber=[]
    for i in returnNumberLine: 
        lineNumber.append(str(i)[2:-3])
    
    if not lineNumber == []:
        #szukanie bezporedniego połączenia między stacjami
        print("You can reach your destination by lines:")
        print(lineNumber)
        chooseLine = checkInput(lineNumber)
        
        busStop=crsr.execute("SELECT s.StopName FROM StopDepartures s JOIN variants v using(LineName) where s.LineName=? group by s.PointId order by s.No ",(chooseLine,))
        returnBusStops= crsr.fetchall()  
        
        busStops=[]
        print("Bus stops leading to your destination:")
        for i in returnBusStops: 
            busStops.append(i)
            #busStops.append(str(i)[2:-3])
        bus = [str(i)[2:-3]for i in busStops]
        print(bus)
        #funkcja odpowiedziala za pokazanie iloci przystanków do celu
        busStopsDisplay(bus,inpFrom,inpTo)
        #obliczenie ceny biletu
        choice=input("Are you a student? Type 'yes' or 'no'.\n").lower()  
        ticketCosts(choice)
        print("Final costs of your trip: {} zł".format(getTicketCosts()))
    else:
        #szukanie poredniego połączenia 
        print("Indirect connection!")
        
        with open('graf.json',encoding="utf8") as json_file:
            data = json.load(json_file)
            newdict={}
            newdict = making_graph_from_file_text(data)
            
            if all (inp not in newdict for inp in (inpFrom,inpTo)):
                print("We don't have such connection!!! Try again:")
                connectToData()
            else:
                shortestWay = find_shortest_path(newdict, inpFrom, inpTo)
                fullPath = path_with_correct_lines(shortestWay,newdict)
                message(shortestWay,fullPath,inpFrom,inpTo)


def message(shortPath,longPath,From,To):
    journeyCosts=[]
    choice=input("Are you a student? Type 'yes' or 'no'.\n").lower()   
    
    
    print("Path to your destination:" , shortPath)
    print("\n")
    print("You can reach your destination by lines:")
    
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
        lines = []
        #usuwanie duplikatów za pomocą list comprehensions
        [lines.append(x) for x in cor if x not in lines]
        already = 0
        To = shortPath[i+1]
        
        print(From," --> ",To," via lines: ",lines)
        ticketCosts(choice)
        
        print()
        
        From = shortPath[i+1]
    print("Final costs of your trip: {} zł".format(getTicketCosts()))
        
            
            
def find_shortest_path(graph, start, end):
        queue = []
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

connectToData()
