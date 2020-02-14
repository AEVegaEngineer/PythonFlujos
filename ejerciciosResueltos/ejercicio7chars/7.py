def split(cadena,subcadena):
    lista = []
    substr = ""
    i=0
    for c in cadena:
        
        if c == subcadena or c == cadena[len(cadena)-1]:
            lista.append(substr)
            substr=""
        if c != subcadena:
            substr+=c
        i+=1
    return lista

def listaACadena(lista):      
    # inicializa cadena vacía
    cadena = "" 
    # itera en la lista y guarda en la cadena
    for ele in lista:  
        cadena += ele   
    # retorna la cadena  
    return cadena  

def agregar():
    nombre=input("Ingrese nombre:")
    apellido=input("Ingrese apellido:")
    dni=input("Ingrese DNI:")
    # abris el archivo con parámetro de lectura
    f = open("persona.csv", 'r')
    textoCompleto = f.readlines()
    f.close()
    if dni in textoCompleto:
        return "No puede guardar un DNI registrado"
    else:
        f = open("persona.csv", 'a')
        linea = nombre+","+apellido+","+dni+'\n'
        f.write(linea)
        f.close()
        return "Persona ingresada correctamente"
 
def eliminar():
    entrada=input("Ingrese DNI a eliminar:")
    f = open("persona.csv", 'r')
    records = []
    match = 0

    for line in f:
        linea = split(line,',')
        dni = list(linea[2])
        dni = listaACadena(dni)
        if dni != entrada:
            records.append(line)
        else:
            match = 1
    if match == 0:
        return "No se encontro a la persona"
    f.close()

    f = open("persona.csv", 'w')
    for linea in records:
        f.write(linea)
    f.close()
    return "Se ha eliminado a la persona"
def buscar():
    entrada=input("Ingrese DNI o apellido a buscar:")
    f = open("persona.csv", 'r')
    encontrado = 0
    for line in f:
        cadSeparada = split(line,',')
        if cadSeparada[1] == entrada:
            encontrado = 1
        if cadSeparada[2] == entrada:
            encontrado = 1
        if encontrado == 1:
            return (word[0]+" "+word[1]+" "+ word[2])
    if encontrado == 0:
        return("No existe persona con ese apellido o DNI")
def ordenarArchivoPor():
    entrada=input("Ingrese el campo por el que desea ordenar: nombre[1], apellido[2], DNI[3]: ")

    f = open("persona.csv", 'r')
    records = []
    for line in f:
        linea = split(line,',')
        records.append(linea)
    f.close()
    entrada = int(entrada)
    if entrada == 3:
        records.sort(key=lambda x:int(x[2]))
    else:
        records.sort(key=lambda x:x[entrada-1])
    f = open("persona.csv", 'w')
    for linea in records:
        f.write(linea[0]+","+linea[1]+","+linea[2]+"\n")
    f.close()
    return "Se ha reordenado el archivo exitosamente"
def mostrarArchivo():
    f = open("persona.csv", 'r')
    for line in f:
        if line != None:
            print (line)
    f.close()
    return ""
def salir():
    return "SALIR"
 
 
 
def elegirMenu(argument):
    switcher = {
        1: agregar,
        2: eliminar,
        3: buscar,
        4: ordenarArchivoPor,
        5: mostrarArchivo,
        6: salir
    }
    # Obtiene la función del switcher del diccionario
    func = switcher.get(argument, lambda: "Opción inválida")
    # Ejecuta la función
    print (func())

def mostrarMenu():
    print("\n")
    print ("1. AGREGAR REGISTRO")
    print("2. ELIMINAR REGISTRO")
    print("3. BUSCAR REGISTRO")
    print("4. ORDENAR ARCHIVO POR")
    print("5. MOSTRAR ARCHIVO")
    print("6. SALIR")

def main():
    eleccion=0
    while int(eleccion) != 6:
        mostrarMenu()
        eleccion=input("Ingrese opción:")
        elegirMenu(int(eleccion))
    
main()