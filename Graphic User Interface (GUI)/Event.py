from tkinter import *


def pressedKey(event):
    print(event.keysym)

windowExample = Tk()

windowExample.bind("<Key>", pressedKey)

windowExample.mainloop()