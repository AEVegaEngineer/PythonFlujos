import csv
import collections

def generadora(ori,dest,cant):
    
    # abris el archivo con parámetro de lectura
    contador = 0
    palabras = []
    f = open(ori, 'r')
    for word in f:        
        word = word.replace(",","")
        word = word.replace(".","")            
        if pmax>=len(word)>=pmin:                
            if contador < cant and word not in palabras:
                contador+=1
                palabras.append(word)
    f.close()
    f = open(dest, 'w')
    for elm in palabras:
        linea = str(elm)+","
        print (linea)
        f.write(linea+'\n')
    f.close()

def main():
    ori = 'origen.txt'
    dest = 'destino.txt'
    cant = 5
    generadora(ori,dest,cant)
    
main()