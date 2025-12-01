import numpy as np
import matplotlib.pyplot as plt
class Clase_Base:
    def __init__(self):
        self.n=0
        self.punto=[]
        self.puntos=[]
        self.xp=[]
        self.xy=[]

    def ingresar_puntos(self):
        print("METODO DE MINIMOS CUADRADOS \n")
        self.n=int(input('Ingrese el numero de puntos: '))
        for i in range(self.n):
            self.x=float(input(f"Ingrese el valor de x del punto {i+1}: "))
            self.y=float(input(f'ingrese el valor de f(x) del punto {i+1}: ')) 
            self.xp.append(self.x)
            self.xy.append(self.y)
            self.punto=[self.x,self.y]
            self.puntos.append(self.punto)

    def mostrar_puntos(self):
        print('Puntos del metodo de minimos cuadrados\n')
        for i in range (self.n):
            print(f'{self.puntos[i]}\n')
class Minimos_cuadrados(Clase_Base):
    def __init__(self):
        super().__init__()
        self.a1=0
        self.xsum=0
        self.ysum=0
        self.a0=0
        self.xiyisum=0
        self.xi2sum=0
        self.resultado=0
        self.sr=0
        self.st=0
        self.sumota=0
        self.sy=0
        self.syx=0
        self.r2=0
        self.r=0
        self.yprom=0
        self.xprom=0
        self.xsum=0
        self.ysum=0

    def metodo(self):
        for i in range(self.n):
            self.yprom+=self.puntos[i][1]/self.n
            self.xprom+=self.puntos[i][0]/self.n  
            self.xsum+=self.puntos[i][0]
            self.ysum+=self.puntos[i][1]
            self.xiyisum+=(self.puntos[i][0]*self.puntos[i][1])
            self.xi2sum+=self.puntos[i][0]**2

        for i in range(self.n):
            self.a1=((self.n*self.xiyisum)-(self.xsum*self.ysum))/((self.n*self.xi2sum)-(self.xsum)**2)
            self.a0=self.yprom-(self.a1*self.xprom)
            self.st+=(self.puntos[i][1]-self.yprom)**2
            self.sr+=(self.puntos[i][1]-self.a0-(self.a1*self.puntos[i][0]))**2
        self.syx=(self.sr/self.n-2)**1/2
        self.sy=(self.st/self.n-1)**1/2
        print("\n--- Regresión lineal por mínimos cuadrados---")
        print(f"{'xi':<8}{'yi':<8}{'xi^2':<10}{'xiyi':<10}{'(yi-yprom)^2':<15}{'(yi-a0-a1xi)^2':<15}")
        print("-" * 60)
        for i in range(self.n):
            xi=self.puntos[i][0]
            xi2=(self.puntos[i][0])**2
            yi=self.puntos[i][1]
            xiyi=(self.puntos[i][0])*(self.puntos[i][1])
            yi_yprom=(self.puntos[i][1]-self.yprom)**2
            yi_ao=(self.puntos[i][1]-self.a0-(self.a1*self.puntos[i][0]))**2
            print(f"{xi:<8}{yi:<8}{xi2:<10.2f}{xiyi:<10.4f}{yi_yprom:<15.4f}{yi_ao:<15.4f}")
        print('-'*60)   
        print(f'{self.xsum:<8}{self.ysum:<8.2f}{self.xi2sum:<10.4f}{self.xiyisum:<10.4f}{self.st:<15.4f}{self.sr:<5.4f}')
        print(f"polinomio: y={self.a0:.6f} + {self.a1:.6f}x")
        if (self.syx < self.sy):
            print('El ajuste de la recta es CORRECTO')
        else:
            print('El ajuste de la recta es INCORRECTO')    
    def grafica(self):
        plt.scatter(self.xp,self.xy)
        plt.plot(self.xp,self.xy,marker='o')
        x_vals=np.linspace(0,self.n+1,100)
        y_vals=self.a1*x_vals+self.a0
        plt.plot(x_vals,y_vals)
        plt.grid(True)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Ajuste lineal por minimos cuadrados")
        plt.legend()
        plt.show()
                
minimos_cuadrados=Minimos_cuadrados()
minimos_cuadrados.ingresar_puntos()
minimos_cuadrados.metodo()
minimos_cuadrados.grafica()