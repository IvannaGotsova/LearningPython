from tkinter import *


windowExample = Tk()

listBoxExample = Listbox(font=("Ariel", 22, "italic"), fg="blue", bg="black")
listBoxExample.pack()

listBoxExample.insert(1, "one")
listBoxExample.insert(2, "two")
listBoxExample.insert(3, "three")
listBoxExample.insert(4, "four")
listBoxExample.insert(5, "five")
listBoxExample.insert(6, "six")

windowExample.mainloop()