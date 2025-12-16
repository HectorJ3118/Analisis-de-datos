
class Trapecio_multiple:
    def __init__(self):
        self.n=None
        self.polinomio={}
        self.a=None
        self.b=None
        self.suma=0

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
    
    def pedir_datos(self):
        print("Ingresa los datos para el metodo de trapecio multiple:\n")
        self.a=float(input("Ingresa el punto inicial: "))
        self.b=float(input('Ingresa el punto final: ')) 
        self.n=int(input('Ingresa la cantidad de trapecios: ')) 

    def metodo(self):
        h = (self.b - self.a) / self.n
        
    
        for i in range(1, self.n):
            x = self.a + i * h
            self.suma += self.evaluar_polinomio(x) 
        
        
        resultado = (self.b - self.a) * (self.evaluar_polinomio(self.a) + 
                                       2 * self.suma + 
                                       self.evaluar_polinomio(self.b)) / (2 * self.n)

        print(f'Aplicando el metodo de trapecio de aplicacion multiple: \n')
        print(f'Desde el punto {self.a}, hasta el punto {self.b}, usando {self.n} trapecios')
        print(f'Da como resultado {resultado}')
    
    

metodo=Trapecio_multiple()
metodo.pedir_polinomio()
metodo.imprimir_polinomio()
metodo.pedir_datos()
metodo.metodo()

        
           
        