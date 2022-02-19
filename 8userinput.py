from tkinter import *
import os

path = os.path.realpath(__file__)

root_obj = Tk()

def submit():
    print(f"username is {uservalue.get()}")
    print(f"password is {passvalue.get()}")

root_obj.geometry("360x240")
root_obj.title(path+"login page")

label1 = Label(root_obj, text="username")
label2 = Label(root_obj,text="password")
label1.grid()
label2.grid(row =1)


uservalue = Entry(root_obj,textvariable=StringVar())
passvalue = Entry(root_obj, textvariable= StringVar())
uservalue.grid(row=0,column=1)
passvalue.grid(row=1,column=1)

button = Button(root_obj,text="submit",command=submit)
button.grid()

root_obj.mainloop()
