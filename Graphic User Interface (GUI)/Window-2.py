from tkinter import *

def printCommand():
    windowNew = Tk()
    labelNew = Label(windowNew, text="New Window")
    labelNew.pack()
    print("From new Window")
    windowExample.destroy()


windowExample = Tk()


button = Button(text="Click", command=printCommand)
button.pack()


windowExample.mainloop()