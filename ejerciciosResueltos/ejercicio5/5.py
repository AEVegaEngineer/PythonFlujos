import csv
import collections

def cabecera2(arch,cant,pmin,pmax):
    
    # abris el archivo con parámetro de lectura
    contador = 0
    palabras = []
    f = open(arch, 'r')
    for line in f:
        for word in line.split():
            word = word.replace(",","")
            word = word.replace(".","")            
            if pmax>=len(word)>=pmin and contador < cant and word not in palabras:               
                contador+=1
                palabras.append(word)
    f.close()
    f = open('resultado.csv', 'w')
    for elm in palabras:
        linea = str(elm)+","
        print (linea)
        f.write(linea+'\n')
    f.close()

def main():
    cant = 4
    pmin = 2
    pmax = 4
    arch = 'cuentos.txt'
    cabecera2(arch,cant,pmin,pmax)
    
main()