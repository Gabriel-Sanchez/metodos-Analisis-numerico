from Metodos.funcionesRespuesta import *

def funcionMuller(textfunc, x1, x2):
    
    listaIteraciones = []

    fx = funcResp(textfunc, float(x2))
    fx = float(fx[0])

    df = float(Dg(textfunc, float(x2)))

    x3 = x2 - (fx / df)

    fxo = funcResp(textfunc, float(x2))
    fxo = float(fxo[0])

    # variabFB.set(fx)
    # variabFA.set(fxo)

    fx4 = fx

    i = 0

    while (abs(fx4)) > 0.00000001:
        y1 = funcResp(textfunc, float(x1))
        y1 = float(y1[0])

        y2 = funcResp(textfunc, float(x2))
        y2 = float(y2[0])

        y3 = funcResp(textfunc, float(x3))
        y3 = float(y3[0])

        c1 = ((y2 - y1) / (x2 - x1))
        c2 = ((y3 - y2) / (x3 - x2))

        d1 = ((c2 - c1) / (x2 - x1))

        s = (c2 + (d1 * (x3 - x2)))

        x4 = (x3 - ((2 * y3) / (2 + (sgn(s) * (((s ** 2) -4 * y3 * d1) ** (1 / 2))))))

        x1 = x2
        x2 = x3
        x3 = x4

        i = i + 1

        fx4 = funcResp(textfunc, float(x4))
        fx4 = float(fx4[0])

        infoAImprimir = str(i) + "            \t " + str(round(x4, 13)) + "       \t\t" + str(round(fx4, 13)) + "\n"
        
        # areatexo.insert(str(float(i)), infoAImprimir)
        listaIteraciones.append(infoAImprimir)

        print(f"intento : {i}  error {fx4}")

    # variabM.set(x4)
    # variabFM.set(fx4)
    
    return { 'M':x4, 'FM':fx4, 'FB':fx, 'FA':fxo, 'ListIteraciones':listaIteraciones }



resp = funcionMuller('( x ^ 3 ) + ( 4 * ( x ^ 2 ) ) - 10',1,2)

# print(resp['M']) 
# print(resp) 
print() 

for i in resp['ListIteraciones']:
    print(i)