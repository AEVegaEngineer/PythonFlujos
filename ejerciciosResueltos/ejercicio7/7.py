def agregar():
    nombre=input("Ingrese nombre:")
    apellido=input("Ingrese apellido:")
    dni=input("Ingrese DNI:")
    # abris el archivo con parámetro de lectura
    f = open("persona.csv", 'r')
    records = []
    for line in f:
        for word in line.split():
            word = word.replace(","," ")
            word = word.replace(".","")
            word = word.split()            
            records.append(word) 
    f.close()
    encontrado = 0
    for row in records:
        if row[2] == dni:
            encontrado = 1
    if encontrado == 1:
        return "Error, DNI ya existe"
    else:
        f = open("persona.csv", 'a')
        linea = nombre+","+apellido+","+dni+'\n'
        f.write(linea)
        f.close()

    return "Persona ingresada correctamente"
 
def eliminar():
    dni=input("Ingrese DNI a eliminar:")
    f = open("persona.csv", 'r')
    records = []
    for line in f:
        contador = 0
        for word in line.split():
            contador+=1
            word = word.replace(","," ")
            word = word.replace(".","")
            word = word.split()            
            if word[2] != dni:
                records.append(line) 
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
        for word in line.split():
            word = word.replace(","," ")
            word = word.replace(".","")
            word = word.split()       
            if word[1] == entrada or word[2] == entrada:
                encontrado = 1
                return (word[0]+" "+word[1]+" "+ word[2])
                break
    if encontrado == 0:
        return("No existe persona con ese apellido o DNI")
def ordenarArchivoPor():
    entrada=input("Ingrese el campo por el que desea ordenar: nombre[1], apellido[2], DNI[3]: ")

    f = open("persona.csv", 'r')
    records = []
    for line in f:
        for word in line.split():
            word = word.replace(","," ")
            word = word.replace(".","")
            word = word.split()            
            records.append(word) 
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
        print (line)
    f.close()
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