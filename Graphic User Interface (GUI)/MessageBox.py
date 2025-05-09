from tkinter import *
from tkinter import messagebox


def info():
    messagebox.showinfo(title="Info", message="This is info message box!")


def warning():
    messagebox.showwarning(title="Warning", message="This is warning message box!")


def error():
    messagebox.showerror(title="Error", message="This is error message box!")


def yesNoCancel():
    messagebox.askyesnocancel(title="Yes No Cancel", message="This is yes no cancel message box!")


def askQuestion():
    messagebox.askquestion(title="Question?", message="This is question message box!")


def askRetryCancel():
    messagebox.askretrycancel(title="Retry", message="This is retry message box!")


windowExample = Tk()

buttonInfo = Button(text="Button Info", command=info, font=("Ariel", 22, "italic"), fg="blue", bg="black")
buttonInfo.pack()

buttonWarning = Button(text="Button Warning", command=warning, font=("Ariel", 22, "italic"), fg="blue", bg="black")
buttonWarning.pack()

buttonError = Button(text="Button Info", command=error, font=("Ariel", 22, "italic"), fg="blue", bg="black")
buttonError.pack()

buttonYesNoCancel = Button(text="Button Yes No Cancel", command=yesNoCancel, font=("Ariel", 22, "italic"), fg="blue", bg="black")
buttonYesNoCancel.pack()

buttonQuestion = Button(text="Button Ask Question", command=askQuestion, font=("Ariel", 22, "italic"), fg="blue", bg="black")
buttonQuestion.pack()

buttonRetry = Button(text="Button Retry", command=askRetryCancel, font=("Ariel", 22, "italic"), fg="blue", bg="black")
buttonRetry.pack()

windowExample.mainloop()