class Lagrange:
    def __init__(self, m, x, fx, n, punto):
        self.m = m
        self.x = x
        self.fx = fx
        self.n = n
        self.punto = punto

    def crear_li(self, i, x_eval):
        Li = 1
        for j in range(self.n+1):
            if j != i:
                Li *= (x_eval - self.x[j]) / (self.x[i] - self.x[j])
        return Li

    def evaluar_punto(self):
        
        resultado = 0
        for i in range(self.n+1):
            resultado += self.fx[i] * self.crear_li(i, self.punto)

        
        print("\nEl polinomio de Lagrange es:")
        polinomio = ""

        for i in range(self.n+1):
            termino = f"{self.fx[i]} * ["

            for j in range(self.n+1):
                if j != i:
                    termino += f"(x - {self.x[j]})/({self.x[i]} - {self.x[j]})"

                if j != self.n:
                    termino += " "

            termino += "]"

            if i < self.n:
                termino += " + "

            polinomio += termino

        print(polinomio)
        print(f"\nEvaluado en {self.punto} = {resultado:.4f}")



print('INTERPOLACIÓN POR LAGRANGE')
m = int(input('Ingrese la cantidad de puntos: '))

print('Ingrese los valores de xi:')
x = [float(input(f'x{i}: ')) for i in range(m)]

print('Ingrese los valores de f(xi):')
fx = [float(input(f'f(x{i}): ')) for i in range(m)]

n = int(input('Ingrese el grado de interpolación n <= m-1: '))

if n <= m - 1:
    punto = float(input("Ingrese el punto donde se evaluará la función: "))
    metodo = Lagrange(m, x, fx, n, punto)
    metodo.evaluar_punto()
else:
    print("El grado debe ser <= m - 1")

