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

a = split("test,test2,test3\n",',')

print (a)