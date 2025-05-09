from tkinter import *


windowExample = Tk()

click = 0
def clicked():
    global click
    click += 1
    print("Clicked times: " + str(click))


buttonExample = Button(text="Button Example", font=("colibri", 22, "italic"), fg="blue", bg="black", state="disabled")
buttonExample.pack()

buttonClicked = Button(text="Button Clicked", command=clicked, font=("colibri", 22, "italic"), fg="blue", bg="black", state="active")
buttonClicked.pack()


windowExample.mainloop()