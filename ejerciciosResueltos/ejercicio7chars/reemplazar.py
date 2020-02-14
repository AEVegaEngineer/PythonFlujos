#reemplaza una caracter X por otro Y de una cadena CAD
def reemplazarCaracter(CAD,X,Y):    
    # cambia el string a lista
    CAD  = list(CAD)
    # busca el caracter a cambiar
    limiteInferior = 0
    posicion = 0
    for c in CAD:
        for xi in X:
            if c == xi:
                limiteInferior = posicion
        posicion+=1
    # cambia el caracter que quieres cambiar
    CAD[Y] = "T"
    # convert the list back to a string. 
    CAD = "".join(CAD)