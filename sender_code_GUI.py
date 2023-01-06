import tkinter as tk
from tkinter import ttk
import mct.client
import mct.server

def onClick():
    print("text entered is : ",mc.get())
    #lambda : mct.client.server_connection(m_code)

rt = tk.Tk()
rt.title('Sending Morse Code')
rt.geometry('500x400+50+50')
rt.config(bg = 'SlateGray1')
tk.Label(rt, text = 'Type the message in the box and click connect to send.',
         fg = "black",bg = "azure",font = ('Times',16)).pack()
tk.Label(rt,bg = "SlateGray1").pack()

mc = tk.StringVar()
y = ttk.Frame(rt)
y.pack()

m_code_entry = ttk.Entry(y,textvariable = mc)
#m_code_entry.place(height = 200,width = 200)
#m_code_entry.pack(ipady = 3,ipadx = 100)
m_code_entry.pack(fill='x', expand=True,ipady = 3,ipadx = 100)
tk.Label(rt,bg = "SlateGray1").pack()



ttk.Button(rt, text = 'Connect',
           command =lambda : mct.client.server_connection(mc.get())).pack(ipady = 3,ipadx = 10)



    
rt.mainloop()
