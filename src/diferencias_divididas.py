class diferencias_divididas:
    def __init__(self,m,x,fx,n,punto):
        self.m=m
        self.x=x
        self.fx=fx
        self.n=n
        self.tabla=[]
        self.punto=punto

    def crear_tabla(self):
        self.tabla.append(self.fx)
        for i in range(1,self.m):
            fila=[]
            for j in range (self.m-i):
                numerador=self.tabla[i-1][j+1]-self.tabla[i-1][j]
                denominador=self.x[j+i]-self.x[j]
                fila.append(numerador/denominador)
            self.tabla.append(fila)
               

    def evaluar_punto(self):
        resultado=self.tabla[0][0]
        prod=1.0
        
        for i in range(1,self.n+1):
            prod*=(self.punto-self.x[i-1])
            resultado+= self.tabla[i][0]*prod
       
        print("El polinomio de Newton es:")
        for j in range(self.n+1):
            termino = f"{self.tabla[j][0]}"   

            for k in range(j):                 
                termino += f"(x - {self.x[k]})"

            if j < self.n:
                termino += " + "
            
            print(termino, end="")
        print(' ')   
        print(f"Este polinomio evauado en {self.punto} = {resultado}")
           


    
print('INTERPOLACION POR DIFERENCIAS DIVIDIDAS DE NEWTON')
m=int(input('Ingrese la cantidad de puntos: '))
print('Ingrese los valores de xi ')
x=[float(input(f'x{i}: '))for i in range(m)]
print('ingrese los valores de f(xi) ')
fx=[float(input(f'f(x{i}): '))for i in range(m)]
        
n=int(input('Ingrese el grado de interpolacion n < =m-1: '))
if n<= m-1:
    punto=float(input("Ingrese el punto donde quiere evaluar la funcion: "))
    metodo=diferencias_divididas(m,x,fx,n,punto)
    metodo.crear_tabla()
    metodo.evaluar_punto()
else:
    print('el grado de interpolacion debe de ser al menos uno menos que el numero de datos')    


        