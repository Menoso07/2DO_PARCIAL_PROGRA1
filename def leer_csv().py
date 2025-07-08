with open("Preguntas.csv", "r") as archivo :
    matriz = []
    nombres_columnas = archivo.readline().strip().split(",")

    for linea in archivo:

        linea = linea.rstrip("\n")
        fila = []
        valores = linea.split(",")

        for valor in valores :

            if valor.isdigit() :
                fila.append(int(valor))
            else :
                fila.append(valor)

        matriz.append(fila)

print(nombres_columnas)

for fila in matriz:
    print(fila)