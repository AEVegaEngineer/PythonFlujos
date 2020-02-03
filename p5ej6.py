def palindroma(fra): #de atras hacia adelnate se lee igual 
    SinEspacio=sinEspacio(fra)
    Alreves=SinEspacio[::-1]
    if SinEspacio==Alreves:
        res=True
    else:
        res=False
    return res
    
def todoMAY(letra): #pasa una letra q paso x parametro solo esa a may 
    i=chr(ord(letra)-32)
    return i
    
def sinEspacio(fra): ##!!! con for las cosas q no sean las q estan definidas ahi se las saltea 
    res="" # muy importante q no haya espacio en el medio 
    #for i in fra:
    for i in range (0,len(fra)):
        if fra[i]>="A" and fra[i]<="Z":
            res=str(res+fra[i])
        elif fra[i]>="a" and fra[i]<="z":
            res=str(res+todoMAY(fra[i]))
        elif fra[i]=="á" or fra[i]=="é" or fra[i]=="í" or fra[i]=="ó" or fra[i]=="ú":
            res=str(res+sinTilde(fra[i]))
    return res 
    
def sinTilde(let):
    if let=="á":
        res="A"
    elif let=="é":
        res="E"
    elif let=="í":
        res="I"
    elif let=="ó":
        res="O"
    elif let=="ú":
        res="U"
    return res

def main():
    fra=input("Ingrese frase:")
    if palindroma(fra)==True:
        print("Si se cumple")
    else:
        print("No se cumple")
main()