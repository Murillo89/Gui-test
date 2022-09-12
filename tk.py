from tkinter import * 
from tkinter.ttk import *
import time

from time import strftime


root = Tk()
root.title("clock")

root.geometry("700x800")

message = Label(root, text="Hello World")
message.pack()


def time():
  string = strftime("%H:%M:%S")
  lbl.config(text = string)
  lbl.after(1000, time)

lbl = Label(root, font = ("calibru", 40, "bold"),
    background = "purple",
    foreground = "white")

lbl.pack(anchor = "center")
time()

root.mainloop()

