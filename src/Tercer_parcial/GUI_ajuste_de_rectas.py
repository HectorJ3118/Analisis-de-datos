import tkinter as tk
import subprocess 
from tkinter import ttk
import  threading
import sys
import os

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
def ejecutar_minimos_cuadrados():
    
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_programa = os.path.join(carpeta_actual, "minimoscuadrados.py")
    subprocess.Popen([sys.executable, ruta_programa])
def ejecutar_diferencias_divididas():
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_programa = os.path.join(carpeta_actual, "diferencias_divididas.py")
    subprocess.Popen([sys.executable, ruta_programa])
def ejecutar_lagrange():
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_programa = os.path.join(carpeta_actual, "interpolacion_lagrange.py")
    subprocess.Popen([sys.executable, ruta_programa])



def minimos_cuadrados():
    threading.Thread(target=ejecutar_minimos_cuadrados, daemon=True).start()

def diferencias_divididas():
    threading.Thread(target=ejecutar_diferencias_divididas, daemon=True).start()
    
def lagrange():
    threading.Thread(target=ejecutar_lagrange, daemon=True).start()
   


btn1 = ttk.Button(frame, text="Minimos Cuadrados",command=minimos_cuadrados)
btn2 = ttk.Button(frame, text="Diferencias Divididas",command=diferencias_divididas)
btn3 = ttk.Button(frame, text="Lagrange",command=lagrange)

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


