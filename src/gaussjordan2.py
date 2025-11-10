import numpy as np


class MatrizBase:
    def __init__(self):
        self.matriz = None

    def pedir_matriz(self):
        print("Introduce la matriz que quieres resolver:")
        matriz = []
        for i in range(3):
            fila = list(map(float, input(f"Fila {i+1} (4 valores separados por espacio): ").split()))
            matriz.append(fila)
        self.matriz = np.array(matriz, dtype=float)

    def imprimir_matriz(self):
        print("\nMatriz introducida:")
        print("┌                       ┐")
        print("│  x1     x2     x3     |  c │")
        for fila in self.matriz:
            print(f"│ {fila[0]:6.4f} {fila[1]:6.4f} {fila[2]:6.4f}  | {fila[3]:6.4f} │")
        print("└                       ┘")



class GaussJordan(MatrizBase):
    def resolver(self):
        A = np.copy(self.matriz)
        n = 3

        print("\n===== Método Gauss-Jordan paso a paso =====")

        for i in range(n):
            print(f"\n Paso {i+1}: Normalización de la fila {i+1})")

            pivote = A[i][i]
            if pivote == 0:
                raise ValueError("Pivote cero: el sistema no se puede resolver con este método.")
            A[i] = A[i] / pivote

            self.imprimir_paso(A)

            print(f"\nEliminación de los demás elementos en la columna {i+1}:")
            for j in range(n):
                if j != i:
                    factor = A[j][i]
                    A[j] = A[j] - factor * A[i]
            self.imprimir_paso(A)

        print("\n Matriz reducida por Gauss-Jordan:")
        self.imprimir_paso(A)

        print("\Soluciones:")
        for i, var in enumerate(['x1', 'x2', 'x3']):
            print(f"{var} = {A[i, -1]:.4f}")

    def imprimir_paso(self, A):
        print("┌                               ┐")
        print("│  x1     x2     x3     |  c │")
        for fila in A:
            print(f"│ {fila[0]:8.4f} {fila[1]:8.4f} {fila[2]:8.4f} | {fila[3]:8.4f} │")
        print("└                               ┘")


if __name__ == "__main__":
    print("=== Resolver sistema 3x3 por el método de Gauss-Jordan ===\n")

    solver = GaussJordan()
    solver.pedir_matriz()
    solver.imprimir_matriz()
    solver.resolver()

