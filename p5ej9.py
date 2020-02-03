def ContarPal(txt):
    i=0
    j=0
    ContPal=0
    LT=len(txt)
    while i<LT:
        while i<LT and not esLetra(txt[i]): #cuando no es letra entra 
            i+=1
            j=i
        while j<LT and esLetra(txt[j]): #cuando es letra se queda
            j+=1
            
        if j<=LT: #si j<lt no entra directamente y no cuenta esa palabra
            ContPal+=1
        i=j
            
    return ContPal
        
def esLetra(let):
    res=False
    if (let>="A" and let<="Z") or (let>="a" and let<="z"):
        res=True
    return res
    
def PMinLong(txt):
    i=0
    j=0
    MinPal=" " 
    #MaxPal=" "
    LT=len(txt)
    while i<LT:
        while i<LT and not esLetra(txt[i]): #cuando no es letra entra 
            i+=1
            j=i
        while j<LT and esLetra(txt[j]): #cuando es letra se queda
            j+=1
            
        if j<=LT:
            if MinPal != " ":
                if len(MinPal)>len(txt[i:j]):
                    MinPal=txt[i:j]
            else:
                MinPal=txt[i:j]
        i=j
    return MinPal

def PMaxLong(txt):
    i=0
    j=0
    MaxPal=" " 
    #MaxPal=" "
    LT=len(txt)
    while i<LT:
        while i<LT and not esLetra(txt[i]): #cuando no es letra entra 
            i+=1
            j=i
        while j<LT and esLetra(txt[j]): #cuando es letra se queda
            j+=1
            
        if j<=LT:
            if MaxPal != " ":
                if len(MaxPal)<len(txt[i:j]):
                    MaxPal=txt[i:j]
            else:
                MaxPal=txt[i:j]
        i=j
    return MaxPal
    
    
def main():
    txt=input("Ingrese texto:")
    print("El texto contiene:", ContarPal(txt),"palabras")
    print("La palabra mas cortas es:",PMinLong(txt))
    print("La palabra mas larga es:",PMaxLong(txt))
main()