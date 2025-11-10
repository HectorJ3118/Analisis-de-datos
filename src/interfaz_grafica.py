import tkinter as tk
from tkinter import messagebox
from biseccion import Biseccion
from regla_falsa import Regla_Falsa

root=tk.Tk()
root.geometry('300x300')
root.title('Metodos')
root.resizable(0,0)

def metodo_biseccion():
    frame2=tk.Frame(root,)

def metodo_regla_falsa():
    pass



frame1=tk.Frame(root)
frame1.pack()
tk.Label(frame1,text='Selecciona el metodo que quieras utilizar').grid(row=0,column=0,columnspan=5)

boton_biseccion=tk.Button(frame1,text='Biseccion',height=5, width=15,command=metodo_biseccion)
boton_biseccion.grid(row=1,column=0,columnspan=5)

boton_regla_falsa=tk.Button(frame1,text='Regla Falsa',height=5,width=15,command=metodo_regla_falsa)
boton_regla_falsa.grid(row=2,column=0,columnspan=5)




root.mainloop()