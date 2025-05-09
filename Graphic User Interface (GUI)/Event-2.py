from tkinter import *


def pressedMouse(event):
    print("You pressed a button on the mouse")

windowExample = Tk()

windowExample.bind("<Button-1>", pressedMouse)
windowExample.bind("<Button-3>", pressedMouse)

windowExample.mainloop()