from tkinter import *

root = Tk() #creates a blank window

#to create input box use entry widget
e = Entry(root,width=50,borderwidth=5)
e.pack()
#this get function get whateber you've typed into it
e.get()



#define a function to execute the button


def my_click():
    var="Hey wassup " + e.get()
    my_Label=Label(root,text=var)
    my_Label.pack()

my_Button = Button(root, text="Enter your name", padx=50, command=my_click,fg="green",)#calling function using command variable

my_Button.pack() #placing widget indside the window



root.mainloop()# keep window open,close button breaks the loop
