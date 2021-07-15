from tkinter import *

root = Tk() #creates a blank window


#define a function to execute the button


def my_click():
    my_Label=Label(root,text="welcome to TVA")
    my_Label.pack()

my_Button = Button(root, text="click me", padx=50, command=my_click,fg="green",)#calling function using command variable

my_Button.pack() #placing widget indside the window



root.mainloop()# keep window open,close button breaks the loop
