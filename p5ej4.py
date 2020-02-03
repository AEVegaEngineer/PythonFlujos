def todoMIN(txt):
    res= " "
    i=0
    while i<len(txt):
        if txt[i]>"A" and txt[i]<"Z":
            res= res+ chr(ord(txt[i]+32))
        else:
            res=res+txt[i]
        i+=1
    return res ## return res!!

def esLetra(let):
    res=False
    if let>="a" and let<="z":
        res=True
    return res

def principioFin(txt):
    LTXT=len(txt)
    i=0
    j=len(txt)-1
    primera=""
    ultima=""
    
    while not esLetra (txt[i]): # si no es letra vuelve a entrar
        print(str(i)+" no es letra: "+txt[i])
        i+=1
    while esLetra(txt[i]) and i<j:
        print(str(i)+" es letra: "+txt[i])
        primera=primera+(txt[i])
        i+=1
        
        
    while not esLetra(txt[j]) and j>0:
        j=j-1
        
    while esLetra(txt[j]) and j>0:
        ultima=(txt[j])+ultima
        j=j-1
        
    if primera==ultima:
        res="Si cumple"
    else:
        res="No cumple"
        
    return res

def main():
    t=input("Ingrese texto:")
    Min=todoMIN(t)
    print(principioFin(t))
    
    
main()
    