from tkinter import *

windowExample  = Tk()


frameExample = Frame(windowExample, bg="blue", border=5)
frameExample.pack()

labelOne = Label(frameExample, text="Label One Example")
labelOne.pack()

labelTwo = Label(frameExample, text="Label Two Example")
labelTwo.pack()

labelThree = Label(frameExample, text="Label Three Example")
labelThree.pack()






windowExample.mainloop()