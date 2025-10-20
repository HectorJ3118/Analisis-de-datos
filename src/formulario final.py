# ############################################################################
# **    Proyecto       : Practica 1, Calculadora utilizando tkinter
# **    Plataforma     : VS Code
# **    Fecha/Hora     : 22/09/2025
# **    Descripción    : Esta es la practica numero 1 de la clase de analisis de datos,
# **    donde a partir de ventanas se creo una calculadora funcional con alguna de las 
# **    funciones mas importantes.
# **   By             : Hector Jimenez
# **   contact        : hjimenezm2101@alumno.ipn.mx
#  #############################################################################

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :                       Librerias / Bibliotecas / Modulos                      |
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
import tkinter as tk
from tkinter import ttk, messagebox
# +-------------------------------------------------------------------------------
# |       DEFINICION Y DESARROLLO DE CLASES O FUNCIONES DE PROGRAMADOR            |
# +-------------------------------------------------------------------------------


root = tk.Tk()
root.title("Formulario de Registro")
root.geometry("400x600")
root.config(bg="#262628")


miframe = tk.Frame(root, bg="#262628")
miframe.pack(padx=20, pady=20, fill="both", expand=True)

genero_obtenido = tk.StringVar()
turno_obtenido = tk.StringVar()
resumen=tk.StringVar()
turno_matutino=tk.BooleanVar()
turno_vespertino=tk.BooleanVar()
def registro():
    nombre = nombre_obtenido.get()
    apellido = apellido_obtenido.get()
    correo = correo_obtenido.get()
    boleta = boleta_obtenido.get()
    genero = genero_obtenido.get()
    
    semestre = semestre_obtenido.get()
    fecha = f"{dia.get()} de {mes.get()} de {anio.get()}"
    if turno_matutino.get() and not turno_vespertino.get():
        turno='Matutino'
    elif turno_vespertino.get() and not turno_matutino.get():
        turno='Vespertino'
    elif turno_matutino.get() and turno_vespertino.get():
        turno='Ambos'
    else:
        turno='NO SELECCIONADO'
                    
    if not nombre or not apellido or not correo or not boleta or genero == "" or semestre == "Selecciona tu semestre":
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return
    
    resumen="Nombre: "+nombre_obtenido.get()+" "+apellido_obtenido.get()+"\n"+"Boleta: "+boleta_obtenido.get()+"\n"+"Genero: "+genero_obtenido.get()+"\n"+"Turno: "+turno+"\n"+"Semestre: "+semestre_obtenido.get()+"\n"+ "Fecha de nacimiento: "+dia.get()+ " de "+mes.get()+" del "+anio.get()

    messagebox.showinfo("Registro Exitoso", resumen)

titulo = tk.Label(miframe, text="Formulario de Registro",font=("Arial", 16, "bold"), fg="white", bg="#262628")
titulo.pack(pady=10)

# ===============================================================================
# ||                                                                            ||
# ||        P R O G R A M A / F U N C I O N    P R I N C I P A L                ||
# ||                                                                            ||
# ===============================================================================

tk.Label(miframe, text="Nombre:", fg="white", bg="#262628").pack(anchor="w")
nombre_obtenido = tk.Entry(miframe, width=40)
nombre_obtenido.pack(pady=2)


tk.Label(miframe, text="Apellido:", fg="white", bg="#262628").pack(anchor="w")
apellido_obtenido = tk.Entry(miframe, width=40)
apellido_obtenido.pack(pady=2)


tk.Label(miframe, text="Correo:", fg="white", bg="#262628").pack(anchor="w")
correo_obtenido = tk.Entry(miframe, width=40)
correo_obtenido.pack(pady=2)


tk.Label(miframe, text="Boleta:", fg="white", bg="#262628").pack(anchor="w")
boleta_obtenido = tk.Entry(miframe, width=40)
boleta_obtenido.pack(pady=2)


tk.Label(miframe, text="Género:", fg="white", bg="#262628").pack(anchor="w")
tk.Radiobutton(miframe, text="Masculino", variable=genero_obtenido,value="Masculino", bg="#262628", fg="white").pack(anchor="w")
tk.Radiobutton(miframe, text="Femenino", variable=genero_obtenido,value="Femenino", bg="#262628", fg="white").pack(anchor="w")


tk.Label(miframe, text="Turno:", fg="white", bg="#262628").pack(anchor="w")
tk.Checkbutton(miframe,text='Matutino',variable=turno_matutino,onvalue=True,offvalue=False,bg='#262628',fg='white').pack(anchor='w')
tk.Checkbutton(miframe,text='Vespertino',variable=turno_vespertino,onvalue=True,offvalue=False,bg='#262628',fg='white').pack(anchor='w')

tk.Label(miframe, text="Semestre:", fg="white", bg="#262628").pack(anchor="w")
semestre_obtenido = ttk.Combobox(miframe, values=[f"{i}" for i in range(1, 10)], width=37)
semestre_obtenido.set("Selecciona tu semestre")
semestre_obtenido.pack(pady=2)


tk.Label(miframe, text="Fecha de nacimiento:", fg="white", bg="#262628").pack(anchor="w")

frame_fecha = tk.Frame(miframe, bg="#262628")
frame_fecha.pack(pady=2)

dia = ttk.Combobox(frame_fecha, values=[f"{i:02}" for i in range(1, 32)], width=5)
dia.set("Día")
dia.pack(side="left", padx=2)

mes = ttk.Combobox(frame_fecha, values=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"], width=10)
mes.set("Mes")
mes.pack(side="left", padx=2)

anio = ttk.Combobox(frame_fecha, values=[str(i) for i in range(1980, 2025)], width=6)
anio.set("Año")
anio.pack(side="left", padx=2)


boton_registro = tk.Button(miframe, text="Registrar", command=registro,width=20, bg="#00b894", fg="white", font=("Arial", 12, "bold"))
boton_registro.config(bd=8,relief='raised')
boton_registro.pack(pady=15)

root.mainloop()
