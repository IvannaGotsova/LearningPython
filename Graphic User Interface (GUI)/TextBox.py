from tkinter import *


def text():
    inputText = textExample.get('1.0',END)
    print(inputText)


windowExample = Tk()

textExample = Text(font=("Ariel", 22, "italic"), fg="blue", bg="black")
textExample.pack()

buttonText = Button(windowExample, text="Button Text", command=text, font=("colibri", 22, "italic"), fg="blue", bg="black", state="active")
buttonText.pack()


windowExample.mainloop()