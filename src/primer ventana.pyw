# ############################################################################
# **    Proyecto       : Practica 0
# **    Plataforma     : VS Code
# **
# **    Fecha/Hora     : 02/09/2025
# **    Descripción    :
# **   By             : Hector Jimenez
# **   contact        : hjimenezm2101@alumno.ipn.mx
#  #############################################################################

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :                       Librerias / Bibliotecas / Modulos                      |                       :
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# +-------------------------------------------------------------------------------
# |       DEFINICION Y DESARROLLO DE CLASES O FUNCIONES DE PROGRAMADOR            |
# +-------------------------------------------------------------------------------

import tkinter as tk
# ===============================================================================
# ||                                                                            ||
# ||        P R O G R A M A / F U N C I O N    P R I N C I P A L                ||
# ||                                                                            ||
# ===============================================================================
root=tk.Tk()


root.title("Primera ventana")
root.resizable(1,1)
root.geometry("200x300")
root.config(bg="pink")
myframe=tk.Frame()
myframe.config(bg='lightgreen')
myframe.config(width='100',height='100')

myframe.pack(anchor="center")

myframe.config(bd=45,relief="flat")




















'''
myframe.config(bd=35)
myframe.config(relief='groove')#Raised ,sunken,flat,groove,ridge
#Tarea buscar el atributo justify, a que bibilioteca, que tiene, que hace 
'''



root.mainloop()
