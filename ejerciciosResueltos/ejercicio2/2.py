import csv

def agregarMedia(archivo):
    # abris el csv con parámetro de lectura
    f = open('2.csv', 'r')
    lector = csv.reader(f)
    lista = list(lector)
    f.close()

    # Abrís el archivo en modo escritura
    f = open('2.csv', 'w')

    # iterás cada línea y escribís en el archivo lo mismo que hay en la lista
    for linea in lista:
        contador = 0
        total = 0
        lineaFormateada = ','.join(linea)
        f.write(lineaFormateada+'\n')
        for elemento in linea:
            #total= total + (int)elemento
            i = int(elemento)
            total+=i
            contador+=1
        promedio = total/contador
        f.write("promedio: "+str(promedio)+'\n')

    f.close()
def main():
    valores=agregarMedia('2.csv')
    
main()