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
      self.fx=tuple
      self.fdx=0
    
    def Pedir_Polinomio(self):
       grado=int(input('Ingresa el grado del polinomio')) 

       for i in range (grado,0):
         print(i)

caculo=Clase_Base()
caculo.Pedir_Polinomio()       
        

