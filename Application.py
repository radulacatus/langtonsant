from Tkinter import *
from Grid import Grid

class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.running = True
        self.grid()
        self.create_widgets(master)
        self.grid = Grid(self.canvas, 40)
        self.val = 0
        self.draw_every_steps = 1
        self.draw_step = 0
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
        
        self.btn_stop = Button(self)
        self.btn_stop["text"] = "Restart"
        self.btn_stop["command"] = self.restart
        self.btn_stop.grid()
        
        self.canvas = Canvas(master, height = 400, width = 500, bg="white")
        self.canvas.pack()
        self.canvas.grid()
        
    def start(self):
        self.running = True
        
    def stop(self):
        self.running = False
        
    def restart(self):
        self.grid.restart()
        self.running = True
        
    def animation(self):
        if self.running == True:
            self.grid.step_all()
            self.draw_step += 1
            if(self.draw_step >= self.draw_every_steps):
                self.draw_step = 0
                self.grid.draw()
        self.master.after(1, self.animation)
            