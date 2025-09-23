
import tkinter as tk
root=tk.Tk()


root.title("Primera ventana")
root.resizable(1,1)
root.geometry("200x250")
root.config(bg="pink")
miframe=tk.Frame()
miframe.config(bg='red')
miframe.config(width='150',height='150')
miframe.pack() 
miframe.config(bd=35)
miframe.config(relief='raised')
miframe.config(cursor='hand2')
root.mainloop()
'''
.pack tiene algunos atributos como
side=
fill=
expand=
'''