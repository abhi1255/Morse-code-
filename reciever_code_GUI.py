import tkinter as tk
from tkinter import ttk
import mct.client
import mct.server

rt = tk.Tk()
rt.title('Recieving Morse Code')
rt.geometry('500x400')
rt.config(bg = 'SlateGray1')

def morse_code():
    mr_win = tk.Toplevel(rt)
    mr_win.title("Translated Morse Code")
    mr_win.geometry('300x200')
    mr_win.config(bg = "azure2")
    
    trns = mct.server.translate()
    mr_label = tk.Label(mr_win,text = trns,fg = 'black',font = ('Times',16))
    mr_label.pack()
    

recv = tk.Button(rt, text ="Recieve",bg='pale violet red',
                 command = lambda:mct.server.client_connect(),font = ('Times', 12))
recv.config(width=20,height=2)
recv.place(x = 155, y = 45)

trns = tk.Button(rt, text ="Translate",bg='pale violet red',
                 command = morse_code,font = ('Times',12))
trns.config(width=20,height=2)
trns.place(x = 155, y = 135)

rt.mainloop()





