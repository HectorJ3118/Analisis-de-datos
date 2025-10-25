# ############################################################################
# **    Proyecto       : Practica 1, Calculadora utilizando tkinter
# **    Plataforma     : VS Code
# **    Fecha/Hora     : 22/09/2025
# **    Descripción    : Esta es la practica numero 1 de la clase de analisis de datos,
# **    donde a partir de ventanas se creo una calculadora funcional con alguna de las 
# **    funciones mas importantes.
# **   By             : Hector Jimenez
# **   contact        : hjimenezm2101@alumno.ipn.mx
#  #############################################################################

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :                       Librerias / Bibliotecas / Modulos                      |
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# +-------------------------------------------------------------------------------
# |       DEFINICION Y DESARROLLO DE CLASES O FUNCIONES DE PROGRAMADOR            |
# +-------------------------------------------------------------------------------
class Clase_Base:
    def __init__(self):
      self.x=0
      self.fx=[]
      self.fdx=0
      self.polinomio= {}
    def pedir_Polinomio(self):
      self.grado=int(input('Ingresa el grado del polinomio: ')) 
      
      for i in range (self.grado,0,-1):
        coeficiente=float(input(f'Escriba el coeficiente del termino (orden descendente): '))
        self.fx=[coeficiente,i]
        self.polinomio[i]=self.fx

    def imprimir_Polinomio(self):

      for i in range(self.grado,0,-1):
         print(self.polinomio[i])
         
# ===============================================================================
# ||                                                                            ||
# ||        P R O G R A M A / F U N C I O N    P R I N C I P A L                ||
# ||                                                                            ||
# ===============================================================================
caculo=Clase_Base()
caculo.pedir_Polinomio()  
caculo.imprimir_Polinomio()     
        


