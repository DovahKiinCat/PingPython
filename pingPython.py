from tkinter import *
from tkinter import ttk
import tkinter as tk
import os

def ping():
    host_ip = host.get()
    host_ping = number.get()
    
    resposta = os.system(f'ping -n {host_ping} {host_ip}')
    
    if resposta == 0:
        respf = f'{host_ip} está ONLINE!!'
    
        resp.config(text=respf)
    elif resposta == 2 or 256 or 512:
        respf = f'{host_ip} está OFFLINE!! e não tem resposta do servidor'
    
        resp.config(text=respf)
    else:
        respf = f'{host_ip} está OFFLINE!!'
    
        resp.config(text=respf)
        
        
root = Tk()
root.title("Ping com Interface gráfica")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

host = StringVar()

ttk.Label(mainframe, text="Insira o IP ou Host").grid(column=1, row=1, sticky=W)

host_entry = ttk.Entry(mainframe, width=20, textvariable = host)
host_entry.grid(column=2, row=1, sticky=(W, E))

number = StringVar()

ttk.Label(mainframe, text="Número de Envios").grid(column=1, row=2, sticky=W)

number_ping = ttk.Combobox(mainframe, width=20,textvariable=number)
number_ping.grid(column=2, row=2, sticky=(W, E))
number_ping ['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
number_ping.current(0)

pingButton = ttk.Button(mainframe, text="Executar", command=ping, padding="10 10 10 10")
pingButton.grid(column=2, row=3, sticky=(S))

resp = ttk.Label(mainframe, text="", foreground="red")
resp.grid(column=2, row=4, sticky=(W, E))

root.geometry("800x400")
root.mainloop()