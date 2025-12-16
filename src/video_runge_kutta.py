class Runge_kutta:
    def __init__(self):
        self.polinomio=[]
        self.iteraciones=None
    def pedir_polinomio(self):
        grado = int(input("Ingrese el grado del polinomio: "))
        for i in range(grado, -1, -1):
            coef = float(input(f"Ingrese el coeficiente de x^{i}: "))
            self.polinomio[i] = coef
        print("\nPolinomio ingresado correctamente.\n")     

    def evaluar_polinomio(self, x):
        
        resultado = 0
        for g, c in self.polinomio.items():
            resultado += c * (x ** g)
        return resultado    
    
    def pedir_datos(self):
        self.x0=float(input("Ingresa el valor de X0: "))
        self.y0=float(input("Ingresa el valor de Y0: "))
        self.h=float(input("Ingresa el tamaño del paso (h): "))
        self.punto=float(input("Ingresa el punto donde quieres evaluar la solucion: "))
        avance=self.punto-self.x0
        avance_int = int(avance * 100000) 
        h_int = int(self.h * 100000)
        self.iteraciones=int(avance_int/h_int)
        if avance_int % h_int==0:
            self.i=0
            n=0
            while True:
                self.i+=1
                n+=1
                print("Iteracion")







                if self.i==self.iteraciones or n==100 :
                    break


        else:
            print("Este punto no se puede alcanzar con ese paso")    
            

    

metodo=Runge_kutta()
metodo.pedir_datos()