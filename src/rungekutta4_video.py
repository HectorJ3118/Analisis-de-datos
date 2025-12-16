class Runge_kutta:
    def __init__(self):
        self.polinomio = {}
        self.x0 = None
        self.y0 = None
        self.h = None
        self.punto = None
        self.iteraciones = None
        self.k1 = None
        self.k2 = None
        self.k3 = None
        self.k4 = None
        self.y = None
    
    def pedir_polinomio(self):
        
        num_terminos = int(input("\n¿Cuantos terminos tiene tu polinomio?: "))
        
        for i in range(num_terminos):
            print(f"\nTermino {i+1}:")
            coef = float(input("  Coeficiente: "))
            exp_x = int(input("  Exponente de x : "))
            exp_y = int(input("  Exponente de y : "))
            
            
            self.polinomio[i] = {'coef': coef, 'exp_x': exp_x, 'exp_y': exp_y}
        
        print("\nPolinomio ingresado correctamente.")
        self.mostrar_polinomio()
    
    def mostrar_polinomio(self):
        print("\nPolinomio f(x, y) = ", end="")
        terminos = []
        for termino in self.polinomio.values():
            coef = termino['coef']
            exp_x = termino['exp_x']
            exp_y = termino['exp_y']
            
            
            partes = []
            if coef != 0:
                if abs(coef) != 1 or (exp_x == 0 and exp_y == 0):
                    partes.append(f"{coef:+g}")
                elif coef == 1:
                    partes.append("+")
                elif coef == -1:
                    partes.append("-")
                
                if exp_x > 0:
                    if exp_x == 1:
                        partes.append("x")
                    else:
                        partes.append(f"x^{exp_x}")
                if exp_y > 0:
                    if exp_y == 1:
                        partes.append("y")
                    else:
                        partes.append(f"y^{exp_y}")
                
                termino = "".join(partes)
                if termino.startswith("+"):
                    termino = termino[1:]
                terminos.append(termino)
        
        if not terminos:
            print("0")
        else:
            print(" + ".join(terminos).replace("+ -", "- "))
    
    def evaluar_polinomio(self, x, y):
        resultado = 0
        for termino in self.polinomio.values():
            coef = termino['coef']
            exp_x = termino['exp_x']
            exp_y = termino['exp_y']
            
            valor_x = x ** exp_x if exp_x > 0 else 1
            valor_y = y ** exp_y if exp_y > 0 else 1
            
            resultado += coef * valor_x * valor_y
        
        return resultado
    
    def calcular_runge_kutta(self):
        
        self.k1 = self.h * self.evaluar_polinomio(self.x0, self.y0)
        
        x_medio = self.x0 + self.h/2
        y_medio = self.y0 + self.k1/2
        self.k2 = self.h * self.evaluar_polinomio(x_medio, y_medio)
        
        y_medio2 = self.y0 + self.k2/2
        self.k3 = self.h * self.evaluar_polinomio(x_medio, y_medio2)
        
        
        x_final = self.x0 + self.h
        y_final = self.y0 + self.k3
        self.k4 = self.h * self.evaluar_polinomio(x_final, y_final)
        
        
        delta_y = (self.k1 + 2*self.k2 + 2*self.k3 + self.k4) / 6
        nuevo_y = self.y0 + delta_y
        
        return nuevo_y
    
    def pedir_datos(self):
        
        self.pedir_polinomio()
        
        self.x0 = float(input("Ingresa el valor inicial de x (x0): "))
        self.y0 = float(input("Ingresa el valor inicial de y (y0): "))
        self.h = float(input("Ingresa el tamaño del paso (h): "))
        self.punto = float(input("Ingresa el punto x donde quieres evaluar la solución: "))
        
        
        avance = self.punto - self.x0
        
        
        if abs(self.h) < 1e-10:
            print("Error: El paso h no puede ser cero.")
            return
        
        
        self.iteraciones = int(round(avance / self.h))
        
       
        if abs(avance - self.iteraciones * self.h) > 1e-10:
            print(f" El punto {self.punto} no es alcanzable exactamente con h = {self.h}")
            
            
        
       
        print(f"Se necesitan {self.iteraciones} iteraciones para llegar aproximadamente a x = {self.punto}")
        print(f"\nCondiciones iniciales: x0 = {self.x0}, y0 = {self.y0}")
        print(f"Paso h = {self.h}")
        print("-" * 50)

        x_actual = self.x0
        y_actual = self.y0
        
        for i in range(1, self.iteraciones + 1):
            print(f"\n--- Iteracion {i} ---")
            print(f"x{i-1} = {x_actual:.6f}, y{i-1} = {y_actual:.6f}")
            
            self.x0 = x_actual
            self.y0 = y_actual
            nuevo_y = self.calcular_runge_kutta()
        
            print(f"k1 = h * f(x, y) = {self.h:.6f} * f({x_actual:.6f}, {y_actual:.6f}) = {self.k1:.6f}")
            print(f"k2 = h * f(x + h/2, y + k1/2) = {self.h:.6f} * f({x_actual + self.h/2:.6f}, {y_actual + self.k1/2:.6f}) = {self.k2:.6f}")
            print(f"k3 = h * f(x + h/2, y + k2/2) = {self.h:.6f} * f({x_actual + self.h/2:.6f}, {y_actual + self.k2/2:.6f}) = {self.k3:.6f}")
            print(f"k4 = h * f(x + h, y + k3) = {self.h:.6f} * f({x_actual + self.h:.6f}, {y_actual + self.k3:.6f}) = {self.k4:.6f}")
            print(f"y = (k1 + 2k2 + 2k3 + k4)/6 = ({self.k1:.6f} + 2*{self.k2:.6f} + 2*{self.k3:.6f} + {self.k4:.6f})/6 = {(self.k1 + 2*self.k2 + 2*self.k3 + self.k4)/6:.6f}")
            
            x_actual += self.h
            y_actual = nuevo_y
            
            print(f"Nuevos valores: x{i} = {x_actual:.6f}, y{i} = {y_actual:.6f}")
        
        print("-"*60)
        print(f"RESULTADO FINAL:")
        print(f"En x = {x_actual:.6f}")
        
        self.y = y_actual
        return y_actual
    
    def mostrar_resultado(self):
        print(f"Número de iteraciones: {self.iteraciones}")
        print(f"\nSolución aproximada: y({self.punto}) ≈ {self.y:.10f}")
        




print("PROGRAMA PARA RESOLVER ECUACIONES DIFERENCIALES")
print("USANDO EL METODO DE RUNGE-KUTTA DE 4TO ORDEN")
print("-" * 60)
metodo = Runge_kutta()
metodo.pedir_datos()
metodo.mostrar_resultado()
        