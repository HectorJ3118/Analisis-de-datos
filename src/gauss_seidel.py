# ############################################################################
# **    Proyecto       : Practica , Gauss-Seidel
# **    Plataforma     : VS Code
# **    Fecha/Hora     : 10/11/2025
# **    Descripción    : Practica enfocada en el metodo de Gausss-Seidel para la resolucion
# **    de un sistema de ecuacione 3x3.           
# **    
# **   By             : Hector Jimenez
# **   contact        : hjimenezm2101@alumno.ipn.mx
#  #############################################################################

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :                       Librerias / Bibliotecas / Modulos                      |
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# +-------------------------------------------------------------------------------
# |       DEFINICION Y DESARROLLO DE CLASES O FUNCIONES DE PROGRAMADOR            |
# +-------------------------------------------------------------------------------

class Clase_Base:
    def __init__(self):
        self.x1=0
        self.x2=0
        self.x3=0
        

    def ingresar_sistema(self):
        print("Ingrese el sistema 3x3 a resolver")
        self.sistema=[]
        for i in range(3):
            print(f'Ingrese los datos de la fila {i+1}')
            self.fila = list(map(float, input(f"Fila {i+1}: ").split()))
            self.sistema.append(self.fila)
           
    def mostrar_sistema(self):
        print("\nSistema introducido:")
        print("┌                       ┐")
        print("│  x1     x2     x3     |    c   │")
        for self.fila in self.sistema:
            print(f"│ {self.fila[0]:6.4f} {self.fila[1]:6.4f} {self.fila[2]:6.4f}  | {self.fila[3]:6.4f} │")
        print("└                       ┘")
class Seidel(Clase_Base):
    def __init__(self):
        super().__init__()
        self.error=None
        self.iteracion=[]
        self.tolerancia=0.0001
        self.iteraciones=0
    def pedir_datos(self):
        self.tolerancia=float(input("Ingrese la toleracia: "))
    def metodo(self):
        self.iteraciones=0
        self.x1_anterior = self.x1
        self.x2_anterior = self.x2
        self.x3_anterior = self.x3

        print("\n--- Iteraciones del Método Gauss-Seidel ---")
        print(f"{'Iter':<5}{'x1':<10}{'x2':<10}{'x3':<10}{'Error 1(%)':<10}{'Error 2(%)':<10}{'Error 3(%)':<10}{'Error(%)':<15}")
        print("-" * 100)
        while True:
            self.iteraciones += 1
            
            x1_old, x2_old, x3_old = self.x1, self.x2, self.x3

            self.x1 = (self.sistema[0][3] - (self.sistema[0][1]*self.x2) - (self.sistema[0][2]*self.x3)) / self.sistema[0][0]
            self.x2 = (self.sistema[1][3] - (self.sistema[1][0]*self.x1) - (self.sistema[1][2]*self.x3)) / self.sistema[1][1]
            self.x3 = (self.sistema[2][3] - (self.sistema[2][0]*self.x1) - (self.sistema[2][1]*self.x2)) / self.sistema[2][2]


            if self.iteraciones == 1:
                self.error1 =self.error2 = self.error3 = self.error= 100
            else:
                self.error1 = abs((self.x1 - x1_old) / self.x1) * 100
                self.error2 = abs((self.x2 - x2_old) / self.x2) * 100
                self.error3 = abs((self.x3 - x3_old) / self.x3) * 100
                self.error=(self.error1+self.error2+self.error3)/3

            print(f"{self.iteraciones:<5}{self.x1:<10.5f}{self.x2:<10.5f}{self.x3:<10.5f}{self.error1:<12.5f}{self.error2:<12.5f}{self.error3:<12.5f}{self.error:<15.5f}{'-' if self.error is None else f'{self.error:<15.5f}'}")
            
            self.iteracion.append({
                "iter": self.iteraciones,
                "x1": self.x1,
                "x2": self.x2,
                "x3": self.x3,
                "Error 1": self.error1,
                "Error 2": self.error2,
                "Error 3": self.error3,
                "Error": self.error,
                
            })
            
            if self.iteraciones > 1 and self.error <= self.tolerancia:
                break    

        print("-"*100)
        print(f"Soluciones aproximadas: \n")   
        print(F'X1: {self.x1:.6f}') 
        print(F'X2: {self.x2:.6f}') 
        print(F'X3: {self.x3:.6f}') 
        print(f"Con un error de {self.error:.6f}% tras {self.iteraciones} iteraciones.\n")
'''
metodo=Seidel()
metodo.ingresar_sistema()
metodo.pedir_datos()
metodo.mostrar_sistema() 
metodo.metodo()
'''