from tkinter import *
import os

path = os.path.realpath(__file__)
root_obj = Tk()
root_obj.geometry("1280x720")

root_obj.title(path+"sublime text/project1")

f1 = Frame(root_obj, bg = "grey",borderwidth=10, relief=SUNKEN)
f1.pack(fill = "y",side = LEFT)

f2 = Frame(root_obj, bg = "grey", borderwidth=  12, relief=SUNKEN)
f2.pack(fill="x", side = TOP)


label=  Label(f1, text="navigation bar", fg = "white",font="TimesnewRoman 16 bold", bg = "grey" )
label.pack(side =TOP)

label = Label(f2,text="wlcome to sublime text", font="TimesnewRoman 16 bold", fg = "white", bg = "grey")
label.pack()

root_obj.mainloop()