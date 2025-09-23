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
import tkinter as tk
# +-------------------------------------------------------------------------------
# |       DEFINICION Y DESARROLLO DE CLASES O FUNCIONES DE PROGRAMADOR            |
# +-------------------------------------------------------------------------------

root = tk.Tk()
root.title("Calculadora")
root.resizable(1,1)
root.geometry("400x420")  
root.config(bg="#262628")


calculadora_encendida = tk.BooleanVar(value=True)
numeroPantalla = tk.StringVar()
numeroAnterior = tk.StringVar()
resultado = 0 
operacion = '' 
numeroActual = '0'
tienePunto = False
esperandoNuevoNumero = False

miframe = tk.Frame(root, bg="#262628")
miframe.pack(pady=10)
miframe.config(bd=10, relief='ridge',cursor='dot')

entrada = tk.Entry(miframe, font=('Ds-Digital',22), justify='right', textvariable=numeroPantalla)
entrada.config(bg='#9DDF03', bd=8, relief='groove')
entrada.grid(row=0, column=0, columnspan=5, padx=5, pady=10, sticky='we')

anterior = tk.Label(miframe, font=('Ds-Digital',16), justify='right', textvariable=numeroAnterior)
anterior.config(bg="#9DDF03", bd=8, relief='groove')
anterior.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky='we')


def prender_apagar():
    global calculadora_encendida
    
    if calculadora_encendida.get():
        apagar_calculadora()
        calculadora_encendida.set(False)
        btn_off.config(text='ON', bg='#C9343E', activebackground='red')
    else:
        encender_calculadora()
        calculadora_encendida.set(True)
        btn_off.config(text='OFF', bg='#C9343E', activebackground='red')

def apagar_calculadora():
    global estado_previo
    estado_previo = numeroPantalla.get()
    numeroPantalla.set("")
    numeroAnterior.set("")
    
    btn1.config(state='disabled', bg='gray'),btn9.config(state='disabled', bg='gray')
    btn2.config(state='disabled', bg='gray'),btn0.config(state='disabled', bg='gray')
    btn3.config(state='disabled', bg='gray'),btnmas.config(state='disabled', bg='gray')
    btn4.config(state='disabled', bg='gray'),btnmenos.config(state='disabled', bg='gray')
    btn5.config(state='disabled', bg='gray'),btnpor.config(state='disabled', bg='gray')
    btn6.config(state='disabled', bg='gray'),btnborrar.config(state='disabled', bg='gray')
    btn7.config(state='disabled', bg='gray'),btndiv.config(state='disabled', bg='gray')
    btn8.config(state='disabled', bg='gray'),btans.config(state='disabled', bg='gray')
    btp.config(state='disabled', bg='gray'),btnsqr.config(state='disabled', bg='gray')
    btex.config(state='disabled', bg='gray'),btig.config(state='disabled', bg='gray')

def encender_calculadora():
    numeroPantalla.set("0")
    
    btn1.config(state='normal', bg="#1d3a6d"),btn9.config(state='normal', bg='#1D3A6D')
    btn2.config(state='normal', bg='#1D3A6D'),btn0.config(state='normal', bg='#1D3A6D')
    btn3.config(state='normal', bg='#1D3A6D'),btnmas.config(state='normal', bg='#C9343E')
    btn4.config(state='normal', bg='#1D3A6D'),btnmenos.config(state='normal', bg='#C9343E')
    btn5.config(state='normal', bg='#1D3A6D'),btnpor.config(state='normal', bg='#C9343E')
    btn6.config(state='normal', bg='#1D3A6D'),btnborrar.config(state='normal', bg='#C9343E')
    btn7.config(state='normal', bg='#1D3A6D'),btndiv.config(state='normal', bg='#C9343E')
    btn8.config(state='normal', bg='#1D3A6D'),btans.config(state='normal', bg='#C9343E')
    btp.config(state='normal', bg='#1D3A6D'),btnsqr.config(state='normal', bg='#C9343E')
    btex.config(state='normal', bg='#C9343E'),btig.config(state='normal', bg='#C9343E')


def numeroPulsado(num):
    global numeroActual, tienePunto, esperandoNuevoNumero
    
    if esperandoNuevoNumero:
        numeroActual = '0'
        tienePunto = False
        esperandoNuevoNumero = False

    if numeroActual == '0' and num != '.':
        numeroActual = num
    else:
        if num == '.' and tienePunto:
            return
        numeroActual += num

    if num == '.':
        tienePunto = True
        if numeroActual == '.':
            numeroActual = '0.'

    numeroPantalla.set(numeroActual)

def suma():
    global resultado,numeroActual,operacion,tienePunto,esperandoNuevoNumero

    if operacion and not esperandoNuevoNumero:
        calcular()

    resultado= float(numeroActual) if '.' in numeroActual else int(numeroActual)
    operacion='suma'
    numeroAnterior.set(f"{resultado} +")
    esperandoNuevoNumero=True
    tienePunto=False

def resta():
    
    global resultado,numeroActual,operacion,tienePunto,esperandoNuevoNumero

    if operacion and not esperandoNuevoNumero:
        calcular()

    resultado= float(numeroActual) if '.' in numeroActual else int(numeroActual)
    operacion='resta'
    numeroAnterior.set(f"{resultado} -")
    esperandoNuevoNumero=True
    tienePunto=False    

def multiplicacion():
    global resultado,numeroActual,operacion,tienePunto,esperandoNuevoNumero

    if operacion and not esperandoNuevoNumero:
        calcular()

    resultado= float(numeroActual) if '.' in numeroActual else int(numeroActual)
    operacion='multiplicacion'
    numeroAnterior.set(f"{resultado} *")
    esperandoNuevoNumero=True
    tienePunto=False 

def division(): 
    global resultado,numeroActual,operacion,tienePunto,esperandoNuevoNumero

    if operacion and not esperandoNuevoNumero:
        calcular()

    resultado= float(numeroActual) if '.' in numeroActual else int(numeroActual)
    operacion='division'
    numeroAnterior.set(f"{resultado} /")
    esperandoNuevoNumero=True
    tienePunto=False

def potencia(): 
    global resultado,numeroActual,operacion,tienePunto,esperandoNuevoNumero

    if operacion and not esperandoNuevoNumero:
        calcular()

    resultado= float(numeroActual) if '.' in numeroActual else int(numeroActual)
    operacion='potencia'
    numeroAnterior.set(f"{resultado} ^")
    esperandoNuevoNumero=True
    tienePunto=False    

def calcular():
    
    global resultado, numeroActual, operacion, tienePunto, esperandoNuevoNumero
    
    if not operacion:
        return
    
    num2 = float(numeroActual) if '.' in numeroActual else int(numeroActual)
    
    if operacion == 'suma':
        resultado += num2
    elif operacion == 'resta':
        resultado -= num2
    elif operacion == 'multiplicacion':
        resultado *= num2
    elif operacion == 'division':
        if num2 == 0:
            numeroPantalla.set("No se admite division entre 0")
            return
        resultado /= num2
    elif operacion == 'potencia':
        resultado **= num2
        
       
    if resultado == int(resultado):
        resultado = int(resultado)
        numeroActual = str(resultado)
    else:
        numeroActual = str(resultado)
        
    numeroPantalla.set(numeroActual)
    numeroAnterior.set("")
    operacion = ''
    esperandoNuevoNumero = True
    tienePunto = '.' in numeroActual

def limpiar():
    global resultado, operacion, numeroActual, tienePunto, esperandoNuevoNumero
    numeroActual = '0'
    resultado = 0
    operacion = ''
    tienePunto = False
    esperandoNuevoNumero = False
    numeroPantalla.set(numeroActual)
    numeroAnterior.set("")

def raizCuadrada():
    global numeroActual, tienePunto

    num = float(numeroActual) if '.' in numeroActual else int(numeroActual)
    if num < 0:
            numeroPantalla.set("No admite raices negativas")
            return
        
    resultado = num ** 0.5
    if resultado == int(resultado):
        numeroActual = str(int(resultado))
        tienePunto = False
    else:
        numeroActual = str(resultado)
        tienePunto = True
        
    numeroPantalla.set(numeroActual)
    
def usarAns(): 
    global numeroActual, tienePunto, esperandoNuevoNumero
    if esperandoNuevoNumero:
        numeroActual = '0'
        tienePunto = False
        esperandoNuevoNumero = False
    
    if numeroActual == '0':
        numeroActual = str(resultado)
    else:
        numeroActual += str(resultado)
    
    tienePunto = '.' in numeroActual
    numeroPantalla.set(numeroActual)

# ===============================================================================
# ||                                                                            ||
# ||        P R O G R A M A / F U N C I O N    P R I N C I P A L                ||
# ||                                                                            ||
# ===============================================================================

btn7 = tk.Button(miframe, text='7', width=5, height=2, font=('Name Smile',10), activebackground='#1C4BA1', activeforeground='white',command=lambda: numeroPulsado("7"))
btn7.config(bg="#1d3a6d", bd=5, relief='raised')
btn7.grid(row=2, column=0, padx=2, pady=2)

btn8 = tk.Button(miframe, text='8', width=5, height=2, font=('Name Smile',10),activebackground='#1C4BA1', activeforeground='white',command=lambda: numeroPulsado("8"))
btn8.config(bg='#1d3a6d', bd=5, relief='raised')
btn8.grid(row=2, column=1, padx=2, pady=2)

btn9 = tk.Button(miframe, text='9', width=5, height=2, font=('Name Smile',10),activebackground='#1C4BA1', activeforeground='white',command=lambda: numeroPulsado("9"))
btn9.config(bg='#1d3a6d', bd=5, relief='raised')
btn9.grid(row=2, column=2, padx=2, pady=2)

btnmas = tk.Button(miframe, text='+', width=5, height=2, font=('Name Smile',10),activebackground='red', activeforeground='black',command=suma)
btnmas.config(bg='#C9343E', bd=5, relief='raised')
btnmas.grid(row=2, column=3, padx=2, pady=2)

btnmenos = tk.Button(miframe, text='-', width=5, height=2, font=('Name Smile',10),activebackground='red', activeforeground='black',command=resta)
btnmenos.config(bg='#C9343E', bd=5, relief='raised')
btnmenos.grid(row=2, column=4, padx=2, pady=2)



btn4 = tk.Button(miframe, text='4', width=5, height=2, font=('Name Smile',10),activebackground='#1C4BA1', activeforeground='white',command=lambda: numeroPulsado("4"))
btn4.config(bg='#1d3a6d', bd=5, relief='raised')
btn4.grid(row=3, column=0, padx=2, pady=2)

btn5 = tk.Button(miframe, text='5', width=5, height=2, font=('Name Smile',10), activebackground='#1C4BA1', activeforeground='white',command=lambda: numeroPulsado("5"))
btn5.config(bg='#1d3a6d', bd=5, relief='raised')
btn5.grid(row=3, column=1, padx=2, pady=2)

btn6 = tk.Button(miframe, text='6', width=5, height=2, font=('Name Smile',10),activebackground='#1C4BA1', activeforeground='white',command=lambda: numeroPulsado("6"))
btn6.config(bg='#1d3a6d', bd=5, relief='raised')
btn6.grid(row=3, column=2, padx=2, pady=2)

btnpor = tk.Button(miframe, text='X', width=5, height=2, font=('Name Smile',10),activebackground='red', activeforeground='black',command=multiplicacion)
btnpor.config(bg='#C9343E', bd=5, relief='raised')
btnpor.grid(row=3, column=3, padx=2, pady=2)

btnborrar = tk.Button(miframe, text='C', width=5, height=2, font=('Name Smile',10),activebackground='red', activeforeground='black', command=limpiar)
btnborrar.config(bg='#C9343E', bd=5, relief='raised')
btnborrar.grid(row=3, column=4, padx=2, pady=2)


btn1 = tk.Button(miframe, text='1', width=5, height=2, font=('Name Smile',10),activebackground='#1C4BA1', activeforeground='white',command=lambda: numeroPulsado("1"))
btn1.config(bg='#1d3a6d', bd=5, relief='raised')
btn1.grid(row=4, column=0, padx=2, pady=2)

btn2 = tk.Button(miframe, text='2', width=5, height=2, font=('Name Smile',10),activebackground='#1C4BA1', activeforeground='white',command=lambda: numeroPulsado("2"))
btn2.config(bg='#1d3a6d', bd=5, relief='raised')
btn2.grid(row=4, column=1, padx=2, pady=2)

btn3 = tk.Button(miframe, text='3', width=5, height=2, font=('Name Smile',10),activebackground='#1C4BA1', activeforeground='white',command=lambda: numeroPulsado("3"))
btn3.config(bg='#1d3a6d', bd=5, relief='raised')
btn3.grid(row=4, column=2, padx=2, pady=2)

btndiv = tk.Button(miframe, text='/', width=5, height=2, font=('Name Smile',10), activebackground='red',activeforeground='black',command=division)
btndiv.config(bg='#C9343E', bd=5, relief='raised')
btndiv.grid(row=4, column=3, padx=2, pady=2)

btans = tk.Button(miframe, text='ANS', width=5, height=2, font=('Name Smile',10),activebackground='red',activeforeground='black',command=usarAns)
btans.config(bg='#C9343E', bd=5, relief='raised')
btans.grid(row=4, column=4, padx=2, pady=2)

btp = tk.Button(miframe, text='.', width=5, height=2, font=('Name Smile',10), activebackground='#1C4BA1',activeforeground='white',command=lambda: numeroPulsado('.'))
btp.config(bg='#1d3a6d', bd=5, relief='raised')
btp.grid(row=5, column=0, padx=2, pady=2)

btn0 = tk.Button(miframe, text='0', width=5, height=2, font=('Name Smile',10),activebackground='#1C4BA1',activeforeground='white',command=lambda: numeroPulsado("0"))
btn0.config(bg='#1d3a6d', bd=5, relief='raised')
btn0.grid(row=5, column=1, padx=2, pady=2)

btex = tk.Button(miframe, text='^', width=5, height=2, font=('Name Smile',10),activebackground='red',activeforeground='black',command=potencia)
btex.config(bg='#C9343E', bd=5, relief='raised')
btex.grid(row=5, column=2, padx=2, pady=2)

btnsqr = tk.Button(miframe, text='SQR', width=5, height=2, font=('Name Smile',10),activebackground='red',activeforeground='black',command=raizCuadrada)
btnsqr.config(bg='#C9343E', bd=5, relief='raised')
btnsqr.grid(row=5, column=3, padx=2, pady=2)

btig = tk.Button(miframe, text='=', width=5, height=2, font=('Name Smile',10), activebackground='#0BD20B',activeforeground='black',command=calcular)
btig.config(bg='#018001', bd=5, relief='raised')
btig.grid(row=5, column=4, padx=2, pady=2)


btn_off = tk.Button(miframe, text='OFF', width=15, height=2, font=('Name Smile',10), activebackground='red',activeforeground='black',command=prender_apagar)
btn_off.config(bg='#C9343E', bd=5, relief='raised')
btn_off.grid(row=6, column=2, padx=2, pady=10, columnspan=5)


root.mainloop()