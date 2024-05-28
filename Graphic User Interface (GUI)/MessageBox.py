from tkinter import *
from tkinter import messagebox


def click():
    messagebox.showinfo(title="Title", message="This is message box!")


windowExample = Tk()

buttonExample = Button(text="Button Example", command=click, font=("Ariel", 22, "italic"), fg="blue", bg="black")
buttonExample.pack()

windowExample.mainloop()