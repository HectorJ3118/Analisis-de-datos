import tkinter as tk


root = tk.Tk()
root.title("Ejemplo de uso de justify")
root.geometry("300x300")

texto = '''Texto
de ejemplo para el atributo
justify de tkinter'''

'''
label_izq = tk.Label(root,anchor="center",text=texto, justify="left", bg="lightblue", width=30)
label_izq.pack(expand=True)
'''

'''
label_centro = tk.Label(root,text=texto, justify="center", bg="green", width=30)
label_centro.pack(expand=True)
'''




label_der = tk.Label(text=texto, justify="right", bg="pink", width=30)
label_der.pack(expand=True)




























root.mainloop()
