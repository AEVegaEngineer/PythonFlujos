def calcularValores(archivo):
	file1 = open(archivo, 'r') 
	Lines = file1.readlines() 
	  
	count = 0
	total = 0
	valores = []
	for line in Lines: 
		valor = int(line.strip())
		valores.append(valor)
		total += valor
		count += 1

	resultado = [max(valores),min(valores),total/count,count]
	return resultado

def main():
    valores=calcularValores('1.txt')
    print(valores)   
    
main()