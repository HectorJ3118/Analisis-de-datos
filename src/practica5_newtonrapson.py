# ############################################################################
# **    Proyecto       : Practica 4, Metodo de Newton-Raphson
# **    Plataforma     : VS Code
# **    Fecha/Hora     : 24/10/2025
# **    Descripción    : Practica acerca del metodo de Newton-Raphson para la solucion de polinomios
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
class ClaseBase:
    def __init__(self):
        self.polinomio = {}
        self.x = None
        self.fx = None
        self.fdx = None

    def pedir_polinomio(self):
        print("=== INGRESO DEL POLINOMIO ===")
        n = int(input("Ingrese el grado del polinomio: "))
        for i in range(n, -1, -1):
            coef = float(input(f"Ingrese el coeficiente de x^{i}: "))
            self.polinomio[i] = coef

    def imprimir_polinomio(self):
        print("\nPolinomio ingresado:")
        pol_str = " + ".join([f"{coef}x^{grado}" for grado, coef in sorted(self.polinomio.items(), reverse=True)])
        print("f(x) =", pol_str)

    def evaluar_polinomio(self, x):
        
        grados = sorted(self.polinomio.keys(), reverse=True)
        coeficientes = [self.polinomio[g] for g in grados]
       
        return np.polyval(coeficientes, x)


class NewtonRaphson(ClaseBase):
    def __init__(self):
        super().__init__()
        self.x0 = None
        self.xr = None
        self.error_aparente = None
        self.error_verdadero = None
        self.tolerancia = None
        self.iteraciones = []

    def pedir_datos(self):
        self.x0 = float(input("\nIngrese el valor inicial x0: "))
        self.tolerancia = float(input("Ingrese la tolerancia deseada: "))

    def calcular(self):
        
        grados = sorted(self.polinomio.keys(), reverse=True)
        coeficientes = [self.polinomio[g] for g in grados]
        
        derivada = np.polyder(coeficientes)

        xr_anterior = self.x0
        iteracion = 1

        print("\n=== ITERACIONES NEWTON-RAPHSON ===")
        print(f"{'Iter':<6}{'xr':<15}{'f(xr)':<15}{'f\'(xr)':<15}{'Error (%)':<15}")
        print("-" * 65)

        while True:
            f_xr = np.polyval(coeficientes, xr_anterior)
            fdx_xr = np.polyval(derivada, xr_anterior)

            
            if fdx_xr == 0:
                print("Error: derivada nula, no se puede continuar.")
                break

            xr = xr_anterior - (f_xr / fdx_xr)

            
            if iteracion == 1:
                self.error_aparente = None
            else:
                self.error_aparente = abs((xr - xr_anterior) / xr) * 100

            print(f"{iteracion:<6}{xr:<15.6f}{f_xr:<15.6f}{fdx_xr:<15.6f}{'-' if self.error_aparente is None else f'{self.error_aparente:<15.6f}'}")

           
            if self.error_aparente is not None and self.error_aparente <= self.tolerancia:
                break

            xr_anterior = xr
            iteracion += 1

        print("-" * 100)
        print(f"\nRaíz aproximada: {xr:.6f}")
        print(f"Iteraciones realizadas: {iteracion}")
        print(f"Error final: {self.error_aparente:.6f}%")

# ===============================================================================
# ||                                                                            ||
# ||        P R O G R A M A / F U N C I O N    P R I N C I P A L                ||
# ||                                                                            ||
# ===============================================================================  
'''
metodo = NewtonRaphson()
metodo.pedir_polinomio()
metodo.imprimir_polinomio()
metodo.pedir_datos()
metodo.calcular()
'''