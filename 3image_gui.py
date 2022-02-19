from tkinter import *

root_obj = Tk()

root_obj.geometry("1280x720")

pic = PhotoImage(file="cal.png")

pic_label = Label(image=pic)
pic_label.pack()

root_obj.mainloop()
