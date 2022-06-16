from Metodos.funcionesRespuesta import *

def funcionBiseccion(textfunc, a, b):
    
    listaIteraciones = []
    
    # fa = funcResp(textfunc, float(a))
    # fb = funcResp(textfunc, float(b))

    # fa = float(fa[0])
    # fb = float(fb[0])
    
    x = float(a)
    fa = eval(textfunc)
    x = float(b)
    fb = eval(textfunc)

    # variabFA.set(fa)
    # variabFB.set(fb)

    i = 0

    #m = b - ((fb * (b - a)) / (fb - fa))

    m = (a + (b - a) / 2)

    # fm = funcResp(textfunc, float(m))
    # fm = float(fm[0])
    
    x = float(m)
    fm = eval(textfunc)

    if (fa * fb) < 0:
        while (abs(fm)) > 0.00000001:
            if (fa * fm) > 0:
                a = m
                fa = fm
            else:
                b = m
                fb = fm

            #m = b - ((fb * (b - a)) / (fb - fa))

            m = (a + (b - a) / 2)

            # fm = funcResp(textfunc, float(m))
            # fm = float(fm[0])
            
            x = float(m)
            fm = eval(textfunc)

            i = i + 1

            infoAImprimir = str(i) + "            \t " + str(round(m, 13)) + "       \t\t" + str(round(fm, 13)) + "\n"
            # areatexo.insert(str(float(i)), infoAImprimir)
            listaIteraciones.append(infoAImprimir)

            print(f"intento : {i}  error {fm}")
        print("la raiz es :", m, " con el error de  :", fm)
        # variabM.set(m)
        # variabFM.set(fm)
        return { 'M':m, 'FM':fm, 'FB':fb, 'FA':fa, 'ListIteraciones':listaIteraciones }


    else:

        print("error ")
        listaIteraciones.append("")
        
        # areatexo.insert("1.0", "Error, no hay raiz entre los puntos a y b")
        # variabM.set("")
        # variabFM.set("")
        
        return { 'M':0, 'FM':0, 'FB':fb, 'FA':fa, 'ListIteraciones':listaIteraciones }
        


# resp = funcionBiseccion('( x ^ 3 ) + ( 4 * ( x ^ 2 ) ) - 10',1,2)

# # print(resp['M']) 
# # print(resp) 
# print() 

# for i in resp['ListIteraciones']:
#     print(i)