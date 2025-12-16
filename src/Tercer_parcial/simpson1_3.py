class Simpson1_3:
    def __init__(self):
        self.a=None
        self.b=None
        self.polinomio={}
        self.n=None
        self.suma_pares=0
        self.suma_impares=0
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
    
        while True:
            self.n=int(input('Ingresa la cantidad de segmentos (debe ser par): ')) 
            if self.n % 2 == 0 and self.n > 0:
                break
            print("Error: n debe ser un número par positivo. Intente nuevamente.")
    def metodo(self):
        h = (self.b - self.a) / self.n
        
        print(f'\nCalculando con {self.n} segmentos')
        
        fa = self.evaluar_polinomio(self.a)
        
        for i in range(1, self.n, 2):
            x = self.a + i * h
            fx = self.evaluar_polinomio(x)
            self.suma_impares += fx
            
        for i in range(2, self.n, 2):
            x = self.a + i * h
            fx = self.evaluar_polinomio(x)
            self.suma_pares += fx
        
        fb = self.evaluar_polinomio(self.b)
        
        resultado = (self.b - self.a) * (fa + 4*self.suma_impares + 2*self.suma_pares + fb) / (3 * self.n)
        print('RESULTADOS DEL METODO DE SIMPSON 1/3')
        
        print(f'\nDesde el punto {self.a}, hasta el punto {self.b}')
        print(f'Usando {self.n} segmentos ({self.n/2} parábolas)')
        print(f'\nValor de la integral: {resultado:.4f}')        


metodo=Simpson1_3()
metodo.pedir_polinomio()
metodo.imprimir_polinomio()
metodo.pedir_datos()
metodo.metodo()