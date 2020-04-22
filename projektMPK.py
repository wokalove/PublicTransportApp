import sqlite3 
import numpy as np


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
            
def ticketCosts():
    choice=input("Are you a student? Type 'yes' or 'no'.\n").lower()   
    try:
        if(choice == "yes"):
            cost = Traveler.journeyCosts.append(Traveler.student)
        elif(choice=="no"):
           cost= Traveler.journeyCosts.append(Traveler.adult)
        else:
            raise Error
    except Error:
        print("Wrong input, try again!")
        checkIfStudent()
    if choice in ["yes","no"]:
        finalCosts=np.sum(Traveler.journeyCosts)
        print("Your all travel costs:",finalCosts)
    
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
        print("You can reach your destination by lines:")
        print(lineNumber)
        chooseLine = checkInput(lineNumber)
        
        busStop=crsr.execute("SELECT s.StopName FROM StopDepartures s JOIN variants v using(LineName) where s.LineName=? group by s.PointId order by s.No ",(chooseLine,))
        returnBusStops= crsr.fetchall()  
        
        
        busStops=[]
        print("Bus stops leading to your destination:")
        for i in returnBusStops: 
            busStops.append(str(i)[2:-3])
        #funkcja odpowiedziala za pokazanie iloci przystanków do celu
        busStopsDisplay(busStops,inpFrom,inpTo)
        #obliczenie ceny biletu
        ticketCosts()
    else:
        print("We don't have such connection")
        
connectToData()
