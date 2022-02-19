from tkinter import *
import os


path = os.path.realpath(__file__)

root_obj = Tk()

root_obj.geometry("480x360")
root_obj.title(path+"\sublimetext\project2")

def display1():
    print("this is to perform the action of printing")

def display2():
    print("this is to add something")
frame = Frame(root_obj, bg = "grey", borderwidth= 6)
frame.pack(side= TOP, fill="x", padx= 10)

button = Button(frame, text="button 1", command=display1)
button.pack(side = LEFT,padx = 10)

button2 = Button(frame, text="button 2", command=display2)
button2.pack(side = LEFT,padx = 10)

root_obj.mainloop()