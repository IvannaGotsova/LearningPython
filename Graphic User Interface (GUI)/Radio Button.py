from tkinter import *


optionsExample = ["one", "second", "third", "fourth", "fifth", "sixth", "seventh" ]


windowExample = Tk()

variableExample = StringVar()

for i in range(len(optionsExample)):
    radioButtonExample = Radiobutton(text=optionsExample[i], variable=variableExample, value=i, padx=10, font=("Ariel", 22, "italic"), fg="blue", bg="black")
    radioButtonExample.pack()

windowExample.mainloop()