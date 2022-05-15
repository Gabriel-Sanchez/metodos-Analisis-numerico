from funcionesRespuesta import *

def funcionPuntoFijo(textfx, textgx, x):
    
    listaIteraciones = []
    
    i = 0

    fx = funcResp(textfx, float(x))
    fx = float(fx[0])

    dg = float(Dg(textgx, float(x)))
    print("la derivada de dgx =", dg)

    # variabFA.set(fx)
    # variabFB.set(dg)

    if abs(dg) < 1:
        print("la derivada es menor que 1")
        while (abs(fx)) > 0.00000001:
            print("sigue siendo mayor")
            gx = funcResp(textgx, float(x))
            gx = float(gx[0])
            print("x va a tomar el valor de ", gx)
            x = round(gx, 14)

            fx = funcResp(textfx, float(x))
            fx = float(fx[0])
            i = i + 1
            infoAImprimir = str(i) + "  \t   " + str(round(x, 13)) + "    \t\t" + str(round(fx, 13)) + "    \t\t" + str(round(gx, 13)) + "\n"
            # areatexo.insert(str(float(i)), infoAImprimir)
            listaIteraciones.append(infoAImprimir)
            print(f"intento : {i}  error {fx}")
        print("la raiz es :", x, " con el error de  :", fx)
        # variabM.set(x)
        # variabFM.set(fx)
        
        return { 'M':x, 'FM':fx, 'FB':fx, 'FA':dg, 'ListIteraciones':listaIteraciones }
        

    else:

        print("error ")
        # areatexo.insert("1.0", "Error, no hay convergencia con x0")
        # variabM.set("")
        # variabFM.set("")
        listaIteraciones.append("")
        
        return { 'M':0, 'FM':0, 'FB':fx, 'FA':dg, 'ListIteraciones':listaIteraciones }


resp = funcionPuntoFijo('( x ^ 3 ) + ( 4 * ( x ^ 2 ) ) - 10',1,2)

# print(resp['M']) 
# print(resp) 
print() 

for i in resp['ListIteraciones']:
    print(i)