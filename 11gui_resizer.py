from tkinter import *
import os

root_obj = Tk()
w = 480
h = 360
def resize():
    root_obj.geometry(f"{width.get()}x{height.get()}")
    
root_obj.title(os.path.realpath(__file__))
root_obj.geometry(f"{w}x{h}")
Label(root_obj,text="GUI Window resizer",font="TimesnewRoman 16 bold").grid(row=0,column=2)

width = StringVar()
Label(root_obj,text="Width").grid(row=1,column=0)
Entry(root_obj,textvariable=width).grid(row=1,column=1)

height = StringVar()
Label(root_obj,text="Height").grid(row=2,column=0)
Entry(root_obj, textvariable=height).grid(row=2,column=1)

Button(root_obj,text="Resize",command=resize).grid(row=3,column=1)

root_obj.mainloop()


