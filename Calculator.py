from tkinter import *
import emoji


def click(event):
    lastdel = numinput.get()[:-1]
    val = event.widget.cget("text")
    if val == "=":
        if numinput.get().isdigit():
            value = float(numinput.get())
        else:
            try:
                value = eval(numin.get())
            except Exception as e:
                print(e)
                numinput.set("Error")
                numin.update()
        
        numinput.set(value)
        numin.update()

    elif val == "c":
        numinput.set(" ")
        numin.update()
    
    elif val == "<":
         numinput.set(lastdel)

    elif val == emoji.emojize("🔴"):
        quit()

    else:
        numinput.set(numinput.get()+val)
        numin.update()

root_obj = Tk()

root_obj.geometry("280x500")
root_obj.minsize(280,500)
root_obj.maxsize(280,500)

root_obj.title("Calcultor by SONI")
# root_obj.wm_iconbitmap("calc.ico")

numinput = StringVar()
numinput.set(" ")
numin = Entry(root_obj,textvariable=numinput, font="TimesnewRoman 24 ")
numin.pack(ipadx=20, ipady= 5, padx=10, pady=15, fill=X)

frame = Frame(root_obj,bg = "white" , relief= SUNKEN)
b9 = Button(frame, text="9", font="TimesnewRoman 24 ")
b9.pack(side=LEFT, pady= 10, padx=10)
b9.bind("<Button-1>", click)

b8 = Button(frame, text="8", font="TimesnewRoman 24 ")
b8.pack(side=LEFT, pady= 10, padx=10)
b8.bind("<Button-1>", click)

b7 = Button(frame, text="7", font="TimesnewRoman 24 ")
b7.pack(side=LEFT, pady= 10, padx=10)
b7.bind("<Button-1>", click)

b15 = Button(frame, text="/", font="TimesnewRoman 24 ")
b15.pack(side=LEFT, pady= 10, padx=10)
b15.bind("<Button-1>", click)

frame.pack(side = TOP)

frame1 = Frame(root_obj,bg = "white" , relief= SUNKEN)
b6 = Button(frame1, text="6", font="TimesnewRoman 24 ")
b6.pack(side=LEFT, pady= 10, padx=10)
b6.bind("<Button-1>", click)

b5 = Button(frame1, text="5", font="TimesnewRoman 24 ")
b5.pack(side=LEFT, pady= 10, padx=10)
b5.bind("<Button-1>", click)

b4 = Button(frame1, text="4", font="TimesnewRoman 24 ")
b4.pack(side=LEFT, pady= 10, padx=10)
b4.bind("<Button-1>", click)

b14 = Button(frame1, text="*", font="TimesnewRoman 24 ")
b14.pack(side=LEFT, pady= 10, padx=10)
b14.bind("<Button-1>", click)

frame1.pack(side = TOP)

frame2 = Frame(root_obj,bg = "white" , relief= SUNKEN)
b3 = Button(frame2, text="3", font="TimesnewRoman 24 ")
b3.pack(side=LEFT, pady= 10, padx=10)
b3.bind("<Button-1>", click)

b2 = Button(frame2, text="2", font="TimesnewRoman 24 ")
b2.pack(side=LEFT, pady= 10, padx=10)
b2.bind("<Button-1>", click)

b1 = Button(frame2, text="1", font="TimesnewRoman 24 ")
b1.pack(side=LEFT, pady= 10, padx=10)
b1.bind("<Button-1>", click)

b13 = Button(frame2, text="-", font="TimesnewRoman 24 ")
b13.pack(side=LEFT, pady= 10, padx=10)
b13.bind("<Button-1>", click)

frame2.pack(side = TOP)

frame3 = Frame(root_obj,bg = "white" , relief= SUNKEN)
b0 = Button(frame3, text="0", font="TimesnewRoman 24 ")
b0.pack(side=LEFT, pady= 10, padx=10)
b0.bind("<Button-1>", click)

b11 = Button(frame3, text="=", font="TimesnewRoman 24 ")
b11.pack(side=LEFT, pady= 10, padx=10)
b11.bind("<Button-1>", click)

b12 = Button(frame3, text="+", font="TimesnewRoman 24 ")
b12.pack(side=LEFT, pady= 10, padx=10)
b12.bind("<Button-1>", click)

b10 = Button(frame3, text=".", font="TimesnewRoman 24 ")
b10.pack(side=LEFT, pady= 10, padx=10)
b10.bind("<Button-1>", click)

frame3.pack(side = TOP)


frame4 = Frame(root_obj,bg = "white", relief= SUNKEN)

b16 = Button(frame4 , text="c",font="TimesnewRoman 24 ")
b16.pack(side=LEFT, padx = 10, pady =10)
b16.bind("<Button-1>",click)

b18 = Button(frame4 , text="%",font="TimesnewRoman 24 ",width=2)
b18.pack(side=LEFT, padx = 10, pady =10)
b18.bind("<Button-1>",click)

b17 = Button(frame4 , text="<",font="TimesnewRoman 24 ",width=2)
b17.pack(side=LEFT, padx = 10, pady =10)
b17.bind("<Button-1>",click)

b19 = Button(frame4 , text=emoji.emojize("🔴"),font="TimesnewRoman 24 ",width=6)
b19.pack(side=LEFT, padx = 10, pady =10)
b19.bind("<Button-1>",click)

frame4.pack(side=TOP,padx= 10)

root_obj.mainloop()