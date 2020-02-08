import csv
import collections
import random

def generadora(ori,dest,cant):
    
    # abris el archivo con parámetro de lectura
    contador = 0
    palabras = []
    f = open(ori, 'r')

    line = next(f)
    for x in range(0, cant):    
        lines = open('origen.txt').read().splitlines()
        myline =random.choice(lines)
        palabras.append(myline)

    f.close()
    f = open(dest, 'w')
    for elm in palabras:
        print(elm)
        f.write(elm+'\n')
    f.close()

def main():
    ori=input("Ingrese archivo origen:")
    dest=input("Ingrese archivo destino:")
    cant=input("Ingrese cantidad:")
    generadora(ori,dest,int(cant))
    
main()