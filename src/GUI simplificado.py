import tkinter as tk
import tkinter as tk
from tkinter import messagebox
import numpy as np
from practica3_Biseccion import Biseccion
from practica4_Reglafalsa import Regla_Falsa
from practica5_newtonrapson import NewtonRaphson

class Ventana:
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
        self.metodo=Biseccion()
        self.metodo.pedir_polinomio()
        self.metodo.imprimir_polinomio()
        self.metodo.pedir_datos()
        self.metodo.calcular()

    def metodo_regla_falsa(self):
        self.metodo=Regla_Falsa()
        self.metodo.pedir_polinomio()
        self.metodo.imprimir_polinomio()
        self.metodo.pedir_datos()
        self.metodo.calcular()
    def metodo_newton(self):
        self.metodo=NewtonRaphson()
        self.metodo.pedir_polinomio()
        self.metodo.imprimir_polinomio()
        self.metodo.pedir_datos()
        self.metodo.calcular()


root=tk.Tk()        
GUI=Ventana(root)        
root.mainloop()