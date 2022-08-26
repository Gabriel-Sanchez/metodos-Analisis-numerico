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


# def funcionMuller(textfunc, x1, x2):

#     fx = funcResp(textfunc, float(x2))
#     fx = float(fx[0])

#     df = float(Dg(textfunc, float(x2)))

#     x3 = x2 - (fx / df)

#     fxo = funcResp(textfunc, float(x2))
#     fxo = float(fxo[0])

#     variabFB.set(fx)
#     variabFA.set(fxo)

#     fx4 = fx

#     i = 0

#     while (abs(fx4)) > 0.00000001:
#         y1 = funcResp(textfunc, float(x1))
#         y1 = float(y1[0])

#         y2 = funcResp(textfunc, float(x2))
#         y2 = float(y2[0])

#         y3 = funcResp(textfunc, float(x3))
#         y3 = float(y3[0])

#         c1 = ((y2 - y1) / (x2 - x1))
#         c2 = ((y3 - y2) / (x3 - x2))

#         d1 = ((c2 - c1) / (x2 - x1))

#         s = (c2 + (d1 * (x3 - x2)))

#         x4 = (x3 - ((2 * y3) / (2 + (sgn(s) * (((s ** 2) -4 * y3 * d1) ** (1 / 2))))))

#         x1 = x2
#         x2 = x3
#         x3 = x4

#         i = i + 1

#         fx4 = funcResp(textfunc, float(x4))
#         fx4 = float(fx4[0])

#         infoAImprimir = str(i) + "            \t " + str(round(x4, 13)) + "       \t\t" + str(round(fx4, 13)) + "\n"
#         areatexo.insert(str(float(i)), infoAImprimir)

#         print(f"intento : {i}  error {fx4}")

#     variabM.set(x4)
#     variabFM.set(fx4)




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



#-----------------------funcion que resuelve ------------

# def funcionReglaFalsa(textfunc, a, b):
#     fa = funcResp(textfunc, float(a))
#     fb = funcResp(textfunc, float(b))

#     fa = float(fa[0])
#     fb = float(fb[0])

#     variabFA.set(fa)
#     variabFB.set(fb)

#     i = 0

#     m = b - ((fb * (b - a)) / (fb - fa))

#     fm = funcResp(textfunc, float(m))
#     fm = float(fm[0])

#     if (fa * fb) < 0:
#         while (abs(fm)) > 0.00000001:
#             if (fa * fm) > 0:
#                 a = m
#                 fa = fm
#             else:
#                 b = m
#                 fb = fm

#             m = b - ((fb * (b - a)) / (fb - fa))
#             fm = funcResp(textfunc, float(m))
#             fm = float(fm[0])

#             i = i + 1

#             infoAImprimir = str(i) + "            \t " + str(round(m, 13)) + "       \t\t" + str(round(fm, 13)) + "\n"
#             areatexo.insert(str(float(i)), infoAImprimir)

#             print(f"intento : {i}  error {fm}")
#         print("la raiz es :", m, " con el error de  :", fm)
#         variabM.set(m)
#         variabFM.set(fm)

#     else:

#         print("error ")
#         areatexo.insert("1.0", "Error, no hay raiz entre los puntos a y b")
#         variabM.set("")
#         variabFM.set("")




#------------------funcion regla falsa----------

# def funcionBiseccion(textfunc, a, b):
#     fa = funcResp(textfunc, float(a))
#     fb = funcResp(textfunc, float(b))

#     fa = float(fa[0])
#     fb = float(fb[0])

#     variabFA.set(fa)
#     variabFB.set(fb)

#     i = 0

#     #m = b - ((fb * (b - a)) / (fb - fa))

#     m = (a + (b - a) / 2)

#     fm = funcResp(textfunc, float(m))
#     fm = float(fm[0])

#     if (fa * fb) < 0:
#         while (abs(fm)) > 0.00000001:
#             if (fa * fm) > 0:
#                 a = m
#                 fa = fm
#             else:
#                 b = m
#                 fb = fm

#             #m = b - ((fb * (b - a)) / (fb - fa))

#             m = (a + (b - a) / 2)

#             fm = funcResp(textfunc, float(m))
#             fm = float(fm[0])

#             i = i + 1

#             infoAImprimir = str(i) + "            \t " + str(round(m, 13)) + "       \t\t" + str(round(fm, 13)) + "\n"
#             areatexo.insert(str(float(i)), infoAImprimir)

#             print(f"intento : {i}  error {fm}")
#         print("la raiz es :", m, " con el error de  :", fm)
#         variabM.set(m)
#         variabFM.set(fm)

#     else:

#         print("error ")
#         areatexo.insert("1.0", "Error, no hay raiz entre los puntos a y b")
#         variabM.set("")
#         variabFM.set("")

#---------------funcion Biseccion-------------


# def funcionPuntoFijo(textfx, textgx, x):
#     i = 0

#     fx = funcResp(textfx, float(x))
#     fx = float(fx[0])

#     dg = float(Dg(textgx, float(x)))
#     print("la derivada de dgx =", dg)

#     variabFA.set(fx)
#     variabFB.set(dg)

#     if abs(dg) < 1:
#         print("la derivada es menor que 1")
#         while (abs(fx)) > 0.00000001:
#             print("sigue siendo mayor")
#             gx = funcResp(textgx, float(x))
#             gx = float(gx[0])
#             print("x va a tomar el valor de ", gx)
#             x = round(gx, 14)

#             fx = funcResp(textfx, float(x))
#             fx = float(fx[0])
#             i = i + 1
#             infoAImprimir = str(i) + "  \t   " + str(round(x, 13)) + "    \t\t" + str(round(fx, 13)) + "    \t\t" + str(round(gx, 13)) + "\n"
#             areatexo.insert(str(float(i)), infoAImprimir)
#             print(f"intento : {i}  error {fx}")
#         print("la raiz es :", x, " con el error de  :", fx)
#         variabM.set(x)
#         variabFM.set(fx)

#     else:

#         print("error ")
#         areatexo.insert("1.0", "Error, no hay convergencia con x0")
#         variabM.set("")
#         variabFM.set("")





#--------------------funcion punto fijo---------

# def funcionNewtonRaphson(textfx, x):
#     i = 0

#     fx = funcResp(textfx, float(x))
#     fx = float(fx[0])

#     dg = float(Dg(textfx, float(x)))
#     print("la derivada de dgx =", dg)

#     variabFA.set(fx)
#     variabFB.set(dg)

#     if abs(dg) != 0:
#         print("la derivada es diferente de 0")




#         while (abs(fx)) > 0.00000001:
#             print("sigue siendo mayor")
#             #gx = funcResp(textgx, float(x))
#             #gx = float(gx[0])
#             #print("x va a tomar el valor de ", gx)
#             #x = round(gx, 14)

#             fx = funcResp(textfx, float(x))
#             fx = float(fx[0])

#             df = float(Dg(textfx, float(x)))

#             x = x - (fx / df)

#             i = i + 1
#             infoAImprimir = str(i) + "  \t   " + str(round(x, 13)) + "    \t\t" + str(round(fx, 13)) + "    \t\t" + str(round(df, 13)) + "\n"
#             areatexo.insert(str(float(i)), infoAImprimir)
#             print(f"intento : {i}  error {fx}")
#         print("la raiz es :", x, " con el error de  :", fx)
#         variabM.set(x)
#         variabFM.set(fx)

#     else:

#         print("error ")
#         areatexo.insert("1.0", "Error, no hay convergencia con x0")
#         variabM.set("")
#         variabFM.set("")


#-------------------newton Raphson----------


# def funcionSecante(textfunc, a, b):
#     fa = funcResp(textfunc, float(a))
#     fb = funcResp(textfunc, float(b))

#     fa = float(fa[0])
#     fb = float(fb[0])

#     variabFA.set(fa)
#     variabFB.set(fb)

#     i = 0

#     m = b - ((fb * (b - a)) / (fb - fa))

#     fm = funcResp(textfunc, float(m))
#     fm = float(fm[0])


#     while (abs(fm)) > 0.00000001:
#         print("sigue siendo mayor")
#         # gx = funcResp(textgx, float(x))
#         # gx = float(gx[0])
#         # print("x va a tomar el valor de ", gx)
#         # x = round(gx, 14)
#         b = a
#         fb = fa
#         a = m
#         fa = fm

#         m = b - ((fb * (b - a)) / (fb - fa))


#         fm = funcResp(textfunc, float(m))
#         fm = float(fm[0])

#         #df = float(Dg(textfunc, float(x)))

#         #x = x - (fx / df)

#         i = i + 1
#         infoAImprimir = str(i) + "  \t   " + str(round(m, 13)) + "    \t\t" + str(round(fm, 13))  + "\n"
#         areatexo.insert(str(float(i)), infoAImprimir)
#         print(f"intento : {i}  error {fm}")
#     print("la raiz es :", m, " con el error de  :", fm)
#     variabM.set(m)
#     variabFM.set(fm)


#---------------- metodo secante ----------



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