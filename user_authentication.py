#WE ARE CREATING AN AUTHENTICATION SYSTEM USING GUI PROGRAMME AND ALL CONCEPTS COVERED SO FAR

from tkinter import * #(we use libraries)
from tkinter import messagebox
from tkinter.simpledialog import SimpleDialog

obj=Tk() #(we use objects)
obj.title("Login Form")
obj.geometry("480x360")

def register_window():

	x=Toplevel(obj)
	x.title("Registration Form")
	x.geometry("360x240")

	Label(x,text="Registration form").grid(row=1,column=2) # (we use operators)
	Label(x,text="Username").grid(row=2,column=1) 
	Label(x,text="Password").grid(row=3,column=1)

	username_value = Entry(x,textvariable=StringVar()) # (we declare a variable)
	username_value.grid(row=2,column=2) 
	pass_value = Entry(x,textvariable=StringVar()) # (the user inputs their password)
	pass_value.grid(row=3,column=2)
	
	def msg_box(): #(we use functions)
		dlg3=SimpleDialog(obj,title="Congratuletions!", text="You have been registered successfully!",buttons=[" Ok "])
		store3=dlg3.go()
		if store3==0:
			with open("GUI_4.txt","a") as file: #(we use file handling)
				file.write(f"{username_value.get()}")
				file.write(f"{pass_value.get()}")
				file.close()
			x.destroy()

	Button(x,text="Close",command=x.destroy).grid(row=5, column=2)
	Button(x,text="Register",command=msg_box).grid(row=5,column=1)

def login():
	with open("GUI_4.txt","a") as file:
		file.write("\n")
		file.close()
		
	with open("GUI_4.txt","r") as file:
		temp = 0
		for userpass in file: #(we use loop and search)(we have used lists)
			if username_value1.get() in userpass:
				if pass_value1.get() in userpass: # (we use control flow statements)
					dlg2=SimpleDialog(obj,title="Congratulations!", text="You have logged in successfully!", buttons=[" Ok "])
					store2=dlg2.go()
					if store2==0:
						obj.destroy()

				else:
					temp = 2
			else:
				temp=1  
		if temp ==1:
			dlg=SimpleDialog(obj,title="Attention!",text="Username is not registered. Register yourself.",buttons=[" Ok ", " Cancel "])
			store=dlg.go()
			if store==0:
				register_window()
			elif store==1:
				obj.destroy()
		elif temp == 2:
			messagebox.showerror("showerror", "You have entered the wrong password.")

Label(obj,text="Login Form").grid(row=1,column=2) #we write the heading
Label(obj,text="Username").grid(row=2,column=1) # we give subheading and place them below using grid
Label(obj,text="Password").grid(row=3,column=1)

username_value1 = Entry(obj,textvariable=StringVar()) #we give text box for user input
username_value1.grid(row=2,column=2) # we place the box

pass_value1 = Entry(obj,textvariable=StringVar())
pass_value1.grid(row=3,column=2)

Button(obj,text="Login",command=login).grid(row=5,column=1) # we give buttons for submit and close and place them side-by-side
Button(obj,text="Close",command=obj.destroy).grid(row=5, column=2)
Label(obj,text="If you haven't registered.\nPlease register yourself.").grid(row=6, column=1)
Button(obj,text="Register", command=register_window).grid(row=6, column=2)

obj.mainloop()