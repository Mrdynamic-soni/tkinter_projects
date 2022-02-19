from tkinter import *

obj_root = Tk()

#geometry of gui while starting the program
obj_root.geometry("720x480")

#max size of window
obj_root.maxsize(1280,720)

#min soze of window
obj_root.minsize(360,270)

#puttng a label
label_show = Label(text="This is how you can put label into a python Tkinter GUI")

#packing of label to show in GUI window
label_show.pack()

#starting the gui window
obj_root.mainloop()