from Tkinter import *
##import RPi.GPIO as GPIO
##from time import sleep
###RGBS
##redPin = 12
##greenPin = 13
##bluePin = 6
##
##def blink(pin):
##    GPIO.setmode(GPIO.BCM)
##    GPIO.setup(pin, GPIO.OUT)
##    GPIO.output(pin, 1)
##
##def turnOff(pin):
##    GPIO.setmode(GPIO.BCM)
##    GPIO.setup(pin, GPIO.OUT)
##    GPIO.output(pin, 0)
    

#GUI page 1, root
root = Tk()

root.title("Group 6 Security System")

root.geometry("640x640+0+0")

heading = Label(root, text="TEAM 6'S SECURITY SYSTEM", font =("courier", 40, "bold"), fg="steelblue").pack()

##photo
##photo = PhotoImage(file="Alcatraz.PNG")
##photoLabel = Label(root, image=photo)
##photoLabel.pack()
#####USER STORAGE
users = {'name':'Chris', 'password':'Sportsman44', 'age':''}


nameLabel = Label(root, text= "Enter your name: ", font = ("arial",20,"bold"), fg="black").place(x=10, y=200)

passwordLabel = Label(root, text = "Enter your password: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 400)

##user inputs
name = StringVar()
password = StringVar()

newName = StringVar()
newPassword = StringVar()

def creation():
    #new user button, new gui called creation
    #blink(bluePin)
    creation = Tk()
    creation.title("Create New User")
    creation.geometry("640x640+0+0")
    pageTitle = Label(creation, text="Enter Unique Info to store in your own GUI!",font =("courier", 30, "bold"), fg="steelblue").pack()
    newName = Label(creation, text="Enter your name: ", font = ("arial",15,"bold"), fg="black").place(x=10, y=200)
    newPassword = Label(creation, text = "Enter your new password: ", font = ("arial", 15, "bold"), fg = "black").place(x = 10, y = 350)
    entry_box_newName = Entry(creation, textvariable=name, width=25, bg="lightgreen").place(x=250,y=210)
    entry_box_newPassword = Entry(creation, textvariable=password, width=25, bg = "lightgreen").place(x=270, y=350)
    create_button = Button(creation, text = "Create New User", width = 30, height = 5, bg = "gold").place(x = 10, y = 500)
    #userAge = Label(creation, text="Enter your age: ", font = ("arial",15,"bold"), fg="black").place(x=550, y=200)
    #userFact1 = Label(creation, text="Enter information to be securely stored: ", font = ("arial",15,"bold"), fg="black").place(x=550, y=350)
    #turnOff(bluePin)

entry_box_name = Entry(root, textvariable=name, width=25, bg="lightgreen").place(x=280,y=210)

entry_box_password = Entry(root, textvariable=password, width=25, bg = "lightgreen").place(x=350, y=410)

work = Button(root, text="Enter", width=30, height=5, bg="lightblue").place(x=600, y=500)

newUser = Button(root, text="Create New User", width =30, height = 5, bg = "lightblue", command = creation).place(x=800, y=500)            


root.mainloop()


