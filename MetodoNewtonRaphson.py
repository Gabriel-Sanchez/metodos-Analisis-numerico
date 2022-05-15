from funcionesRespuesta import *

def funcionNewtonRaphson(textfx, x):
    
    listaIteraciones = []
    
    i = 0

    fx = funcResp(textfx, float(x))
    fx = float(fx[0])

    dg = float(Dg(textfx, float(x)))
    print("la derivada de dgx =", dg)

    # variabFA.set(fx)
    # variabFB.set(dg)

    if abs(dg) != 0:
        print("la derivada es diferente de 0")




        while (abs(fx)) > 0.00000001:
            print("sigue siendo mayor")
            #gx = funcResp(textgx, float(x))
            #gx = float(gx[0])
            #print("x va a tomar el valor de ", gx)
            #x = round(gx, 14)

            fx = funcResp(textfx, float(x))
            fx = float(fx[0])

            df = float(Dg(textfx, float(x)))

            x = x - (fx / df)

            i = i + 1
            infoAImprimir = str(i) + "  \t   " + str(round(x, 13)) + "    \t\t" + str(round(fx, 13)) + "    \t\t" + str(round(df, 13)) + "\n"
            # areatexo.insert(str(float(i)), infoAImprimir)
            listaIteraciones.append(infoAImprimir)
            print(f"intento : {i}  error {fx}")
        print("la raiz es :", x, " con el error de  :", fx)
        # variabM.set(x)
        # variabFM.set(fx)
        
        return { 'M':x, 'FM':fx, 'FB':dg, 'FA':fx, 'ListIteraciones':listaIteraciones }
        

    else:

        print("error ")
        listaIteraciones.append('')
        
        # areatexo.insert("1.0", "Error, no hay convergencia con x0")
        # variabM.set("")
        # variabFM.set("")
        
        return { 'M':x, 'FM':fx, 'FB':dg, 'FA':fx, 'ListIteraciones':listaIteraciones }


resp = funcionNewtonRaphson('( x ^ 3 ) + ( 4 * ( x ^ 2 ) ) - 10',1)

# print(resp['M']) 
# print(resp) 
print() 

for i in resp['ListIteraciones']:
    print(i)
