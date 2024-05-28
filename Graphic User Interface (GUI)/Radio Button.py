from tkinter import *


optionsExample = ["one", "second", "third", "fourth", "fifth", "sixth", "seventh" ]

windowExample = Tk()

variableExample = StringVar()

for i in range(len(optionsExample)):
    radioButtonExample = Radiobutton(text=optionsExample[i], variable=variableExample, value=i, padx=10, )
    radioButtonExample.pack()

windowExample.mainloop()