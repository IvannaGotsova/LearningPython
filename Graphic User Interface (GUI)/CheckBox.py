from tkinter import *


def PrintVariable():
    print(variableExample.get())


windowExample = Tk()

variableExample = BooleanVar()

checkBoxExample = Checkbutton(text="Check Box", variable=variableExample, onvalue=True, offvalue=False,
                              command=PrintVariable, font=("Ariel", 22, "italic"), fg="blue", bg="black")
checkBoxExample.pack()

windowExample.mainloop()
