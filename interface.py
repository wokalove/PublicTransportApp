# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:34:35 2020

@author: Dell
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
import sqlite3

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master =master
        self.config(bg="black")
        self.init_window()
    def init_window(self):
        self.master.title("My app")
        self.pack(fill = BOTH, expand=1)
        label= Label(self,text="Travelling in Cracow",bg = "black",fg = "white")
        label.config(font=("Courier",34 ))
        label.pack(pady=30)
        
        load = Image.open('pociąg.jpg')
        render = ImageTk.PhotoImage(load) 
        img = Label(self,image=render)
        img.image=render
        img.place(x=100,y=140)
        
        findButton= Button(self,text= "Find connection",bg="white",command=self.secondWin)
        findButton.place(x=180, y=410)
        findButton.config(font=("AcmeFont",20))
        
        quitButton= Button(self,text= "Quit",command=self.quitFun,fg = "red",bg="white")
        quitButton.place(x=255, y= 490)
        quitButton.config(font=("AcmeFont",20))
        
    def quitFun(self):
        root.destroy()
        sys.exit()
    def secondWin(self):
        secWindow = Tk()
        secWindow.title("Connection")
        root.destroy()
        secWindow.geometry('600x600')
        secWindow.config(bg="black")
        
        connectionLabel= Label(secWindow,text="Find your connection:",bg = "black",fg = "white")
        connectionLabel.config(font=("Courier",30))
        connectionLabel.place(x= 50, y=100)
        
        fromLabel = Label(secWindow,text="From",bg = "black",fg = "white")
        fromLabel.config(font=("Courier", 30))
        fromLabel.place(x=150,y=225)
        
        fromPlace = Entry(secWindow, bd = 10)
        fromPlace.place(x=280,y=230)
        
        toLabel = Label(secWindow,text="To",bg = "black",fg = "white")
        toLabel.config(font=("Courier", 30))
        toLabel.place(x=180,y=300)
        
        toPlace = Entry(secWindow, bd = 10)
        toPlace.place(x=280,y=300)
        
        findConnection = Button(secWindow,text= "Find connection")
        findConnection.place(x=180, y=420)
        findConnection.config(font=("AcmeFont",20))
        
    def getData(self):
        # connect withe the myTable database 
        connection = sqlite3.connect("rozklady.sqlite3") 
        
        
        # cursor object 
        crsr = connection.cursor() 
        userToPlace = toPlace.get()
        
        
        # execute the command to fetch all the data from the table emp 
        crsr.execute("SELECT Name "
                     "FROM Stops WHERE Name=? COLLATE NOCASE",(userToPlace,))
          
        # store all the fetched data in the ans variable 
        ans= crsr.fetchall()  
          
        # loop to print all the data 
        for i in ans: 
            print("There is station in your db:",i) 
           
root = Tk()
root.geometry('600x600')
app = Window(root)
root.mainloop()








    




root.mainloop()