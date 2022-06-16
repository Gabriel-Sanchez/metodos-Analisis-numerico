from Metodos.funcionesRespuesta import *

def funcionMuller(textfunc, x1, x2):
    
    listaIteraciones = []

    x = float(x2)
    fx = eval(textfunc)

    df = float(Dg(textfunc, float(x2)))

    x3 = x2 - (fx / df)
    
    x = float(x2)
    fxo = eval(textfunc)

    fx4 = fx

    i = 0

    while (abs(fx4)) > 0.00000001:

        y1 =  ( float(x1))
        x=y1
        y1 =  ( eval(textfunc))
        
        y2 = ( float(x2))
        x=y2
        y2 = ( eval(textfunc))

        y3 = ( float(x3))
        x=y3
        y3 =  ( eval(textfunc))

        c1 =  ( ((y2 - y1) / (x2 - x1)) )
        c2 = ( ((y3 - y2) / (x3 - x2)))

        d1 = ( ((c2 - c1) / (x2 - x1)))

        s = ( (c2 + (d1 * (x3 - x2))))

        x4 =  ( (x3 - ((2 * y3) / (2 + (sgn(s) * (((s ** 2) -4 * y3 * d1) ** (1 / 2)))))))

        x1 = x2
        x2 = x3
        x3 = x4

        i = i + 1

        x = ( float(x4) )
        x = ( x )
        
        fx4 =  ( eval(textfunc))

        infoAImprimir = str(i) + "            \t " + str(round(x4, 13)) + "       \t\t" + str(round(fx4, 13)) + "\n"
        
        listaIteraciones.append(infoAImprimir)

    return { 'M':x4, 'FM':fx4, 'FB':fx, 'FA':fxo, 'ListIteraciones':listaIteraciones }
