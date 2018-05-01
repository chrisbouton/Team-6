from Tkinter import *

root = Tk()
root.title("Group 6 Security System")
root.geometry("640x640+0+0")

heading = Label(root, text="WELCOME TO THE MILLION DOLLAR IDEA", font =("courier", 40, "bold"), fg="steelblue").pack()

label1 =Label(root, text="Enter your name: ", font = ("arial",20,"bold"), fg="black").place(x=10, y=200)

name = StringVar()
entry_box = Entry(root, textvariable=name, width=25, bg="lightgreen").place(x=280,y=210)


def do_it():
    print("Hello " + str(name.get()))

work = Button(root, text="Work", width=30, height=5, bg="lightblue", command=do_it).place(x=250, y=300)
              
root.mainloop()
