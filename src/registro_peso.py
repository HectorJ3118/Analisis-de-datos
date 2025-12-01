import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

ARCHIVO = "pesos.csv"

# ------------------ GUARDAR PESO ------------------
def guardar_peso():
    peso = entry_peso.get()

    try:
        peso = float(peso)
    except:
        messagebox.showerror("Error", "Ingresa un número válido")
        return

    fecha = datetime.now().strftime("%Y-%m-%d")
    nuevo = [fecha, peso]

    archivo_nuevo = not os.path.exists(ARCHIVO)

    with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        if archivo_nuevo:
            escritor.writerow(["fecha", "peso"])
        escritor.writerow(nuevo)

    messagebox.showinfo("Guardado", f"Registro: {peso} kg")
    entry_peso.delete(0, tk.END)

# ------------------ GRAFICAR ------------------
def graficar():
    fechas = []
    pesos = []

    if not os.path.exists(ARCHIVO):
        messagebox.showerror("Error", "No hay datos guardados")
        return

    with open(ARCHIVO, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            fechas.append(fila["fecha"])
            pesos.append(float(fila["peso"]))

    if not pesos:
        messagebox.showerror("Error", "No hay datos para graficar")
        return

    plt.figure()
    plt.plot(fechas, pesos, marker="o")
    plt.title("Grafica de progreso")
    plt.xlabel("Fecha")
    plt.ylabel("Peso (kg)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ------------------ INTERFAZ ------------------
ventana = tk.Tk()
ventana.title("Registro ")
ventana.geometry("400x300")
ventana.resizable(False, False)


ventana.update_idletasks()
w = 400
h = 300
x = (ventana.winfo_screenwidth() // 2) - (w // 2)
y = (ventana.winfo_screenheight() // 2) - (h // 2)
ventana.geometry(f"{w}x{h}+{x}+{y}")


style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TFrame",
    background="#1e1e2f"
)

style.configure(
    "TLabel",
    background="#1e1e2f",
    foreground="white",
    font=("Segoe UI", 12)
)

style.configure(
    "Titulo.TLabel",
    background="#1e1e2f",
    foreground="#4dd0e1",
    font=("Segoe UI", 18, "bold")
)

style.configure(
    "TButton",
    font=("Segoe UI", 12),
    padding=10,
    background="#4dd0e1"
)

style.map(
    "TButton",
    background=[("active", "#26c6da")]
)

style.configure(
    "TEntry",
    padding=5,
    font=("Segoe UI", 14)
)


frame = ttk.Frame(ventana, padding=20)
frame.pack(fill="both", expand=True)

titulo = ttk.Label(frame, text="Registro Diario", style="Titulo.TLabel")
titulo.pack(pady=10)

label = ttk.Label(frame, text="Ingresa la medicion:")
label.pack(pady=5)

entry_peso = ttk.Entry(frame, width=15, font=("Segoe UI", 14))
entry_peso.pack(pady=5)

btn_guardar = ttk.Button(frame, text="Guardar ", command=guardar_peso)
btn_guardar.pack(pady=10, fill="x")

btn_graficar = ttk.Button(frame, text="Ver grafica", command=graficar)
btn_graficar.pack(pady=5, fill="x")

ventana.mainloop()
