class Simpson3_8:
    def __init__(self):
        self.a=None
        self.b=None
        self.polinomio={}

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
        print("\nIngresa los datos para el metodo de Simpson 1/3:\n")
        self.a=float(input("Ingresa el punto inicial: "))
        self.b=float(input('Ingresa el punto final: ')) 
    
    
    def metodo(self):
        h = (self.b - self.a) / 3
        x1=self.a+h
        print(x1)
        x2=x1+h
        print(x2)

        
       
        print(f'Ancho de cada segmento (h): {h:.6f}')
        
        fa = self.evaluar_polinomio(self.a)
        fx1=self.evaluar_polinomio(x1)
        fx2=self.evaluar_polinomio(x2)
        fb = self.evaluar_polinomio(self.b)
        
        resultado = (self.b - self.a) * (fa + 3*fx1+ 3*fx2 + fb) / (8)
        
        
        print('RESULTADOS DEL METODO DE SIMPSON 3/8')
        
        print(f'\nDesde el punto {self.a}, hasta el punto {self.b}')
        print(f'\nValor de la integral: {resultado:.6f}')        


metodo=Simpson3_8()
metodo.pedir_polinomio()
metodo.imprimir_polinomio()
metodo.pedir_datos()
metodo.metodo()