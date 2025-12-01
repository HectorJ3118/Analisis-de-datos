class Clase_Base:
    def __init__(self):
        self.n=0
        self.punto=[]
        self.puntos=[]

    def ingresar_puntos(self):
        print("METODO DE MINIMOS CUADRADOS \n")
        self.n=int(input('Ingrese el numero de puntos: '))
        for i in range(self.n):
            self.x=float(input(f"Ingrese el valor de x del punto {i+1}: \n"))
            self.y=float(input(f'ingrese el valor de f(x) del punto {i+1}: \n'))  
            self.punto=[self.x,self.y]
            self.puntos.append(self.punto)

    def mostrar_puntos(self):
        print('Puntos del metodo de minimos cuadrados\n')
        for i in range (self.n):
            print(f'{self.puntos[i]}\n')
class Minimos_cuadrados(Clase_Base):
    def __init__(self):
        super().__init__()
        self.a1=0,self.xsum=0,self.ysum=0
        self.a0=0,self.xiyisum=0,self.xi2sum=0
        self.resultado=0,self.yminusypromsum=0
        self.sr=0,self.sumota=0
        self.sy=0
        self.syx=0
        self.r2=0
        self.r=0
        self.yprom=0
        self.xprom=0
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

        print("\n--- Regresión lineal por mínimos cuadrados---")
        print(f"{'xi':<5}{'yi':<5}{'xi^2':<6}{'xiyi':<6}{'(yi-yprom)^2':<15}{'(yi-a0-a1xi)^2':<15}")
        print("-" * 60)
        for i in range(self.n):
            xi=self.puntos[i][0]
            xi2=(self.puntos[i][0])**2
            yi=self.puntos[i][1]
            xiyi=(self.puntos[i][0])*(self.puntos[i][1])
            print(f"{xi:<5}{yi:<5}{xi2:<6}{xiyi:<6}{}")

minimos_cuadrados=Minimos_cuadrados()
minimos_cuadrados.ingresar_puntos()
minimos_cuadrados.metodo()