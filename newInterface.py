# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:07:15 2020

@author: Dell
"""
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class Win1:
	def __init__(self, master):
		self.master = master
		self.master.geometry("600x600+300+10")
		self.master.title("My app")
		self.master.config(bg="black")
		self.master.resizable(False,False)
        
		self.frame = tk.Frame(width=1000, height=1000, background="black")
        
		self.label= tk.Label(self.master,text="Travelling in Cracow",bg = "black",fg = "white")
		self.label.pack(pady=10)
		self.label.config(font=("Courier",25))
        
		self.image= Image.open('pociąg.jpg')
		self.render= ImageTk.PhotoImage(self.image)
		self.imgLabel= tk.Label(self.master,image=self.render)
		self.imgLabel.place(x=100,y=50)
		self.imgLabel.pack(pady=10)
        
		self.butnew("Start", "2", Win2)
		self.quit = tk.Button(self.frame, text = f"Quit", command = self.close_window,height = 4, width = 10,fg="red")
		self.quit.pack(side=tk.TOP,pady=20)

		self.frame.pack( padx=20, pady=20)
	def butnew(self, text, number, _class):
		tk.Button(self.frame, text = text,height = 4, width = 10,fg="red",command= lambda: self.new_window(number, _class)).pack(side=tk.TOP)
        
		
	def new_window(self, number, _class):
		self.new = tk.Toplevel(self.master)
		_class(self.new, number) 
        
	def close_window(self):
		self.master.destroy()
        
class Win2(Win1):
	def __init__(self, master, number):
		self.master = master
		self.master.title("My app")
		self.master.config(bg="black")
		self.master.geometry("600x600+300+10")
		self.master.resizable(False,False)
		#Win1.master.destroy()
        
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
  
	def close_window(self):
		self.master.destroy()
	def butnew(self, text, number, _class):
		tk.Button(self.master, text = text,height = 4, width = 12,fg="blue",command= lambda: self.new_window(number, _class)).pack(side=tk.BOTTOM,pady=20)


class Win3(Win1):
	def __init__(self, master, number):
		self.master = master
		self.master.geometry("600x600+300+10")
		self.master.title("My app")
		self.master.config(bg="black")
		self.master.resizable(False,False)
        
		#self.frame = tk.Frame(self.master,width=1000, height=1000, background="black")
        
		self.label = tk.Label(self.master, text="Found connections:")
		self.label.pack(pady=10)
		self.label.config(font=("Courier",25))
        
		self.quit = tk.Button(self.master, text = f"Quit",height = 4, width = 12,fg="blue", command = self.close_window)
		self.quit.pack(pady=200)
        
		#self.frame.pack( padx=20, pady=20)
       
        
root = tk.Tk()
app = Win1(root)
root.mainloop()