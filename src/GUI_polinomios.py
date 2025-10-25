import tkinter as tk
from tkinter import messagebox
import numpy as np
from practica3_Biseccion import Biseccion
from practica4_Reglafalsa import Regla_Falsa
from practica5_newtonrapson import NewtonRaphson




class Ventana_Principal:
    def __init__ (self,root):
        self.root=root
        self.root.title("Metodos de solucion de polinomios")
        self.root.geometry('400x300')

        tk.Label(root,text="Seleccione el metodo que quiera utilizar",font=('Arial',14)).grid(column=0,row=0)
        boton_biseccion=tk.Button(root,text='Biseccion',command=self.metodo_biseccion)
        boton_biseccion.grid(row=1,column=0)

        boton_regla_falsa=tk.Button(root,text='Regla falsa',command=self.metodo_regla_falsa)
        boton_regla_falsa.grid(row=2,column=0)

        boton_newton=tk.Button(root,text='Newton-Raphon',command=self.metodo_newton)
        boton_newton.grid(row=3,column=0)


    def metodo_biseccion(self):
        self.ventanab=tk.Tk()
        self.ventanab.title('Metodo de Biseccion')
        self.ventanab.geometry("600x400")

        tk.Label(self.ventanab,text="Ingrese el polinomio (grado y coeficiente)").pack()
        self.entrada_polinomio=tk.Entry(self.ventanab,width=50)
        self.entrada_polinomio.pack()

        tk.Label(self.ventanab,text='Limite inferior(xl): ').pack()
        self.xl=tk.Entry(self.ventanab)
        self.xl.pack()

        tk.Label(self.ventanab,text='Limite Superior(xu): ').pack()
        self.xu=tk.Entry(self.ventanab)
        self.xu.pack()

        tk.Label(self.ventanab,text='Ingrese la tolerancia: ').pack()
        self.tolerancia=tk.Entry(self.ventanab)
        self.tolerancia.pack()

        tk.Button(self.ventanab,text='Calcular',command=self.ejecutarbiseccion).pack(pady=10)
        self.texto_resultado=tk.Text(self.ventanab,height=12)
        self.texto_resultado.pack()

    def ejecutarbiseccion(self):
        try:
            texto=self.entrada_polinomio.get()
            pares=texto.split(';')
            polinomio={}
            for i in pares:
                grado,coef=i.strip('()').split(',')
                polinomio[int(grado)]=float(coef)
            xl=float(self.xl.get())
            xu=float(self.xu.get())
            tol=float(self.tolerancia.get())

            metodo=Biseccion()
            metodo.polinomio=polinomio
            metodo.xl=xl
            metodo.xu=xu
            metodo.tolerancia=tol
            resultado=metodo.calcular()

            self.texto_resultado.delete("1.0",tk.END)
            self.texto_resultado.insert(tk.END,resultado)
            
        except Exception as e:
            messagebox.showerror('Error',str(e))        

    def metodo_regla_falsa(self):
        pass
    def metodo_newton(self):
        pass    

root=tk.Tk()
ventana=Ventana_Principal(root)
root.mainloop()
