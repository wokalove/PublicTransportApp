import json
import sqlite3
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

class Traveler:
    '''Storing price of tickets and final journey costs. Moreover, functions 
    resposible for counting costs of journey. These aren't time tickets,
    but one-way. Prices taken from MPK Cracow website. After checking out costs
    of journey  they are cleaning in clear_costs_of_journey.'''

    FULL_PRICE = 4.60
    REDUCED_PRICE = 2.30

    def __init__(self):
        self.__journey_costs = []

    @property
    def total_cost(self):
        return sum(self.__journey_costs)

    @total_cost.setter
    def ticket_costs(self, choice):
        '''Function which count costs of journey depend on user's input.'''
        final_costs = []
        if choice == "yes":
            self.__journey_costs.append(Traveler.REDUCED_PRICE)
        elif choice == "no":
            self.__journey_costs.append(Traveler.FULL_PRICE)
        else:
            print("Wrong input, try again!")
        if choice in ["yes", "no"]:
            final_costs = sum(self.__journey_costs)
            return final_costs
        else:
            return 0.0

    def clear_costs_of_journey(self):
        self.__journey_costs.clear()

class Window1:
    ''' Class for first window - initialization of two buttons and image
        Opening next window via command called on button "Start".'''
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x600+300+10")
        self.master.title("My app")
        self.master.config(bg="black")
        self.master.resizable(False, False)
        self.background_color = "black"
        self.font_type = "Courier"

        self.frame = tk.Frame(width=1000, height=1000, 
                              background=self.background_color)

        self.label = tk.Label(self.master, text="Travelling in Cracow",
                             bg=self.background_color, fg="white")
        self.label.pack(pady=20)
        self.label.config(font=(self.font_type, 25))

        self.image = Image.open('pociąg.jpg')
        self.render = ImageTk.PhotoImage(self.image)
        self.img_label = tk.Label(self.master, image=self.render)
        self.img_label.pack(pady=20)

        self.create_new_button("Start", "2", Window2)
        self.quit = tk.Button(self.frame, 
                              text=f"Quit",
                              command=self.close_window,
                              height=2, width=10, fg="red")
        self.quit.config(font=(self.font_type, 20))

        self.quit.pack(side=tk.TOP, pady=20)
        self.frame.pack(padx=20, pady=20)

    def create_new_button(self, text, number, _class):
        ''' Creating new button with lambda expression'''
        b = tk.Button(self.frame, text=text, height=2, width=10, fg="red",
                    command=lambda: self.new_window(number, _class))
        b.config(font=("Courier", 20))
        b.pack(side=tk.TOP)

    def new_window(self, number, _class):
        ''' Creating next window after clicking on specific button'''
        self.new = tk.Toplevel(self.master)
        _class(self.new, number)

    def close_window(self):
        ''' Closing window  - function for quit button'''
        self.master.destroy()

class Window2(Window1):
    ''' Window  for users inputs'''
    def __init__(self, master, number):
        self.master = master
        self.master.title("My app")
        self.master.config(bg="black")
        self.master.geometry("600x600+300+10")
        self.master.resizable(False, False)
        self.background_color = "black"
        self.font_color = "white"
        self.font_type = "Courier"

        self.frame = tk.Frame(self.master, width=500, height=500,
                              background=self.background_color)

        self.student_label = tk.Label(self.master,
                                     text=
                                     "Are you a student?\nType 'yes' or 'no'.",
                                     bg= self.background_color, fg="white")
        self.student_label.place(x=160, y=50)
        self.student_label.config(font=(self.font_type, 20))

        self.student_place = tk.Entry(self.master,bd=20)
        self.student_place.place(x=220, y=130)

        self.connection_label = tk.Label(self.master, text="Connection",
                                        bg= self.background_color,
                                        fg= self.font_color)
        self.connection_label.place(x=180, y=200)
        self.connection_label.config(font=(self.font_type, 30))
        
        self.from_label = tk.Label(self.master, text="From:",
                                  bg= self.background_color,
                                  fg= self.font_color)
        self.from_label.place(x=100, y=280)
        self.from_label.config(font=(self.font_type, 30))
        
        self.from_place = tk.Entry(self.master, bd=20)
        self.from_place.place(x=240, y=280)

        self.to_label= tk.Label(self.master,text="To:",
                                bg= self.background_color,
                                fg= self.font_color)
        self.to_label.place(x=140, y=380)
        self.to_label.config(font=(self.font_type, 30))

        self.to_place = tk.Entry(self.master, bd=20)
        self.to_place.place(x=240, y=380)

        self.create_new_button("Find connection -->", "2", Win3)
        return_button = tk.Button(self.master, font=(self.font_type,12),
                                  text="<--- Back",height=2,
                                  width=12, fg="red",
                                  command=
                                  lambda:self.return_window(self.master))
        return_button.place(x=150, y=480)

        self.frame.pack(padx=50, pady=200)

    def new_window(self, number, _class, answers):
        '''Function overriden from base class in this case from Window1'''
        self.new = tk.Toplevel(self.master)
        _class(self.new, number,answers) 

    def return_window(self,master): 
        ''' Function which return to last window - this function is called 
        after clinking on specific button'''
        master.withdraw()

    def create_new_button(self, text, number, _class):
        ''' overriden button creating function from base class  '''
        b = tk.Button(self.master, text=text,height=2,width=20,
                      fg="red",
                      command= lambda:self.new_window(number, _class,
                                                      self.get_user_answers()))
        b.config(font=( self.font_type, 12))
        b.place(x=300, y=480)

    def show_lines(self,inp_from,inp_to,if_student):
        ''' Function which is called on button and displays 
            all stops from connect_to_data function'''
        l = tk.Label(self.master, 
                     text ="I am looking for connection..",
                     font=("Courier",12),
                     bg="white", fg="black",wraplength=600)
        text = str(self.connect_to_data(inp_from,
                                      inp_to,if_student)).replace("]","").replace("[","")
        l.config(text=text)

        if text == []:
            l.config(text="We don't have such connection!:("
                                                           ,wraplength=300,
                                                           font=
                                                           (self.font_type,12))
        l.place(x=300, y=130, anchor="center")

    def get_user_answers(self):
        ''' getting users answers from tk.Entry places'''
        answers=[]
        answers.append(self.student_place.get())
        answers.append(self.from_place.get())
        answers.append(self.to_place.get())
        
        self.label = tk.Label(self.master)
        self.label.config(font=( self.font_type, 25),
                          text="Found connection",bg="black", fg="white")
        self.label.pack(pady=20)
        print(answers)
        return answers
    
    def connect_to_data(self,inp_from,inp_to,if_student):
        ''' function responsible for connecting to database and check if journey
        is direct or indirect '''
        costs = Traveler()
        costs.clear_costs_of_journey()
        connection = sqlite3.connect("rozklady.sqlite3") 
        crsr = connection.cursor() 
        line_number=[]
        for (stops,) in crsr.execute("""SELECT DISTINCT LineName FROM StopDepartures
                                 WHERE StopName=?
                                 AND LineName IN (SELECT LineName from 
                                                  StopDepartures  where StopName=?)
                                 COLLATE NOCASE"""
                                 ,(self.studentAns[1], self.studentAns[2],)):
                                     line_number.append(stops)
        lines = [i for i in line_number]

        if line_number:
            print("You can reach your destination by lines:")
            print(lines)
            return lines
        else:
            with open('graf.json',encoding="utf8") as json_file:
                data = json.load(json_file)
                new_dict = self.making_graph_from_file_text(data)

                if all (inp not in new_dict for inp in (inp_from,inp_to)):
                    l = tk.Label(self.master,
                                 text ="We don't have such connection...",
                                 font=( self.font_type ,12),
                                 bg="white", fg="black",
                                 wraplength=600)
                    l.place(x=300, y=130, anchor="center")
                else:
                    shortest_way = find_shortest_path(new_dict, 
                                                           inp_from, inp_to)
                    fullPath = self.path_with_correct_lines(shortest_way,
                                                            new_dict)
                    self.display_bus_stops_indirect(shortest_way,fullPath,
                                                    inp_from,inp_to,if_student)

    def find_stops(self,number,inp_from,inp_to,if_student):
        ''' finding stops in direct connection and counting costs of journey'''

        choose_line = number.get()

        connection = sqlite3.connect("rozklady.sqlite3") 
        crsr = connection.cursor() 
        bus_stops=[]
        for (line,) in crsr.execute("""SELECT s.StopName FROM StopDepartures s 
                              JOIN variants v using(LineName) WHERE s.LineName=? 
                              GROUP BY s.PointId ORDER BY s.No """,
                              (choose_line,)):
            bus_stops.append(line)
        
        print("Bus stops leading to your destination:")
        '''
        for i in return_bus_stops: 
            bus_stops.append(i)
        '''
        bus = [i for i in bus_stops]

        self.bus_stops_display(bus,inp_from,inp_to)
        costs = Traveler()
        costs.ticket_costs = if_student
        
        text= 'Cost of journey:'+str('%.2f'%costs.ticket_costs)
        cost_lab = tk.Label(self.master,text=text,
                            font=( self.font_type, 12),
                            bg="black", fg="white",wraplength=300)
        cost_lab.place(x=300, y=540, anchor="center")


    def bus_stops_display(self,busStops,inpFrom,inpTo):
        ''' displaying bust stops in direct connection  there and back'''
        l = tk.Label(self.master, text = "Write down line of tram/bus!!!",
                     font=(self.font_type, 8),bg="white", fg="black")
        l.place(x=300, y=390, anchor="center")

        from_index=busStops.index(inpFrom)
        to_index=busStops.index(inpTo)
        final_stops=[]

        greater = max(from_index,to_index)
        smaller=min(from_index,to_index)
    
        for i in range(smaller,greater+1):
            final_stops.append(busStops[i])

        if from_index>to_index:
            text=str(', '.join(final_stops[::-1]))
            print(final_stops[::-1])
            l.config(text=text, wraplength=600)
        else:
            print(final_stops)
            text=str(', '.join(final_stops))
            l.config(text=text, wraplength=600)

    def making_graph_from_file_text(self,text):
        ''' Making new_dict from dictionary {nr_line: next_stops}
            from .json file new_dict are conections specific line 
            between neighboring pairs of stops'''
        new_dict = {}
        for line_number,stops in text.items():
            for i in range(len(stops) - 1):
                first = stops[i]
                second = stops[i+1]

                if first != second:
                    if first in new_dict:
                        if second in new_dict[first]:
                            new_dict[first][second].append(line_number)
                        else:
                            new_dict[first].update({second:[line_number]})
                    else:
                        new_dict.update({first:{second:[line_number]}})
            if second not in new_dict:
                new_dict.update({second:{}})

        return new_dict

    def path_with_correct_lines(self,path,graph):
        '''Updating graf with stops adding lines'''
        full_path = {}
        path = path.split(', ')

        for i in range(len(path) - 1):
            find_line = graph[path[i]][path[i+1]]
            full_path.update({path[i]:find_line})

        full_path.update({path[i+1]:[]})

        return full_path

    def display_bus_stops_indirect(self,short_path,long_path,From,To,if_student):
        ''' Displaying path of indirect connections
            with removing duplicate lines'''
        print("Path to your destination:" , short_path)
        print("\n")
        print("You can reach your destination by lines:")

        short_path = short_path.split(', ')
        short_path = np.array(short_path)
        From = short_path[0]
        already = 0
        stops=[]
        costs = Traveler()
        for i in range(len(short_path)-1):

            if(already == 0):
                lines = np.intersect1d(long_path[short_path[i]],
                                       long_path[short_path[i+1]])
                cor = long_path[short_path[i]]
            else:
                lines = np.intersect1d(lines, long_path[short_path[i+1]])

            if (lines.size > 0):
                cor = lines
                already = 1
                continue
            lines = []

            [lines.append(x) for x in cor if x not in lines]
            already = 0
            To = short_path[i+1]

            costs.ticket_costs = if_student

            text=str(From) + "-->" +str(To) +"  LINES:" + str(lines)
            stops.append(text)

            From = short_path[i+1]

        final_costs_text = str("Final costs are:") + str('%.2f'%costs.ticket_costs)
        stops.append(final_costs_text)
        text = str(stops).replace("{","").replace("}", "").replace('[',"").replace(']',"").replace('"',"")


        stopsLabel = tk.Label(self.master, 
                              text=text,
                              font=(self.font_type,20),
                              bg="black", fg="white",
                              width=200,height=200,wraplength =350)
        stopsLabel.place(x=300,y=300, anchor="center")


    def save_to_file_ONLY_ONCE(self):
        ''' Saving dictionary to file just ONCE: (line_number: next_stops) '''
        connection = sqlite3.connect("rozklady.sqlite3") 
        crsr = connection.cursor()

        line_numbers=[]
        for (line_number,) in crsr.execute(""""SELECT DISTINCT LineName
                                            from StopDepartures ASC;"""):
            line_numbers.append(line_number)

        graf = {}
        stops_to_line=[]
        for line in line_numbers:
            for (stops,) in crsr.execute("""SELECT s.StopName 
                                            FROM StopDepartures s 
                                            JOIN variants v using(LineName)
                                            where s.LineName=? group by s.PointId 
                                            order by s.No """,(line,)):
                stops_to_line.append(stops)
            graf[line]=stops_to_line
            stops_to_line=[]
            json.dump( graf, open( 'graf.json', 'w' ,encoding='utf8'),ensure_ascii=False )

class Win3(Window2):
    def __init__(self, master, number,studentAns):
        self.master = master
        self.master.geometry("600x600+300+10")
        self.master.title("My app")
        self.master.config(bg="black")
        self.master.resizable(False,False)

        self.background_color = "black"
        self.font_color = "white"
        self.font_type = "Courier"

        self.label_found = tk.Label(self.master)
        self.label_found.config(font=(self.font_type,25),
                                text="Found connections",
                                bg=self.background_color,
                                fg=self.font_color)
        self.label_found.pack(pady=10)
        self.studentAns = studentAns

        b = tk.Button(self.master, 
                      text="Show Lines",
                      command=lambda:self.show_lines(self.studentAns[1],
                                                     self.studentAns[2],
                                                     self.studentAns[0]),
                      height=1,
                      width=10,
                      fg="red",
                      bg="white")
        b.config(font=(self.font_type, 12))
        b.pack(pady=2)

        self.label_type_line = tk.Label(self.master)
        self.label_type_line.config(font=(self.font_type,25),
                                    text="Type line from given above:",
                                    bg=self.background_color,
                                    fg=self.font_color)
        self.label_type_line.place(x=40, y=150)
                
        self.choose_line_place = tk.Entry(self.master, bd=20)
        self.choose_line_place.place(x=220, y=200)

        show_button = tk.Button(self.master,
                                text = f"Show Stops",
                                height = 1, width = 10,
                                fg="red", 
                                command=
                                lambda: self.find_stops(self.choose_line_place,
                                                                self.studentAns[1],
                                                                self.studentAns[2],
                                                                self.studentAns[0]))
        show_button.place(x=400, y=210)
        show_button.config(font=(self.font_type, 15))

        self.quit_button = tk.Button(self.master,
                                     text = f"Quit",
                                     height = 1, width = 10,fg="red",
                                     command = self.close_window)
        self.quit_button.configure(font=(self.font_type, 12))
        self.quit_button.place(x=320, y=560)
        
        back_button = tk.Button(self.master,
                                font=(self.font_type, 12), 
                                text = "<--- Back",height = 1, 
                                width = 10,fg="red",
                                command= lambda:self.return_window(self.master))
        back_button.place(x=180, y=560)
        
def find_shortest_path(graph, start, end):
    ''' looking for shortest path indirect connection'''
    queue = []
    dist = {start: [start]}
    queue.append(start)
    while queue:
        at = queue.pop(0)
                
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                queue.append(next)
                        
    shortest_way = str(dist.get(end))
    shortest_way = shortest_way.translate({ord(i): None for i in "[]'"})
    print("Find_shortest_path",type(shortest_way))
    print("Graf:",graph)
    return shortest_way

def main():
    root = tk.Tk()
    Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()

