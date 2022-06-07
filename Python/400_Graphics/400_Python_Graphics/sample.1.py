import tkinter as tk
from graphics import *
def main():
    win=Graphwin("my circle", 100, 100)
    c= Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse()
    win.close()
    
    main()
    