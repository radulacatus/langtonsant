from Tkinter import *
from Grid import Grid
from Ant import Ant
from Rule import Rule

class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.running = True
        self.grid()
        self.create_widgets(master)
        self.grid = Grid(self.canvas, 40)
        self.ants = [Ant(20, 20, self.grid, Rule(2))]
        self.val = 0
        master.after(100, self.animation)

    def create_widgets(self, master):
        self.btn_start = Button(self, text = "Start")
        self.btn_start["text"] = "Start"
        self.btn_start["command"] = self.start
        self.btn_start.grid()
        
        self.btn_stop = Button(self)
        self.btn_stop["text"] = "Stop"
        self.btn_stop["command"] = self.stop
        self.btn_stop.grid()
        
        self.canvas = Canvas(master, height = 400, width = 500, bg="white")
        self.canvas.pack()
        self.canvas.grid()
        
    def start(self):
        self.running = True
        
    def stop(self):
        self.running = False
        
    def animation(self):
        if self.running == True:
            for ant in self.ants:
                ant.step()
            self.grid.draw()
        self.master.after(1, self.animation)
            