import csv

with open('ejemplo.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Los nombres de las columnas son {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} trabaja en el departamento de {row[1]} y nació en {row[2]}.')
            line_count += 1
    print(f'Procesadas {line_count} líneas.')