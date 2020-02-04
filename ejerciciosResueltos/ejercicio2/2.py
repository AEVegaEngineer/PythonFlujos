import csv

with open('2.csv','r') as stop_words: 
    lineas = [linea.strip() for linea in stop_words]

for linea in lineas:
    print(linea)

#with open('2.csv') as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter=',')
    #line_count = 0
    #for row in csv_reader:
        #step = 0
        #for col in row:
        #    step+=1
        #    col
        #if line_count == 0:
        #    print(f'Los nombres de las columnas son {", ".join(row)}')
        #    line_count += 1
        #else:
        #    print(f'\t{row[0]} trabaja en el departamento de {row[1]} y nació en {row[2]}.')
        #    line_count += 1
    #print(f'Procesadas {line_count} líneas.')