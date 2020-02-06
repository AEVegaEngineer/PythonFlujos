import csv
import collections

def cabecera(archivo,cant,pmin,pmax):
    
    # abris el archivo con parámetro de lectura
    contador = 0
    palabras = []
    f = open(archivo, 'r')
    for line in f:
        for word in line.split():
            word = word.replace(",","")
            word = word.replace(".","")            
            if pmax>=len(word)>=pmin:                
                if contador < cant:
                    contador+=1
                    palabras.append(word)
    f.close()
    print (palabras)


def main():
    cant = 4
    pmin = 2
    pmax = 4
    cabecera('cuentos.txt',cant,pmin,pmax)
    
main()