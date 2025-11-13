class Clase_Base:
    def __init__(self):
        self.x1=0
        self.x2=0
        self.x3=0

    def ingresar_sistema(self):
        self.sistema=[]
        print('Ingrese en sistema que quiere resolver')
        for i in range(3):
            self.fila = list(map(float, input(f"Ingrese los datos de la Fila {i+1} \n").split()))
            self.sistema.append(self.fila)

    def mostrar_sistema(self):
        print("Sistema ingresado\n")
        for i in range (3):
            print(f"Fila {i+1}= {self.sistema[i]}\n")    

class Metodo_Seidel(Clase_Base):
    def __init__(self):
        super().__init__()
        self.error=None
        self.error1=None
        self.error2=None
        self.error3=None
        self.tolerancia=0
        self.iteraciones=0
    def pedir_tolerancia(self):
        self.tolerancia=float(input("Ingrese la tolerancia: "))    
    def resolver_sistema(self):
        
        print("Iteraciones \n")
        print("Iteracion"+"     "+"   X   "+"     "+"   Y   "+"     "+"   Z   "+"     "+"   ERROR(%)   ")

        while True:
            self.iteraciones+=1
            self.x1_ant=self.x1
            self.x2_ant=self.x2
            self.x3_ant=self.x3

            self.x1 = (self.sistema[0][3] - (self.sistema[0][1]*self.x2) - (self.sistema[0][2]*self.x3)) / self.sistema[0][0]
            self.x2 = (self.sistema[1][3] - (self.sistema[1][0]*self.x1) - (self.sistema[1][2]*self.x3)) / self.sistema[1][1]
            self.x3 = (self.sistema[2][3] - (self.sistema[2][0]*self.x1) - (self.sistema[2][1]*self.x2)) / self.sistema[2][2]

            if self.iteraciones==1:
                self.error1=self.error2=self.error3=self.error=100
            else:
                self.error1 = abs((self.x1 - self.x1_ant) / self.x1) * 100
                self.error2 = abs((self.x2 - self.x2_ant) / self.x2) * 100
                self.error3 = abs((self.x3 - self.x3_ant) / self.x3) * 100
                self.error=(self.error1+self.error2+self.error3)/3    

            print(f"    {self.iteraciones}         {self.x1:.4f}      {self.x2:.4f}      {self.x3:.4f}      {self.error:.4f}")

            if self.iteraciones > 1 and self.error <= self.tolerancia:
                break

        print('Solucion aproximada del sistema por metodo de Seidel')
        print(f'X: {self.x1:.4f}')   
        print(f'Y: {self.x2:.4f}')
        print(f'Z: {self.x3:.4f}')    
        print(f"Despues de {self.iteraciones} iteraciones, con un error promedio de {self.error:.4f}")

sistema=Metodo_Seidel()
sistema.ingresar_sistema()
sistema.mostrar_sistema()
sistema.pedir_tolerancia()
sistema.resolver_sistema() 