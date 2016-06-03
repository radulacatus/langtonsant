from Tkinter import *
from Application import Application

root = Tk()

root.title("Langton's Ant")
root.geometry("600x600")
app = Application(root)
root.mainloop()
