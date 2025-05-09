from tkinter import *

def printCommand():
    print("This is from menubar!")

windowExample = Tk()

menubar = Menu(windowExample)
windowExample.config(menu=menubar)

firstmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="First", menu=firstmenu)
firstmenu.add_command(label="one one", command=printCommand)
firstmenu.add_command(label="one two", command=printCommand)
firstmenu.add_command(label="one three", command=printCommand)

secondmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Second", menu=secondmenu)
secondmenu.add_command(label="two one", command=printCommand)
secondmenu.add_command(label="two two", command=printCommand)
secondmenu.add_command(label="two three", command=printCommand)

thirdmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Third", menu=thirdmenu)
thirdmenu.add_command(label="three one", command=printCommand)
thirdmenu.add_command(label="three two", command=printCommand)
thirdmenu.add_command(label="three three", command=printCommand)

windowExample.mainloop()