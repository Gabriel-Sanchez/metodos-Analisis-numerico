from tkinter import *
import math


from Metodos.MetodoReglaFalsa import funcionReglaFalsa
from Metodos.MetodoBiseccion import funcionBiseccion
from Metodos.MetodoNewtonRaphson import funcionNewtonRaphson
from Metodos.MetodoSecante import funcionSecante
from Metodos.MetodoMuller import funcionMuller
from Metodos.MetodoPuntoFijo import funcionPuntoFijo



ventana = Tk()
ventana.title("Metodos de Analisis Numerico")


def llamaMetodo(respMetodo):
    
        
    variabFB.set(respMetodo['FB'])
    variabFA.set(respMetodo['FA'])
    
    i = 0
    for info in respMetodo['ListIteraciones']:
        i = i + 1
        print(info)
        areatexo.insert(str(float(i)), info)

    variabM.set(respMetodo['M'])
    variabFM.set(respMetodo['FM'])

def Corta_Fx_Gx_or_a_y_b(texto):
    listabuscar = texto.split(" ")
    for dat in range(0, len(listabuscar)):
        if listabuscar[dat] == ",":
            cortFG = texto.split(" , ")
            print(cortFG)
            break
        else:
            cortFG = texto
            print(cortFG)

    print(cortFG)
 

    return cortFG


def sen(grados):
    return math.sin(math.radians(grados))

def Dg(gx, x):
    h = 0.000001
    fxmenosh = funcResp(gx, (x - h))
    fxmash = funcResp(gx, (x + h))
    print("tiene el mas y meos h")
    fxmash = float(fxmash[0])
    fxmenosh = float(fxmenosh[0])

    print(fxmenosh)
    print(fxmash)
    Resp = ( fxmash - fxmenosh ) / (2 * h)
    return Resp

def funVariables(textfunc, X):

    FxGX = Corta_Fx_Gx_or_a_y_b(textfunc)
    a_y_b = Corta_Fx_Gx_or_a_y_b(X)
    areatexo.delete("1.0", END)


    variabFA.set(" ")
    variabFB.set(" ")
    variabM.set("")
    variabFM.set("")

    if varRadioBut.get() == 1:

        fx = FxGX
        x = a_y_b[0]
        y = a_y_b[1]
        # funcionReglaFalsa(fx, float(x), float(y))
        llamaMetodo(funcionReglaFalsa(fx, float(x), float(y)))
        print("va a realizar la Regla Falsa")

    elif varRadioBut.get() == 2:

        fx = FxGX[0]
        print("fx antes de entrar a punto fijo es: ", fx)
        gx = FxGX[1]
        print("gx antes de entrar a PF ", gx)

        print("va a realizar el punto fijo")
        
        llamaMetodo(funcionPuntoFijo(fx, gx, float(X)))
    elif varRadioBut.get() == 3:

        fx = FxGX
        print("va a realizar newton Rapson")
        llamaMetodo(funcionNewtonRaphson(fx, float(X)))
    elif varRadioBut.get() == 4:
        fx = FxGX
        x = a_y_b[0]
        y = a_y_b[1]
        print("biseccion")
        llamaMetodo(funcionBiseccion(fx, float(x), float(y)))
    elif varRadioBut.get() == 5:
        print("")

        fx = FxGX
        x = a_y_b[0]
        y = a_y_b[1]
        # funcionMuller(fx, float(x), float(y))
        llamaMetodo(funcionMuller(fx, float(x), float(y)))




    elif varRadioBut.get() == 6:
        fx = FxGX
        x = a_y_b[0]
        y = a_y_b[1]
        print("secante")
        llamaMetodo(funcionSecante(fx, float(x), float(y)))


    else:


        print("no hay opcion")
        areatexo.insert("1.0", "Error, no hay opcion")

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return (-1)
    else:
        return 0


def funcResp(textfunc, x):

    print(" el texto en la func resp es : ", textfunc)
    
    lista = textfunc.split(" ")
    ind = 0
    print(lista)

    for indice in range(0, len(lista)):
        if lista[indice] == "x":
            lista[indice] = x

        if lista[indice] == "-x":
            lista[indice] = (x * -1)

        if lista[indice] == "pi":
            lista[indice] = math.pi

    while len(lista) != ind:

        if lista[ind] == "(":
            j = ind
            j2 = ind
            while lista[j] != ")":
                if lista[j] == "(":
                    j2 = j
                    ind = ind - 1
                j = j + 1
            print(f"se va a entrar a resolver el parentesis en la posicion :{j2}")
            iteracionesResp(j2, lista)

        ind = ind + 1
    lista.insert(0, "(")
    lista.insert(len(lista), ")")
    iteracionesResp(0, lista)

    print(lista)
    print("va a retornar la lista 2")

    return lista




def iteracionesResp(i2, lista):
    i = i2
    iteraciones = 0
    print(f"i={i}")

    while lista[i] != ")":

        if lista[i] == 'sen':
            print("va a resolver un sen")
            r = math.sin(float(lista[i + 1]))

            lista[i + 1] = r

            lista.pop(i)
            #lista.pop(i - 1)

            i = i - 1
            print(lista)

        if lista[i] == 'cos':
            print("va a resolver un cos")
            r = math.cos(float(lista[i + 1]))

            lista[i + 1] = r

            lista.pop(i)
            #lista.pop(i - 1)

            i = i - 1
            print(lista)

        if lista[i] == 'tan':
            print("va a resolver un exponente")
            r = math.tan(float(lista[i + 1]))

            lista[i + 1] = r

            lista.pop(i)
            #lista.pop(i - 1)

            i = i - 1
            print(lista)

        i = i + 1

    #--------------
    i = i2

    while lista[i] != ")":

        if lista[i] == '^':
            print("va a resolver un exponente")
            r = float(lista[i - 1]) ** float(lista[i + 1])

            lista[i + 1] = r

            lista.pop(i)
            lista.pop(i - 1)

            i = i - 1
            print(lista)
        i = i + 1

    i = i2

    while lista[i] != ")":

        if lista[i] == '*':
            print("va a multiplicar")
            r = float(lista[i - 1]) * float(lista[i + 1])

            lista[i + 1] = r

            lista.pop(i)
            lista.pop(i - 1)

            i = i - 1
            print(lista)


        if lista[i] == '/':
            print("va a dividir")
            r = float(lista[i - 1]) / float(lista[i + 1])

            lista[i + 1] = r

            lista.pop(i)
            lista.pop(i - 1)

            i = i - 1

            print(lista)
        i = i + 1
        j = 0


        iteraciones += 1

    i = i2
    print(f'i va a tomar el valor de i2 ={i}')
    while lista[i] != ")":

        if lista[i] == '+':
            print(f"va a sumar con la ={i}")
            r = float(lista[i - 1]) + float(lista[i + 1])

            lista[i + 1] = r

            lista.pop(i)
            lista.pop(i - 1)

            i = i - 1

            print(lista)

        if lista[i] == '-':
            print("va a restar")
            r = float(lista[i - 1]) - float(lista[i + 1])

            lista[i + 1] = r

            lista.pop(i)
            lista.pop(i - 1)

            i = i - 1
            print(lista)


        i = i + 1
        j = 0
        print("SE VA A IMP")

        print(lista)
        print('fin de la imp')
        iteraciones += 1

    print("casi sale")
    print(f"numero de iteraciones = {iteraciones}")
    print(f"se va a eliminar la i={i}")
    lista.pop(i)
    lista.pop(i2)
    print("fin, va a retornar")

    return lista


#----------------------

def impresionEnLabels():

    if varRadioBut.get() == 1:
        labetextoentrada.config(text="Regla falsa: introducir fx")
        labelA.config(text="a,b =")
        labelFA.config(text="fa =")
        labelFB.config(text="fb =")
    elif varRadioBut.get() == 2:
        labetextoentrada.config(text="Punto Fijo: introducir fx y gx sepados por una coma (,)")
        labelA.config(text="x =")
        labelFA.config(text="fx = ")
        labelFB.config(text="Dg =")
    elif varRadioBut.get() == 3:
        labetextoentrada.config(text="Newton Raphson introducir fx")
        labelA.config(text="x =")
        labelFA.config(text="fx = ")
        labelFB.config(text="Dx =")
    elif varRadioBut.get() == 4:
        labetextoentrada.config(text="Biseccion introducir fx")
        labelA.config(text="a,b =")
        labelFA.config(text="fa = ")
        labelFB.config(text="fb =")
    elif varRadioBut.get() == 5:
        labetextoentrada.config(text="Muler introducir fx")
        labelA.config(text="x1, x2 =")
        labelFA.config(text="f1x = ")
        labelFB.config(text="fx2 =")
    elif varRadioBut.get() == 6:
        labetextoentrada.config(text="Secante introducir fx")
        labelA.config(text="a,b =")
        labelFA.config(text="fa = ")
        labelFB.config(text="fb =")



    print(varRadioBut.get())

#------------------------


#------------------funciones --------------------------
listaF = []
listaG = []

variabInfunc = StringVar()



variabA = StringVar()
variabB = StringVar()
variabFA = StringVar()
variabFB = StringVar()
variabM = StringVar()
variabFM = StringVar()

varRadioBut = IntVar()

#----------------variables--------------






#-------------fondo

frameRadioBut = Frame(ventana, pady=10)
frameRadioBut.pack()




RadioB1 = Radiobutton(frameRadioBut, text="Regla Falsa", variable=varRadioBut, value=1, command=lambda:impresionEnLabels()).grid(row=0, column=0, sticky="w")#pack(anchor= W)
#RadioB1.grid(row=0, column=0)
RadioB2 = Radiobutton(frameRadioBut, text="Punto Fijo", variable=varRadioBut, value=2, command=lambda:impresionEnLabels() ).grid(row=1, column=0, sticky="w")#pack(anchor=W)
#RadioB2.grid(row= 1, column=0)
RadioB3 = Radiobutton(frameRadioBut, text="Newton Raphson", variable=varRadioBut, value=3, command=lambda:impresionEnLabels()).grid(row=2, column=0, sticky="w")#pack(anchor=W)

RadioB4 = Radiobutton(frameRadioBut, text="Biseccion", variable=varRadioBut, value=4, command=lambda:impresionEnLabels()).grid(row=0, column=1, sticky="w")#pack(anchor= W)

RadioB5 = Radiobutton(frameRadioBut, text="Muller", variable=varRadioBut, value=5, command=lambda:impresionEnLabels() ).grid(row=1, column=1, sticky="w")#pack(anchor=W)

RadioB6 = Radiobutton(frameRadioBut, text="Secante", variable=varRadioBut, value=6, command=lambda:impresionEnLabels()).grid(row=2, column=1, sticky="w")#pack(anchor=W)

#--------------radio botones--------


frameIntoText = Frame(ventana, width=200, height=200, padx=50)
frameIntoText.pack()

intoText = Entry(frameIntoText, width=53, textvariable=variabInfunc)
intoText.grid(row=1, column=0, padx=10, pady=10)

labetextoentrada = Label(frameIntoText, text="elija un metodo")
labetextoentrada.grid(row=0, column=0, pady=5)

#-----------------area de texto de entrada-----------

frameVariab = Frame(ventana,width=200, height=200)
frameVariab.pack()

labelA = Label(frameVariab, text="a =")
labelA.grid(row=0, column=0, pady=5)

entryA = Entry(frameVariab, textvariable=variabA)
entryA.grid(row=0, column=1, padx=5, pady=5)

#labelB = Label(frameVariab, text="b =")
#labelB.grid(row=0, column=2, pady=5)

#entryB = Entry(frameVariab,textvariable=variabB)
#entryB.grid(row=0, column=3, padx=5, pady=5)

#--------------------------- entrada de variables A y B------------

labelFA = Label(frameVariab, text="f(a) =")
labelFA.grid(row=1, column=0, pady=5)

outFA = Entry(frameVariab, textvariable=variabFA)
outFA.grid(row=1, column=1, padx=5, pady=5)

labelFB = Label(frameVariab, text="f(b) =")
labelFB.grid(row=1, column=2, pady=5)

outFB = Entry(frameVariab, textvariable=variabFB)
outFB.grid(row=1, column=3, padx=5, pady=5)

#---------------- salida de respuesta Fa y Fm-------

frameAreaYBoton = Frame(ventana)
frameAreaYBoton.pack()

botonresolver = Button(frameAreaYBoton, text="Resolver", command=lambda:funVariables(variabInfunc.get(), variabA.get()))
botonresolver.grid(row=0, column=0, padx=10, pady=10)

areatexo = Text(frameAreaYBoton, width=70, height=5)
areatexo.grid(row=1, column=0, padx=10, pady=10)
areatexo.delete("1.0", END)


#---------------------area de respuestas---------------

frameRespuesta = Frame(ventana, pady=10)
frameRespuesta.pack()

labelM = Label(frameRespuesta, text="m =")
labelM.grid(row=1, column=0, pady=5)

outM = Entry(frameRespuesta,textvariable=variabM)
outM.grid(row=1, column=1, padx=5, pady=5)

labelFM = Label(frameRespuesta, text="f(m) =")
labelFM.grid(row=1, column=2, pady=5)

outFM = Entry(frameRespuesta, textvariable=variabFM)
outFM.grid(row=1, column=3, padx=5, pady=5)

#------------------------area de la respuesta y el error



ventana.mainloop()

#-----------------------fin de la ventana-----------------