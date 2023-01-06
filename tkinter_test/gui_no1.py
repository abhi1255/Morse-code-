'''
import tkinter

window = tkinter.Tk("BRUH")
window.mainloop()

window.title("BRUH")

label = tkinter.Label(window, text = "hello world").pack()

window.mainloop()
'''
import tkinter
 
window = tkinter.Tk()
title = window.title("BRUH")
 
# to rename the title of the window window.title("GUI")
 
# pack is used to show the object in the window
 
label = tkinter.Label(window, text = "Hello World!").pack()
 
window.mainloop()
