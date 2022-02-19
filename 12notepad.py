from tkinter import *
import os


root_obj = Tk()
root_obj.geometry("480x360")
root_obj.title("Untitled-Notepad")
root_obj.wm_iconbitmap("np.ico")

def new():
    pass

def New_Window():
    pass

def Open():
    pass

def saveAs():
    pass

def Print():
    pass

def Exit():
    pass
``
def undo():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def delete():
    pass

def replace():
    pass

def selectAll():
    pass

def wordrap():
    pass

def font():
    pass

def viewHelp():
    pass

def feedback():
    pass

def About():
    pass

mainMenu = Menu(root_obj)

m1= Menu(mainMenu,tearoff=0)
m1.add_command(label="New",command=new)
m1.add_command(label="New Window",command=New_Window)
m1.add_command(label="Open",command=Open)
m1.add_command(label="Save as",command=saveAs)
m1.add_command(label="Print",command=Print)
m1.add_command(label="Exit",command=root_obj.destroy)
root_obj.config(menu=mainMenu)
mainMenu.add_cascade(label="File", menu=m1)



m2= Menu(mainMenu,tearoff=0)
m2.add_command(label="Undo",command=undo)
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="paste",command=paste)
m2.add_command(label="Delete",command=delete)
m2.add_command(label="Replace",command=replace)
m2.add_command(label="Selct All", command= selectAll)
root_obj.config(menu=mainMenu)
mainMenu.add_cascade(label="Edit", menu=m2)


m3 = Menu(mainMenu,tearoff=0)
m3.add_command(label="Wordrap", command=wordrap)
m3.add_command(label="Font...", command=font)
root_obj.config(menu=mainMenu)
mainMenu.add_cascade(label="Format",menu=m3)

m4 = Menu(mainMenu,tearoff=0)
m4.add_cascade(label="view Help", command=viewHelp)
m4.add_cascade(label="Send Feedback", command=feedback)
m4.add_cascade(label="About",command=About)
root_obj.config(menu=mainMenu)
mainMenu.add_cascade(label="Help",command=help)


root_obj.mainloop()