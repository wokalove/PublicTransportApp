import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import numpy as np
import json

class Error(Exception):
    """Base class for exceptions"""

class Traveler:
    '''Storing price of tickets and final journey costs. Moreover, functions 
    resposible for counting costs of journey. These aren't time tickets,
    but one-way. Prices taken from MPK Cracow website.
    '''
    FULL_PRICE = 4.60
    REDUCED_PRICE = 2.30
    __journeyCosts = []

    def ticket_Costs(choice):
        '''Function which count costs of journey depend on user's input.'''
        finalCosts=[]
        if choice == "yes":
            cost = Traveler.journeyCosts.append(Traveler.REDUCED_PRICE)
        elif choice == "no":
            cost = Traveler.journeyCosts.append(Traveler.FULL_PRICE)
        else:
            print("Wrong input, try again!")
        if choice in ["yes", "no"]:
            finalCosts = sum(Traveler.journeyCosts)
        return finalCosts

    def get_Ticket_Costs():
        ''' Returninng final costs of journey'''
        finalCosts = sum(Traveler.journeyCosts)
        return finalCosts

class Window1:
    ''' Class for first window - initialization of two buttons and image
        Opening next window via command called on button "Start".
    '''
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x600+300+10")
        self.master.title("My app")
        self.master.config(bg="black")
        self.master.resizable(False, False)
        
        self.frame = tk.Frame(width=1000, height=1000, background="black")
        
        self.label= tk.Label(self.master,text="Travelling in Cracow",bg = "black",fg = "white")
        self.label.pack(pady=20)
        self.label.config(font=("Courier",25))
        
        self.image= Image.open('pociąg.jpg')
        self.render= ImageTk.PhotoImage(self.image)
        self.imgLabel= tk.Label(self.master,image=self.render)
        self.imgLabel.pack(pady=20)
        
        self.butnew("Start", "2", Window2)
        self.quit = tk.Button(self.frame, text = f"Quit", command = self.close_window,height = 2, width = 10,fg="red")
        self.quit.config(font=("Courier",20))
        
        self.quit.pack(side=tk.TOP,pady=20)
        self.frame.pack( padx=20, pady=20)

        
    def butnew(self, text, number, _class):
        ''' Creating new button with lambda expression'''
        b=tk.Button(self.frame, text = text,height = 2, width = 10,fg="red",command= lambda:self.new_window(number, _class))
        b.config(font=("Courier",20))
        b.pack(side=tk.TOP)
        
        
    def new_window(self, number, _class):
        ''' Creating next window after clicking on specific button'''
        self.new = tk.Toplevel(self.master)
        _class(self.new, number) 
        
    def close_window(self):
        ''' Closing window  - function for quit button'''
        self.master.destroy()
    
    
    def combineFunc(self,*funcs):
        ''' Function which allow us give "two commands" to one button'''
        def combinedFunc(*args,**kwargs):
            for f in funcs:
                f(*args,**kwargs)
        return combinedFunc
        
class Window2(Window1):
    def __init__(self, master, number):
        self.master = master
        self.master.title("My app")
        self.master.config(bg="black")
        self.master.geometry("600x600+300+10")
        self.master.resizable(False,False)
        
        
        self.frame = tk.Frame(self.master,width=500, height=500, background="black")
        
        self.studentLabel= tk.Label(self.master,text="Are you a student?\nType 'yes' or 'no'.",bg = "black",fg = "white")
        self.studentLabel.place(x=160,y=50)
        self.studentLabel.config(font=("Courier",20))
    
        
        self.studentPlace = tk.Entry(self.master,bd=20)
        self.studentPlace.place(x=220,y=130)
        
        self.connectionLabel= tk.Label(self.master,text="Connection",bg = "black",fg = "white")
        self.connectionLabel.place(x=180,y=200)
        self.connectionLabel.config(font=("Courier",30))        
        
        self.fromLabel= tk.Label(self.master,text="From:",bg = "black",fg = "white")
        self.fromLabel.place(x=100,y=280)
        self.fromLabel.config(font=("Courier",30))
        
        self.fromPlace = tk.Entry(self.master,bd=20)
        self.fromPlace.place(x=240,y=280)
        
        self.toLabel= tk.Label(self.master,text="To:",bg = "black",fg = "white")
        self.toLabel.place(x=140,y=380)
        self.toLabel.config(font=("Courier",30))
        
        self.toPlace = tk.Entry(self.master,bd=20)
        self.toPlace.place(x=240,y=380)
        

        self.butnew("Find connection -->", "2", Win3)
        backBtn = tk.Button(self.master,font=("Courier",12), text = "<--- Back",height = 2, width = 12,fg="red",command= lambda:self.return_window(self.master))
        backBtn.place(x=150,y=480)
        
        self.frame.pack( padx=50, pady=200)

    def new_window(self, number, _class, answers):
        '''Function overriden from base class in this case from Window1'''
        self.new = tk.Toplevel(self.master)
        _class(self.new, number,answers) 
        
    def return_window(self,master): 
        ''' Function which return to last window - this function is called after clinking on specific button'''
        master.withdraw()

        
    def butnew(self, text, number, _class):
        ''' overriden button creating function from base class  '''
        b = tk.Button(self.master, text = text,height = 2, width = 20,fg="red",command= lambda:self.new_window(number, _class,self.getAns()))
        b.config(font=("Courier",12))
        b.place(x=300,y=480)
        
    def showLines(self,inpFrom,inpTo,ifStudent):
        l1 = tk.Label(self.master, text ="I am looking for connection..",font=("Courier",12),bg="white", fg="black",wraplength=600)
        text=str(self.connectToData(inpFrom,inpTo,ifStudent)).replace("]","").replace("[","")
        l1.config( text = text)
        
        if text == []:
            l1.config(text="We don't have such connection!:(",wraplength=300,font=("Courier",12))
        l1.place(x=300,y=130, anchor="center")
        
    def getAns(self):
        ans=[]
        ans.append(self.studentPlace.get())
        ans.append(self.fromPlace.get())
        ans.append(self.toPlace.get())
        
        self.label = tk.Label(self.master)
        self.label.config(font=("Courier",25),text="Found connection",bg="black", fg="white")
        self.label.pack(pady=20)
        print(ans)
        return ans
    
    def connectToData(self,inpFrom,inpTo,ifStudent):
        Traveler.journeyCosts=[]
        connection = sqlite3.connect("rozklady.sqlite3") 

        crsr = connection.cursor() 

        #wykonuje zapytanie w sql
        numberLine=crsr.execute("SELECT DISTINCT LineName FROM StopDepartures WHERE StopName=? AND LineName IN (SELECT LineName from StopDepartures  where StopName=?) COLLATE NOCASE",(self.studentAns[1],self.studentAns[2],))
        #zwraca wszystkie rekordy znalezione na wskutek zapytania
        returnNumberLine= crsr.fetchall()  
    
        lineNumber=[]
        print(returnNumberLine)
        for i in returnNumberLine: 
            lineNumber.append(i)
        #list comprehensions do usuwania cudzysłowiów 
        lines = [str(i)[2:-3]for i in lineNumber]
        #print(lineNumber)
    
        if lineNumber:
            #szukanie bezporedniego połączenia między stacjami
            print("You can reach your destination by lines:")
            print(lines)
            return lines
        else:
            #zapis do pliku słownika {nr lini: [kolejne przystanki tej liniii]}
            with open('graf.json',encoding="utf8") as json_file:
                data = json.load(json_file)
                newdict={}
                newdict = self.makingGraphFromFileText(data)
                
                
                if all (inp not in newdict for inp in (inpFrom,inpTo)):
                    l1 = tk.Label(self.master, text ="We don't have such connection...",font=("Courier",12),bg="white", fg="black",wraplength=600)
                    l1.place(x=300,y=130, anchor="center")
                    #print("We don't have such connection!!! Try again:")
                    #self.connectToData(inpFrom,inpTo,ifStudent)
                else:
                    shortestWay = self.findShortestPath(newdict, inpFrom, inpTo)
                    fullPath = self.pathWithCorrectLines(shortestWay,newdict)
                    self.message(shortestWay,fullPath,inpFrom,inpTo,ifStudent)
                    
    
    def findStops(self,number,inpFrom,inpTo,ifStudent):
        
        chooseLine = number.get()
        
        connection = sqlite3.connect("rozklady.sqlite3") 
        crsr = connection.cursor() 

        busStop=crsr.execute("SELECT s.StopName FROM StopDepartures s JOIN variants v using(LineName) where s.LineName=? group by s.PointId order by s.No ",(chooseLine,))
        returnBusStops= crsr.fetchall()  
        
        busStops=[]
        print("Bus stops leading to your destination:")
        for i in returnBusStops: 
            busStops.append(i)
        bus = [str(i)[2:-3]for i in busStops]
        #funkcja odpowiedziala za pokazanie ilosci przystanków do celu
        self.busStopsDisplay(bus,inpFrom,inpTo)
        #obliczenie ceny biletu
        
        Traveler.ticket_Costs(ifStudent)
        
        text= 'Cost of journey:'+str(Traveler.get_Ticket_Costs())
        costLab = tk.Label(self.master, text = text,font=("Courier",12),bg="black", fg="white",wraplength=300)
        costLab.place(x=300,y=540, anchor="center")
        

    def busStopsDisplay(self,busStops,inpFrom,inpTo):
        l1 = tk.Label(self.master, text = "Write down line of tram/bus!!!",font=("Courier",8),bg="white", fg="black")
        l1.place(x=300,y=390, anchor="center")
        
        fromIndex=busStops.index(inpFrom)
        toIndex=busStops.index(inpTo)
        finalStops=[]
        
        greater = max(fromIndex,toIndex)
        smaller=min(fromIndex,toIndex)
    
        for i in range(smaller,greater+1):
            finalStops.append(busStops[i])
        if fromIndex>toIndex:
            text=str(', '.join(finalStops[::-1]))
            #w przypadku gdy index danego przystanku początkowego jest większy od końcowego to odwraca listę(jazda w drugą stronę)
            print(finalStops[::-1])
            l1.config(text=text,wraplength=600)
        else:
            print(finalStops)
            text=str(', '.join(finalStops))
            l1.config(text=text,wraplength=600)

    
    def makingGraphFromFileText(self,text):
    
        newdict = {}
        #key-line_number
        #values - stops
        for line_number,stops in text.items():
            for i in range(len(stops) - 1):
                first = str(stops[i])
                second = str(stops[i+1])
                first = first.translate({ord(i): None for i in "[]'"})
                second = second.translate({ord(i): None for i in "[]'"})
                if first != second:
                    if first in newdict:
                        if second in newdict[first]:
                            newdict[first][second].append(line_number)
                        else:
                            newdict[first].update({second:[line_number]})
                    else:
                        newdict.update({first:{second:[line_number]}})
            if second not in newdict:
                newdict.update({second:{}})
            
        return newdict

    def findShortestPath(self,graph, start, end):
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

    def pathWithCorrectLines(self,path,graph):
        
        fullPath = {}
        
        path = path.split(', ')
        
        for i in range(len(path) - 1):
            findLn = graph[path[i]][path[i+1]]
            fullPath.update({path[i]:findLn})
        
        fullPath.update({path[i+1]:[]})
        
        return fullPath
    def message(self,shortPath,longPath,From,To,ifStudent):
        #choice=input("Are you a student? Type 'yes' or 'no'.\n").lower()   
        
        
        print("Path to your destination:" , shortPath)
        print("\n")
        print("You can reach your destination by lines:")
        
        shortPath = shortPath.split(', ')
        shortPath = np.array(shortPath)
        From = shortPath[0]
        already = 0
        stops=[]
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
           
            text=str(From) + "-->" +str(To) +"VIA LINES" + str(lines)
            stops.append(text)
            Traveler.ticket_Costs(ifStudent)
            From = shortPath[i+1]
        finalCostsText = "Final costs are:" + str(Traveler.get_Ticket_Costs())
        stops.append(finalCostsText)
        text = str(stops).replace("{","").replace("}", "").replace('[',"").replace(']',"").replace('"',"")
        
        
        stopsLabel = tk.Label(self.master, text = text,font=("Courier",20),bg="black", fg="white",width=200,height=200,wraplength =450)
        stopsLabel.place(x=300,y=300, anchor="center")
    def save_to_file_ONLY_ONCE():
        ''' Saving dictionary to file just ONCE: (line_number: next_stops) '''
        connection = sqlite3.connect("rozklady.sqlite3") 
        crsr = connection.cursor() 
        numberLine=crsr.execute("SELECT DISTINCT LineName from StopDepartures ASC;")

        returnNumbersLine= crsr.fetchall()  

        lineNumbers=[]
        for i in returnNumbersLine:
            lineNumbers.append(str(i)[2:-3])

        graf = {}
        for line in lineNumbers:
            busStop=crsr.execute("SELECT s.StopName FROM StopDepartures s JOIN variants v using(LineName) where s.LineName=? group by s.PointId order by s.No ",(line,))
            returnBusStops= crsr.fetchall()  
            graf[line]=returnBusStops
            json.dump( graf, open( 'graf.json', 'w' ,encoding='utf8'),ensure_ascii=False )
        
class Win3(Window2):
    def __init__(self, master, number,studentAns):
        self.master = master
        self.master.geometry("600x600+300+10")
        self.master.title("My app")
        self.master.config(bg="black")
        self.master.resizable(False,False)
        self.studentAns=studentAns
        print("Answer:",self.studentAns)
        
        
        self.label = tk.Label(self.master)
        self.label.config(font=("Courier",25),text="Found connections",bg="black", fg="white")
        self.label.pack(pady=10)
        
        b = tk.Button(self.master, text="Show Lines", command=lambda:self.showLines(self.studentAns[1],self.studentAns[2],self.studentAns[0]),height=1,width=10,fg="red",bg="white")
        b.config(font=("Courier",12))
        b.pack(pady=2)
        
        self.labelTypeLine = tk.Label(self.master)
        self.labelTypeLine.config(font=("Courier",25),text="Type line from given above:",bg="black", fg="white")
        self.labelTypeLine.place(x=40,y=150)
                
        self.chooseLinePlace = tk.Entry(self.master,bd=20)
        self.chooseLinePlace.place(x=220,y=200)
        
 
        show = tk.Button(self.master, text = f"Show Stops",height = 1, width = 10,fg="red", command = lambda : self.findStops(self.chooseLinePlace,self.studentAns[1],self.studentAns[2],self.studentAns[0]))
        show.place(x=400,y=210)
        show.config(font=("Courier",15))
        

        self.quit = tk.Button(self.master, text = f"Quit",height = 1, width = 10,fg="red", command = self.close_window)
        self.quit.configure(font=("Courier",12))
        self.quit.place(x=320,y=560)
        
        backBtn = tk.Button(self.master,font=("Courier",12), text = "<--- Back",height = 1, width = 10,fg="red",command= lambda:self.return_window(self.master))
        backBtn.place(x=180,y=560)
        
    def close_window(self):
        root.destroy()
        

def main():
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()

                    
       
        
