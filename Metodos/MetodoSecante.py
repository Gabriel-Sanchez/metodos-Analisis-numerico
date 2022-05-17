from Metodos.funcionesRespuesta import *

def funcionSecante(textfunc, a, b):
    
    listaIteraciones = []
    
    fa = funcResp(textfunc, float(a))
    fb = funcResp(textfunc, float(b))

    fa = float(fa[0])
    fb = float(fb[0])

    # variabFA.set(fa)
    # variabFB.set(fb)

    i = 0

    m = b - ((fb * (b - a)) / (fb - fa))

    fm = funcResp(textfunc, float(m))
    fm = float(fm[0])


    while (abs(fm)) > 0.00000001:
        print("sigue siendo mayor")
        # gx = funcResp(textgx, float(x))
        # gx = float(gx[0])
        # print("x va a tomar el valor de ", gx)
        # x = round(gx, 14)
        b = a
        fb = fa
        a = m
        fa = fm

        m = b - ((fb * (b - a)) / (fb - fa))


        fm = funcResp(textfunc, float(m))
        fm = float(fm[0])

        #df = float(Dg(textfunc, float(x)))

        #x = x - (fx / df)

        i = i + 1
        infoAImprimir = str(i) + "  \t   " + str(round(m, 13)) + "    \t\t" + str(round(fm, 13))  + "\n"
        # areatexo.insert(str(float(i)), infoAImprimir)
        listaIteraciones.append(infoAImprimir)

        print(f"intento : {i}  error {fm}")
    print("la raiz es :", m, " con el error de  :", fm)
    # variabM.set(m)
    # variabFM.set(fm)
    
    return { 'M':m, 'FM':fm, 'FB':fb, 'FA':fa, 'ListIteraciones':listaIteraciones }
    

resp = funcionSecante('( x ^ 3 ) + ( 4 * ( x ^ 2 ) ) - 10',1,2)

# print(resp['M']) 
# print(resp) 
print() 

for i in resp['ListIteraciones']:
    print(i)