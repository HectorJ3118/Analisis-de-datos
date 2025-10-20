import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title('Calculadora de imc')
root.geometry("250x200")

miframe=tk.Frame()
miframe.pack()


resultado_imc=tk.StringVar()
peso_kilogramos=0
altura_metros=0

def calcular_imc():
    peso=float(entradapeso.get())
    altura=float(entradaaltura.get())

    resultado=peso/altura**2

    if resultado < 18.5:
        miframe.config(bg="lightblue")
        root.config(bg='lightblue')
        print("Bajo peso")
        resultado_imc=f'El IMC es {resultado:.2f}, Peso bajo'
        messagebox.showwarning('Resultado',resultado_imc)
        
    elif resultado <25 and resultado>18.5:
        miframe.config(bg="lightgreen")
        root.config(bg='lightgreen')
        print("Normal")
        resultado_imc=f'El IMC es {resultado:.2f}, Peso Normal'
        messagebox.showinfo('Resultado',resultado_imc)
        
    elif resultado >25 and resultado<30:
        miframe.config(bg="yellow")
        root.config(bg='yellow')
        print("Sobrepeso")
        resultado_imc=f'El IMC es {resultado:.2f}, Sobrepeso'
        messagebox.showinfo('Resultado',resultado_imc)
    elif resultado >30: 
        miframe.config(bg="red")
        root.config(bg='red')     
        print("Obseidad")
        resultado_imc=f'El IMC es {resultado:.2f}, Obesidad'
        messagebox.showwarning('Resultado',resultado_imc)


labelpeso=tk.Label(miframe,text="Ingrese el peso en kg")
labelpeso.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky='we')

entradapeso=tk.Entry(miframe)
entradapeso.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky='we')

labelpeso=tk.Label(miframe,text="Ingrese la altura en metros")
labelpeso.grid(row=2, column=0, columnspan=5, padx=5, pady=5, sticky='we')

entradaaltura=tk.Entry(miframe)
entradaaltura.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky='we')

boton_calcular=tk.Button(miframe,text='Calcular IMC',command=lambda:calcular_imc())
boton_calcular.config(bd=5,relief="raised")
boton_calcular.grid(row=4,column=0, columnspan=3, padx=5, pady=5, sticky='we')




root.mainloop()