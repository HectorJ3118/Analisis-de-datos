# ############################################################################
# **    Proyecto       : Practica 3, Metodo de Biseccion
# **    Plataforma     : VS Code
# **    Fecha/Hora     : 22/09/2025
# **    Descripción    : Practica acerca del metodo de biseccion el cual calcula
# **    la raiz del polinomio que este en el rango dado por el usuario
# **    funciones mas importantes.
# **   By             : Hector Jimenez
# **   contact        : hjimenezm2101@alumno.ipn.mx
#  #############################################################################

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :                       Librerias / Bibliotecas / Modulos                      |
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# +-------------------------------------------------------------------------------
# |       DEFINICION Y DESARROLLO DE CLASES O FUNCIONES DE PROGRAMADOR            |
# +-------------------------------------------------------------------------------
class ClaseBase:
    def __init__(self):
        self.x = None
        self.fx = None
        self.fdx = None
        self.polinomio = {}  

    def pedir_polinomio(self):
        print("\n--- Ingreso del Polinomio ---")
        grado = int(input("Ingrese el grado del polinomio: "))
        for i in range(grado, -1, -1):
            coef = float(input(f"Ingrese el coeficiente de x^{i}: "))
            self.polinomio[i] = coef
        print("\nPolinomio ingresado correctamente.\n")

    def imprimir_polinomio(self):
        print("f(x) = ", end="")
        terminos = []
        for g, c in sorted(self.polinomio.items(), reverse=True):
            if c != 0:
                terminos.append(f"{c:+.2f}x^{g}")
        print(" ".join(terminos))

    def evaluar_polinomio(self, x):
        
        resultado = 0
        for g, c in self.polinomio.items():
            resultado += c * (x ** g)
        return resultado


class Biseccion(ClaseBase):
    def __init__(self):
        super().__init__()
        self.xl = None
        self.xu = None
        self.xr = None
        self.tolerancia = None
        self.error_aparente = None
        self.error_verdadero = None
        self.iteraciones = []

    def pedir_datos(self):
        print("\n--- Datos para el Método de Bisección ---")
        self.xl = float(input("Ingrese el límite inferior (xl): "))
        self.xu = float(input("Ingrese el límite superior (xu): "))
        self.tolerancia = float(input("Ingrese la tolerancia (%): "))
        print()

    def calcular(self):
        while self.evaluar_polinomio(self.xl) * self.evaluar_polinomio(self.xu) > 0:
            print("No hay cambio de signo en el intervalo o hay mas de una solucion en el intervalo. Intente con otro rango.")
            self.pedir_datos()

        iteracion = 0
        self.xr = (self.xl + self.xu) / 2
        xr_anterior = self.xr

        print("\n--- Iteraciones del Método de Bisección ---")
        print(f"{'Iter':<5}{'xl':<10}{'xu':<10}{'xr':<10}{'f(xl)':<12}{'f(xu)':<12}{'f(xr)':<12}{'f(xl)*f(xr)':<15}{'E_aparente(%)':<15}")
        print("-" * 100)

        while True:
            iteracion += 1
            fxl = self.evaluar_polinomio(self.xl)
            fxu = self.evaluar_polinomio(self.xu)
            fxr = self.evaluar_polinomio(self.xr)
            producto = fxl * fxr

            if iteracion == 1:
                self.error_aparente = None
            else:
                self.error_aparente = abs((self.xr - xr_anterior) / self.xr) * 100

            print(f"{iteracion:<5}{self.xl:<10.5f}{self.xu:<10.5f}{self.xr:<10.5f}{fxl:<12.5f}{fxu:<12.5f}{fxr:<12.5f}{producto:<15.5f}{'-' if self.error_aparente is None else f'{self.error_aparente:<15.5f}'}")

            
            self.iteraciones.append({
                "iter": iteracion,
                "xl": self.xl,
                "xu": self.xu,
                "xr": self.xr,
                "fxl": fxl,
                "fxu": fxu,
                "fxr": fxr,
                "producto": producto,
                "error": self.error_aparente
            })

            if fxl * fxr < 0:
                self.xu = self.xr
            else:
                self.xl = self.xr

            xr_anterior = self.xr
            self.xr = (self.xl + self.xu) / 2

           
            if self.error_aparente is not None and self.error_aparente <= self.tolerancia:
                break

        print("-" * 100)
        print(f"Raíz aproximada: {self.xr:.6f}")
        print(f"Con un error de {self.error_aparente:.6f}% tras {iteracion} iteraciones.\n")


# ===============================================================================
# ||                                                                            ||
# ||        P R O G R A M A / F U N C I O N    P R I N C I P A L                ||
# ||                                                                            ||
# ===============================================================================

metodo = Biseccion()
metodo.pedir_polinomio()
metodo.imprimir_polinomio()
metodo.pedir_datos()
metodo.calcular()
#DEBEN SER 21 ITERACIONES