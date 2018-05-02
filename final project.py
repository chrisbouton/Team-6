########################################################################
#Names: Ellen Manuel, Chris Bouton, David Borgognoni
#Date: 11 May 2018
#Description: Security System : Final Pi Project
########################################################################
from Tkinter import *

class MyTest(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def setupGUI(self):
        new = Button(self.master, text = "NEW USER")
        new.pack(fill = X)
        new.place(relx = .5, rely = .37, anchor = CENTER)

        old = Button(self.master, text = "SIGN IN")
        old.pack(fill = X)
        old.place(relx = .5, rely = .5, anchor = CENTER)        

        text = Label(self.master, text = "Welcome to DEC Security System. \n Please sign in or sign up!")
        text.place(relx = .5, rely = .029, anchor = CENTER)
        text.configure(background = "navy")
        
        
#########################################################################
window = Tk()
window.title("Security System")
window.configure(background = "navy")
t = MyTest(window)
t.setupGUI()
window.mainloop()
