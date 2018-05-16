from Tkinter import *


def correcto():
	if (name == "ellen" and password == 2486):
		ellen.Tk()
	elif (name == "chris" and password == 9968):
		chris.Tk()
	elif (name == "david" and password == 7853):
		david.Tk()
	else:
		root.Tk()


class Security(Frame):
	codes = {"ellen": 2486, "chris": 9968, "david": 7853}
	
	def __int__(self, master):
		Frame.__init__(self, master)
		self.master = master
		
	def setup(self):
		heading = Label(root, text = "WELCOME TO THE MILLION DOLLAR IDEA", font = ("courier", 40, "bold"), fg = "steelblue").pack()
		
		name = Label(root, text = "enter your name: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 200)
		password = Label(root, text = "enter your password: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 400)
		
		name = StringVar()
		entry_box_name = Entry(root, textvariable = name, width = 25, bg = "lightgreen").place(x = 280, y = 210)
		entry_box_password = Entry(root, textvariable = password, width = 25, bg = "lightgreen").place(x = 350, y = 410)
		
		user = Button(root, text = "enter", width = 25, height = 5, bg = "lightblue", command = correcto).place(x = 500, y = 500)
		newuser = Button(root, text = "new user?", width = 25, height = 5, bg = "lightblue").place(x = 700, y = 500)
	
	# def newbie():
		# pass

root = Tk()
window = Security(root)
window.setup()
root.title("Group 6 Security System")
root.geometry("640x640+0+0")		
root.mainloop()
