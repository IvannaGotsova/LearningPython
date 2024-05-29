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
labelOne.pack()

labelTwo = Label(tabTwo, text="Tab Two")
labelTwo.pack()

labelThree = Label(tabThree, text="Tab Three")
labelThree.pack()

labelFour = Label(tabFour, text="Tab Four")
labelFour.pack()

labelFive = Label(tabFive, text="Tab Five")
labelFive.pack()



windowExample.mainloop()