import csv
import collections

def frecuenciaPalabra(archivo):
    cnt = collections.Counter()
    # abris el archivo con parámetro de lectura
    f = open(archivo, 'r')
    for line in f:
        for word in line.split():
            word = word.replace(",","")
            word = word.replace(".","")            
            cnt[word] += 1 
    f.close()
    # Abrís el archivo en modo escritura
    f = open('frecuencias.csv', 'w')
    for elm in cnt:
        linea = elm+","+str(cnt[elm])
        print (linea)
        f.write(linea+'\n')
    f.close()

def main():
    frecuenciaPalabra('cuentos.txt')
    
main()