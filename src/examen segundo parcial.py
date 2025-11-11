class Clase_base:
    def __init__(self):
        self.x1=0
        self.x2=0
        self.x3=0
        self.sistema=[]
    def ingresar_sistema(self):
        for i in range(3):
            self.fila=list(map(float,input(f"fila {i+1}: \n").split( )))
            self.sistema.append(self.fila)
    def mostrar_sistema(self):
        for i in range(3):
            print(self.sistema[i])    
            print('\n')

class Metodo(Clase_base):
    def __init__(self):
        super().__init__()
        self.tolerancia=0.0001
        self.error1=None
        self.error2=None
        self.error3=None
        self.errorprom=None
        self.iteracion=None
    def pedir_tolerancia(self):
        self.tolerancia=float(input('Ingrese la tolerancia: '))    
    def metodo(self):
        self.iteracion=0
        self.x1_anterior=self.x1
        self.x2_anterior=self.x2
        self.x3_anterior=self.x3

        while True:
            self.iteracion+=1
            x1_old,x2_old,x3_old=self.x1,self.x2,self.x3
            self.x1 = (self.sistema[0][3] - (self.sistema[0][1]*self.x2) - (self.sistema[0][2]*self.x3)) / self.sistema[0][0]
            self.x2 = (self.sistema[1][3] - (self.sistema[1][0]*self.x1) - (self.sistema[1][2]*self.x3)) / self.sistema[1][1]
            self.x3 = (self.sistema[2][3] - (self.sistema[2][0]*self.x1) - (self.sistema[2][1]*self.x2)) / self.sistema[2][2]
            
            if self.iteracion==1:
                self.error1=self.error2=self.error3=self.errorprom=100
            else:
                self.error1=abs(((self.x1-x1_old)/self.x1)*100)
                self.error2=abs(((self.x2-x2_old)/self.x2)*100) 
                self.error3=abs(((self.x3-x3_old)/self.x3)*100)  
                self.errorprom=(self.error1+self.error2+self.error3)/3

            if self.iteracion>1 and self.errorprom <= self.tolerancia:
                break  

        print(f'Ressultados despues de {self.iteracion} iteraciones: \n')
        print(f'X1={self.x1:.4f}\n')
        print(f'X2={self.x2:.4f}\n')
        print(f'X3={self.x3:.4f}\n')
        print(f"Con un error de {self.errorprom:.4f}")

metodo=Metodo()
metodo.ingresar_sistema()
metodo.mostrar_sistema()
metodo.pedir_tolerancia()
metodo.metodo()