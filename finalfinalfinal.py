from Tkinter import *

class EnterButton(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master
		
	def setupEnter(self):
		label = Label(self.master, text = "name : Ellen Claire Manuel", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 400)
		label2 = Label(self.master, text = "major : Computer Science", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 500)
		label3 = Label(self.master, text = "SSN : 589123689", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 600)
		
	def setupChris(self):
		label = Label(self.master, text = "name : Chris Bouton", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 400)
		label2 = Label(self.master, text = "major : Cyber Engineering", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 500)
		label3 = Label(self.master, text = "SSN : 596200833", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 600)

	def setupDavid(self):
		label = Label(self.master, text = "name : David Borgognoni ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 400)
		label2 = Label(self.master, text = "major : Computer Science", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 500)
		label3 = Label(self.master, text = "SSN : 998731652", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 600)



class Security(Frame):	
	def __int__(self, master):
		Frame.__init__(self, master)
		self.master = master

	def setup(self):
		heading = Label(self.master, text = "WELCOME TO THE MILLION DOLLAR IDEA", font = ("courier", 40, "bold"), fg = "steelblue").pack()
		
		namelabel = Label(self.master, text = "enter your name: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 200)
		passlabel = Label(self.master, text = "enter your password: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 230)
		
		name = StringVar()
		password = StringVar()
		entry_box_name = Entry(self.master, textvariable = name, width = 25, bg = "lightgreen").place(x = 260, y = 210)
		password_box_name = Entry(self.master, textvariable = password, width = 25, bg = "lightgreen").place(x = 310, y = 240)

		name.set("")

		user = Button(self.master, text = "enter", width = 25, height = 5, bg = "lightblue", command = lambda: self.correcto(name.get(), password.get())).place(x = 375, y = 500)		
		newuser = Button(self.master, text = "new user?", width = 25, height = 5, bg = "lightblue").place(x = 700, y = 500)
	
	def correcto(self, name, password):		
		logins = {"ellen" : "ecm889", "chris" : "cb65", "david" : "db885"}

		for login in logins:
		    if (name in logins and password == logins[name]):
				security = Tk()
				window = Enter(security)
				security.title("Group 6 Security System")
				security.geometry("640x640+0+0")
				if (name == "ellen"):
					window.setupEnter()
					break
				if(name == "chris"):
					window.setupChris()
					break
				elif(name == "david"):
					window.setupDavid()
					break
		

########################################################################
root = Tk()
window = Security(root)
window.setup()
root.title("Group 6 Security System")
root.geometry("1280x720+0+0")		
root.mainloop()



