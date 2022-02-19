from tkinter import *

root_obj = Tk()

root_obj.geometry("733x434")
root_obj.minsize(733,434)
root_obj.maxsize(733,434)

pycharm_label = Label(text="hello this is pycharm powered by jetbrains")
pycharm_label.pack()

root_obj.mainloop()