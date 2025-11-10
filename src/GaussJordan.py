# ############################################################################
# **    Proyecto       : Practica , Metodo de Gauss Jordan
# **    Plataforma     : VS Code
# **    Fecha/Hora     : 24/10/2025
# **    Descripción    : Practica acerca del metodo de Gauss-Jordan para la solucion de una matriz 
# **                     3x3.
# **    
# **    
# **   By             : Hector Jimenez
# **   contact        : hjimenezm2101@alumno.ipn.mx
#  #############################################################################

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :                       Librerias / Bibliotecas / Modulos                      |
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
import numpy as np
# +-------------------------------------------------------------------------------
# |       DEFINICION Y DESARROLLO DE CLASES O FUNCIONES DE PROGRAMADOR            |
# +-------------------------------------------------------------------------------

class clase_Base:
    def __init__(self):
        self.matriz=[]

    def pedir_matriz(self):
        for j in range(3):
            print(f'Ingrese la fila{j+1}')
            fila = list(map(float, input(f"Fila {j+1} (3 números separados por espacio): ").split()))
            self.matriz.append(fila)
        self.matriz=np.array(self.matriz,float)   

    def imprimir_matriz(self):
        print('Matriz:\n')
        print(self.matriz)
class Gauss_Jordan(clase_Base):
    def __init__(self):
        super().__init__()
        self.n=len(self.matriz)
    def metodo(self):
        for i in range(self.n):
        # Hacer el pivote igual a 1
            self.matriz[i] = self.matriz[i] / self.matriz[i, i]
        
        # Hacer ceros en la columna i
            for j in range(self.n):
                if i != j:
                    self.matriz[j] = self.matriz[j] - self.matriz[i] * self.matriz[j, i]    
        print('Matriz reducida por el metodo de Gauss-Jordan')
        print(self.matriz)
        print("\nSoluciones del sistema:")
        for i in range(self.n):
            print(f"x{i+1} = {self.matriz[i, -1]}")

matriz=Gauss_Jordan()
matriz.pedir_matriz()
matriz.metodo()