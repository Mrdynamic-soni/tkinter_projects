from tkinter import *
import os

path = os.path.realpath(__file__)
root_obj = Tk()

root_obj.geometry("1280x720")

root_obj.title(path+"GUI_made_by_soni")
text_label = Label(text= '''This is tkinter GUI tutorial project, which i am learning to teach my codeyoung student,\n it's just a money thing.
\n hope no one would mind if a learn and create somthing for me to get job or intership''',bg="cyan",fg="red",padx=15,pady=30, font="TimesnewRoman 24 bold")
text_label.pack(side="top",fill=X)

root_obj.mainloop()