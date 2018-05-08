from Tkinter import *

root = Tk()
root.title("Group 6 Security System")
root.geometry("640x640+0+0")

heading = Label(root, text="WELCOME TO THE MILLION DOLLAR IDEA", font =("courier", 40, "bold"), fg="steelblue").pack()

name = Label(root, text="Enter your name: ", font = ("arial",20,"bold"), fg="black").place(x=10, y=200)
password = Label(root, text = "Enter your password: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 400)

name = StringVar()
entry_box_name = Entry(root, textvariable=name, width=25, bg="lightgreen").place(x=280,y=210)
entry_box_password = Entry(root, textvariable=password, width=25, bg = "lightgreen").place(x=350, y=410)


def enter():
    password = Tk()
	
	##password.title("Group 6 Security System")
	##text = Label(password, text = "Enter your four digit pin ", font = ("courier", 30), fg = "teal").pack()

	
work = Button(root, text="Enter", width=30, height=5, bg="lightblue", command = password).place(x=600, y=500)
              
root.mainloop()