# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import *
import sys
import sqlite3 
import numpy as np

class Win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x600+300+10")
        self.master.title("My app")
        self.master.config(bg="black")
        self.master.resizable(False,False)
        
        self.frame = tk.Frame(width=1000, height=1000, background="black")
        
        self.label= tk.Label(self.master,text="Travelling in Cracow",bg = "black",fg = "white")
        self.label.pack(pady=20)
        self.label.config(font=("Courier",25))
        
        self.image= Image.open('pociąg.jpg')
        self.render= ImageTk.PhotoImage(self.image)
        self.imgLabel= tk.Label(self.master,image=self.render)
        self.imgLabel.pack(pady=20)
        
        self.butnew("Start", "2", Win2)
        self.quit = tk.Button(self.frame, text = f"Quit", command = self.close_window,height = 2, width = 10,fg="red")
        self.quit.config(font=("Courier",20))
        self.quit.pack(side=tk.TOP,pady=20)

        self.frame.pack( padx=20, pady=20)
    def butnew(self, text, number, _class):
        b=tk.Button(self.frame, text = text,height = 2, width = 10,fg="red",command= lambda: self.combineFunc(self.new_window(number, _class),self.close_window))
        b.config(font=("Courier",20))
        b.pack(side=tk.TOP)
        
        
    def new_window(self, number, _class):
        self.new = tk.Toplevel(self.master)
        _class(self.new, number) 
        
    def close_window(self):
        self.master.destroy()
        
    def connectToData():
        pass
    
    def combineFunc(self,*funcs):
        def combinedFunc(*args,**kwargs):
            for f in funcs:
                f(*args,**kwargs)
        return combinedFunc
        
class Win2(Win1):
    def __init__(self, master, number):
        self.master = master
        self.master.title("My app")
        self.master.config(bg="black")
        self.master.geometry("600x600+300+10")
        self.master.resizable(False,False)

        
        self.frame = tk.Frame(self.master,width=500, height=500, background="black")
        
        self.studentLabel= tk.Label(self.master,text="Are you a student?",bg = "black",fg = "white")
        self.studentLabel.place(x=160,y=50)
        self.studentLabel.config(font=("Courier",20))
        
        self.studentPlace = tk.Entry(self.master,bd=20)
        self.studentPlace.place(x=220,y=100)
        
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
        

        self.butnew("Find connection", "2", Win3)
        self.frame.pack( padx=50, pady=200)
        
    def new_window(self, number, _class, answers):
        self.new = tk.Toplevel(self.master)
        _class(self.new, number,answers) 
        
    def getAns(self):
        ans=[]
        ans.append(self.studentPlace.get())
        ans.append(self.fromPlace.get())
        ans.append(self.toPlace.get())
        print(ans)
        return ans

    def butnew(self, text, number, _class):
        b = tk.Button(self.master, text = text,height = 2, width = 20,fg="red",command= lambda: self.combineFunc(self.getAns(),self.new_window(number, _class,self.getAns)))
        b.config(font=("Courier",20))
        b.pack(side=tk.BOTTOM,pady=20)


class Win3(Win1):
    def __init__(self, master, number,studentAns):
        self.master = master
        self.master.geometry("600x600+300+10")
        self.master.title("My app")
        self.master.config(bg="black")
        self.master.resizable(False,False)
        self.studentAns=studentAns
        
        self.label = tk.Label(self.master)
        self.label.config(font=("Courier",25),text="Found lines",bg="black", fg="white")
        self.label.pack(pady=10)
        
        self.textLines = tk.Text(self.master,height = 2, width =40)
        self.textLines.insert(tk.INSERT,"Linie")
        self.textLines.pack(pady=10)
        
        self.labelTypeLine = tk.Label(self.master)
        self.labelTypeLine.config(font=("Courier",25),text="Type line from given above:",bg="black", fg="white")
        self.labelTypeLine.pack(pady=10)
        
        self.chooseLinePlace = tk.Entry(self.master,bd=20)
        self.chooseLinePlace.pack(pady=10)
        
        self.show = tk.Button(self.master, text = f"Show",height = 1, width = 7,fg="red", command = lambda : self.connectToData)
        self.show.place(x=400,y=200)
        self.show.config(font=("Courier",15))
        #self.show.pack(pady=10)
        
        self.textConnections = tk.Text(self.master,height = 15, width =40)
        self.textConnections.insert(tk.INSERT,"Przystanki")
        self.textConnections.pack(pady=10)
        
        self.quit = tk.Button(self.master, text = f"Quit",height = 1, width = 7,fg="red", command = self.close_window)
        self.quit.configure(font=("Courier",15))
        self.quit.place(x=250,y=530)
        
        #@staticmethod
        def connectToData(self):
            connection = sqlite3.connect("rozklady.sqlite3") 
            crsr = connection.cursor() 
            #wykonuje zapytanie w sql
            numberLine=crsr.execute("SELECT DISTINCT LineName FROM StopDepartures WHERE StopName=? AND LineName IN (SELECT LineName from StopDepartures  where StopName=?) COLLATE NOCASE",(self.studentAns[1],self.studentAns[2],))
            #zwraca wszystkie rekordy znalezione na wskutek zapytania
            returnNumberLine= crsr.fetchall()  
            #tablica do przechowywania numerów linii, które doprowadzą do celu
            lineNumber=[]
            for i in returnNumberLine:
                lineNumber.append(str(i)[2:-3])
                if not lineNumber == []:
                    print("You can reach your destination by lines:")
                    print(lineNumber)
                    return lineNumber
                    #chooseLine = checkInput(lineNumber)

       
        
root = tk.Tk()
app = Win1(root)
root.mainloop()