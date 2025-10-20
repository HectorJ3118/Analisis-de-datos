#Formularios 
# Los formularios se basan en interaces que tienen como finalidad
#recabar informacion del usuario.
#
#Los widgets que comunmente se ocupan son :
#
# CheckButton
# Radio Button 
# Button
# Option Menu
# Combobox
#
# Practica 2
# Realizar un formulario como se indica
#  |----------------------------   
#  |    Titulo
#  |Nombre
#  |Apellido
#  |Correo
#  |Boleta
#  |
#  |Genero mas0    fem0
#  |
#  |Turno
#  | | |  Matutino
#  | | |  Vespertino
#  |   
#  |Semestre:
#  |     |--------------|
#  |     |--------------|
#  |Fecha de nacimiento:
#  |
#  |  |------| |--------| |-------|
#  |
#  |
#  |    |-------------------------|
#  |    |           Registro      |
#  |    |-------------------------|
#  |
#  |---------------------------------------------
#  Cuando se oprima el boton registro, debera aparecer una 
#  Ventana emergente que indique 
#  a)Registro exitoso 
#  b)los datos ingresados

import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Calculadora")
root.resizable(1,1)
root.geometry("400x420")  
root.config(bg="#262628")

miframe=tk.Frame()
miframe.pack(pady=10)



def registro():
    nombre= nombre_obtenido.get()
    apellido=apellido_obtenido.get()
    genero=genero_obtenido.get()
    turno=turno_obtenido("Matutino"if turno else 'vespertino')
    fecha=f"{dia.get}/{mes.get}/{anio.get}"

    ventana_resumen=f" 
    Nombre: {nombre}
    Boleta: {Boleta}
    "
    messagebox.showinfo('Registro exitoso, los datos ingresados son :',ventana_resumen)



nombre_obtenido=tk.Entry(miframe)
nombre_obtenido.pack()

apellido_obtenido=tk.Entry(miframe)
apellido_obtenido.pack()

boton_hombre=tk.Checkbutton(miframe,variable=genero_obtenido        )
boton_mujer=tk.Checkbutton(miframe,variable=genero_obtenido         )