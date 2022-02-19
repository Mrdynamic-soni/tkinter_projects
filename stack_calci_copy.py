import sys
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

a = Tk()

frame = Frame(a)
frame.pack()

a.title('Calculator')

def clear():
    mbox = textDisplay.delete(len(textDisplay.get())-1, END)
    return
def set_text(text):
    textDisplay.insert(END, text)
    return

def clear_all():
    textDisplay.delete(0, END)
    return

def equals():
    try:
        result = eval(textDisplay.get())
    except:
        messagebox.showerror(message = 'Invalid Answer')
    clear_all()
    set_text(result)





box = StringVar()

topframe = Frame(a)
topframe.pack(side = TOP)

textDisplay = Entry(frame, textvariable = box, bd = 20, insertwidth = 1, font = 30)
textDisplay.pack(side = TOP)

button1 = Button(topframe, padx = 16, pady = 16, bd = 8, text = '1', command = lambda:set_text('1'))
button1.pack(side = LEFT)

button2 = Button(topframe, padx = 16, pady = 16, bd = 8, text = '2', command = lambda:set_text('2'))
button2.pack(side = LEFT)

button3 = Button(topframe, padx = 16, pady = 16, bd = 8, text = '3', command = lambda:set_text('3'))
button3.pack(side = LEFT)

plus = Button(topframe, padx = 16, pady = 16, bd = 8, text = '+', command = lambda:set_text('+'))
plus.pack(side = LEFT)

middleframe = Frame(a)
middleframe.pack(side = TOP)

button4 = Button(middleframe, padx = 16, pady = 16, bd = 8, text = '4', command = lambda:set_text('4'))
button4.pack(side = LEFT)

button5 = Button(middleframe, padx = 16, pady = 16, bd = 8, text = '5', command = lambda:set_text('5'))
button5.pack(side = LEFT)

button6 = Button(middleframe, padx = 16, pady = 16, bd = 8, text = '6', command = lambda:set_text('6'))
button6.pack(side = LEFT)

minus = Button(middleframe, padx = 16, pady = 16, bd = 8, text = '-', command = lambda:set_text('-'))
minus.pack(side = LEFT)

bottomframe = Frame(a)
bottomframe.pack(side = TOP)

button7 = Button(bottomframe, padx = 16, pady = 16, bd = 8, text = '7', command = lambda:set_text('7'))
button7.pack(side = LEFT)

button8 = Button(bottomframe, padx = 16, pady = 16, bd = 8, text = '8', command = lambda:set_text('8'))
button8.pack(side = LEFT)

button9 = Button(bottomframe, padx = 16, pady = 16, bd = 8, text = '9', command = lambda:set_text('9'))
button9.pack(side = LEFT)

times = Button(bottomframe, padx = 16, pady = 16, bd = 8, text = 'x', command = lambda:set_text('*'))
times.pack(side = LEFT)

morebottom = Frame(a)
morebottom.pack(side = TOP)

equals = Button(morebottom, padx = 16, pady = 16, bd = 8, text = '=', command = equals)
equals.pack(side = LEFT)

button0 = Button(morebottom, padx = 16, pady = 16, bd = 8, text = '0', command = lambda:set_text('0'))
button0.pack(side = LEFT)

clearbu = Button(morebottom, padx = 16, pady = 16, bd = 8, text = 'C', command = clear)
clearbu.pack(side = LEFT)

div = Button(morebottom, padx = 16, pady = 16, bd = 8, text = '/', command = lambda:set_text('/'))
div.pack(side = LEFT)

evenmore = Frame(a)
evenmore.pack(side = TOP)

cebut = Button(evenmore, padx = 16, pady = 16, bd = 8, text = 'CE', command = clear_all)
cebut.pack(side = LEFT)

decimal = Button(evenmore, padx = 16, pady = 16, bd = 8, text = '.', command = lambda:set_text('.'))
decimal.pack(side = LEFT)

power = Button(evenmore, padx = 16, pady = 16, bd = 8, text = '^', command = lambda:set_text('^'))
power.pack(side = LEFT)

a.mainloop


