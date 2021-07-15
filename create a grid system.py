from tkinter import *

root = Tk()  #creates a blank window

my_Label1=Label(root,text="yoo wassup")  #creating a label widget
my_Label2=Label(root,text="hey I'm tony stark welcome to stark industries")  #creating a label widget
my_Label3=Label(root,text="                                                                                                                                                  ")  #creating a label widget



my_Label1.grid(row=0, column=5) #create a grid system
my_Label2.grid(row=1, column=5) #create a grid system
my_Label3.grid(row=1, column=1) #create a grid system

root.mainloop()# keep window open,close button breaks the loop
