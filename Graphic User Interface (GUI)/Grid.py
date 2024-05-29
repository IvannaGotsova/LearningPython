from tkinter import *
from tkinter import ttk


windowExample = Tk()
tabs = ttk.Notebook(windowExample)

tabOne = ttk.Frame(tabs)
tabTwo = ttk.Frame(tabs)
tabThree = ttk.Frame(tabs)
tabFour = ttk.Frame(tabs)
tabFive = ttk.Frame(tabs)

tabs.add(tabOne, text='Tab One')
tabs.add(tabTwo, text='Tab Two')
tabs.add(tabThree, text='Tab Three')
tabs.add(tabFour, text='Tab Four')
tabs.add(tabFive, text='Tab Five')

tabs.pack(expand=1, fill="both")

labelOne = Label(tabOne, text="Tab One")
labelOne.grid(row=0, column=0, padx=20, pady=20)

labelTwo = Label(tabTwo, text="Tab Two")
labelTwo.grid(row=1, column=0, padx=20, pady=20)

labelThree = Label(tabThree, text="Tab Three")
labelThree.grid(row=2, column=0, padx=20, pady=20)

labelFour = Label(tabFour, text="Tab Four")
labelFour.grid(row=3, column=0, padx=20, pady=20)

labelFive = Label(tabFive, text="Tab Five")
labelFive.grid(row=4, column=0, padx=20, pady=20)



windowExample.mainloop()