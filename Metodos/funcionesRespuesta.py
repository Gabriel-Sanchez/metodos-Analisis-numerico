import math
from math import cos, sin, tan
import decimal


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


def Dg(gx, x):
    h = 0.000000000000001
    # fxmenosh = funcResp(gx, (x - h))
    
    x = (x - h)
    fxmenosh = eval(gx)
    
    x = (x + h)
    # fxmash = funcResp(gx, (x + h))
    fxmash = eval(gx)
    
    # fxmash = float(fxmash[0])
    # fxmenosh = float(fxmenosh[0])

    Resp = ( fxmash - fxmenosh ) / (2 * h)
    return Resp

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return (-1)
    else:
        return 0
