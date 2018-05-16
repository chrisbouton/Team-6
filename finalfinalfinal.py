#####################################################################################################################################################################################
#Name: Ellen Manuel, Chris Bouton, David Borgognoni
#Date: 15 May 2018
#Description: Team 6 - Security System
#####################################################################################################################################################################################

from Tkinter import *
import winsound
import time

#class that sets up different windows for each user and has information stored for each user
class EnterButton(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master
		
	#function that sets up a window for Ellen
	def setupEllen(self):
		label = Label(self.master, text = "name : Ellen Claire Manuel", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 400)
		label2 = Label(self.master, text = "major : Computer Science", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 500)
		label3 = Label(self.master, text = "SSN : 589123689", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 600)
	
	#function that sets up a window for Chris
	def setupChris(self):
		label = Label(self.master, text = "name : Chris Bouton", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 400)
		label2 = Label(self.master, text = "major : Cyber Engineering", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 500)
		label3 = Label(self.master, text = "SSN : 596200833", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 600)

	#function that sets up a window for David
	def setupDavid(self):
		label = Label(self.master, text = "name : David Borgognoni ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 400)
		label2 = Label(self.master, text = "major : Computer Science", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 500)
		label3 = Label(self.master, text = "SSN : 998731652", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 600)



#class that sets up the main window of the program// the starting window
class Security(Frame):	
	def __int__(self, master):
		Frame.__init__(self, master)
		self.master = master
	
	#setups what the window is going to look like
	def setup(self):
		#heading of the page
		heading = Label(self.master, text = "WELCOME TO THE MILLION DOLLAR IDEA", font = ("courier", 40, "bold"), fg = "steelblue").pack()
		
		#labels that tell user where to put name and password
		namelabel = Label(self.master, text = "enter your name: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 200)
		passlabel = Label(self.master, text = "enter your password: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 230)
		
		#makes name and password string variables so they can be stored and used for the buttons
		name = StringVar()
		password = StringVar()
		#entry boxes where name and password are entered to be saved and used by the button
		entry_box_name = Entry(self.master, textvariable = name, width = 25, bg = "lightgreen").place(x = 260, y = 210)
		password_box_name = Entry(self.master, textvariable = password, width = 25, bg = "lightgreen").place(x = 310, y = 240)
		
		#sets the name to a constant before something is entered
		name.set("")

		#buttons for a new user and an existing user
		#user button goes to the correcto function that tests if the name and password is correct
		#new user button goes to a new window to create a new user in the dictionary
		user = Button(self.master, text = "enter", width = 25, height = 5, bg = "lightblue", command = lambda: self.correcto(name.get(), password.get())).place(x = 375, y = 500)		
		newuser = Button(self.master, text = "new user?", width = 25, height = 5, bg = "lightblue").place(x = 700, y = 500)
	
	#correcto function linked to the user button
	def correcto(self, name, password):		
		#dictionary that stores name and password pairs for each user
		logins = {"ellen" : "ecm889", "chris" : "cb65", "david" : "db885"}
		
		#length of the sound
       		duration = 1000
        	#the frequency
       		freq = 440
        	#starting time
        	now = time.time()
        	#ending time
        	future = now + 10
		
		#checks to see if name and password match to make a new user
		for login in logins:
		    if (name in logins and password == logins[name]):
				security = Tk()
				window = EnterButton(security)
				security.title("Group 6 Security System")
				security.geometry("640x640+0+0")
				#if user is named "ellen"...
				if (name == "ellen"):
					#set up the security window with the setupEllen function in the EnterButton class
					window.setupEllen()
					#break out of this loop so it check the next name, if applicable
					break
				#if user is named "chris" ...
				if(name == "chris"):
					#set up the security window with the setupChris function in the EnterButton class
					window.setupChris()
					#break out of this loop to check the next name, if applicable
					break
				#if user is named "david" ...
				elif(name == "david"):
					#set up the security window with the setupDavid function in the EnterButton class
					window.setupDavid()
					#break out of this loop to check next name, if applicable
					break
			#if login info is incorrect
			else:
				#plays a sound that lasts for a few seconds 
				while(time.time() < future):
                    			#generates the sound
                    			winsound.Beep(freq, duration)
                    			#allows the sound to be played longer
                    			time.sleep(1)
                			#resets future to run each time incorrect info is entered
                			future = now + 10
		
#creates the root window that will act as the main window of the program// starting window of the program
root = Tk()
window = Security(root)
window.setup()
root.title("Group 6 Security System")
root.geometry("1280x720+0+0")		
root.mainloop()



