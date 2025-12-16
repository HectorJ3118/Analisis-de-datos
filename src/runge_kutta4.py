import sympy as sp

# Definir símbolos
x, y = sp.symbols('x y')

print("Método de Runge–Kutta de 4º orden (RK4)")
print("EDO de la forma dy/dx = f(x,y)")
print("Ejemplo de f(x,y): x + y, x**2 + y, y**2 - x")
print()

# Entrada del usuario
f_input = input("Ingresa la función f(x,y): ")
h = float(input("Ingresa el tamaño de paso h: "))
x0 = float(input("Ingresa el valor inicial x0: "))
y0 = float(input("Ingresa la condición inicial y(x0): "))
n = int(input("Número de pasos a calcular: "))

# Convertir la función a simbólica y luego a numérica
f_sym = sp.sympify(f_input)
f = sp.lambdify((x, y), f_sym, 'math')

# Valores iniciales
xn = x0
yn = y0

print("\nResultados:")
print("n\t x\t\t y")
print("-" * 30)

for i in range(n):
    k1 = f(xn, yn)
    k2 = f(xn + h/2, yn + h*k1/2)
    k3 = f(xn + h/2, yn + h*k2/2)
    k4 = f(xn + h, yn + h*k3)

    yn = yn + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    xn = xn + h

    print(f"{i+1}\t {xn:.5f}\t {yn:.6f}")
