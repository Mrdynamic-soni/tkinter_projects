from tkinter import *
import os

path = os.path.realpath(__file__)
root_obj = Tk()

def display():
    print("Task Completed")
root_obj.geometry("360x240")
Label(root_obj, text="Welcome to SONI Travels").grid(row = 0,column=3)
name = Label(root_obj, text= "Name")
Gender = Label(root_obj, text= "Gender")
Contact = Label(root_obj, text= " Conact")
Destination = Label(root_obj, text="Destination")

name.grid(row=1,column=2)
Gender.grid(row=2,column=2)
Contact.grid(row=3,column=2)
Destination.grid(row=4,column=2)

nameval = StringVar()
genval = StringVar()
Contactval = StringVar()
destvsl = StringVar()
food = IntVar()

nameentry = Entry(root_obj,textvariable=nameval)
genentry = Entry(root_obj,textvariable=genval)
contEntry = Entry(root_obj, textvariable=Contactval)
destentr = Entry(root_obj, textvariable=destvsl)

nameentry.grid(row=1 ,column=3)
genentry.grid(row= 2,column=3)
contEntry.grid(row=3 ,column=3)
destentr.grid(row= 4,column=3)

foodservice = Checkbutton(text="do you want to prebook your meal?" ,variable=food)
foodservice.grid(row=5,column=3)

Button(root_obj, text="submit", command=display).grid(row=6,column=3)

root_obj.mainloop()