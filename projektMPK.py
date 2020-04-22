import sqlite3 

def checkInput(lineNumbers):
    chooseLine= input("Choose line from lines presented ABOVE:")
    print(chooseLine)
    if chooseLine not in lineNumbers:
        print("Wrong input!")
        return checkInput(lineNumbers)
    else:
        return chooseLine
    
    
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
    
    lineNumber=[]
    print("You can reach your destination by lines:")
    for i in returnNumberLine: 
        lineNumber.append(str(i)[2:-3])
    
    print(lineNumber)
    
    if not lineNumber == []:
        chooseLine = checkInput(lineNumber)
        
        busStop=crsr.execute("SELECT s.StopName FROM StopDepartures s JOIN variants v using(LineName) where s.LineName=? group by s.PointId order by s.No ",(chooseLine,))
        returnBusStops= crsr.fetchall()  
        
        
        busStops=[]
        print("Bus stops leading to your destination:")
        for i in returnBusStops: 
            busStops.append(str(i)[2:-3])
        #funkcja odpowiedziala za pokazanie iloci przystanków do celu
        busStopsDisplay(busStops,inpFrom,inpTo)
    else:
        print("We don't have such connection")
        
connectToData()