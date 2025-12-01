import tkinter as tk
from gaussjordan2 import GaussJordan
from tkinter import ttk
from gauss_seidel import Seidel
from jacobi import Jacobi

root = tk.Tk()
root.title("Practicas sistemas 3x3")
root.geometry("400x300")
root.configure(bg="#f4f6f8")  
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TButton",
    font=("Segoe UI", 12, "bold"),
    foreground="#ffffff",
    background="#1e3d59",
    padding=10,
    borderwidth=0,
)
style.map(
    "TButton",
    background=[("active", "#27496d"), ("disabled", "#a6a6a6")]
)


frame = tk.Frame(root, bg="#ffffff", bd=0, highlightthickness=0)
frame.place(relx=0.5, rely=0.5, anchor="center")


title = tk.Label(
    frame,
    text="Seleccione metodo de resolucion",
    font=("Segoe UI Semibold", 18),
    bg="#ffffff",
    fg="#1e3d59"
)
title.pack(pady=(0, 20))
def ejecutar_gauss():
    print("Sistema 3x3 por metodo de Gauss-Jordan\n")

    sistema = GaussJordan()
    sistema.pedir_matriz()
    sistema.imprimir_matriz()
    sistema.resolver()

def ejecutar_seidel():
    metodo=Seidel()
    metodo.ingresar_sistema()
    metodo.pedir_datos()
    metodo.mostrar_sistema()
    metodo.metodo()
def ejecutar_jacobi():
    metodo=Jacobi()
    metodo.ingresar_sistema()
    metodo.pedir_datos()
    metodo.mostrar_sistema()
    metodo.metodo()


btn1 = ttk.Button(frame, text="Gauss-Jordan",command=ejecutar_gauss)
btn2 = ttk.Button(frame, text="Gauss-Seidel",command=ejecutar_seidel)
btn3 = ttk.Button(frame, text="Jacobi",command=ejecutar_jacobi)

btn1.pack(pady=8, ipadx=10, fill="x")
btn2.pack(pady=8, ipadx=10, fill="x")
btn3.pack(pady=8, ipadx=10, fill="x")

def on_enter(e):
    e.widget.configure(style="Hover.TButton")

def on_leave(e):
    e.widget.configure(style="TButton")

style.configure(
    "Hover.TButton",
    background="#0074D9",
    foreground="#ffffff",
)

for btn in (btn1, btn2, btn3):
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()


