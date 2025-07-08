nombres_columnas = ["nombre", "valor"]
matriz = [
    ["BOMBA", {"valor": 1}],
    ["X2", {"valor": 2}],
    ["DOBLE CHANCE", {"valor": 3}],
    ["PASAR", {"valor": 4}]
]

with open("powerups.csv", "w",encoding="utf-8") as archivo:
    archivo.write(",".join(nombres_columnas) + "\n")

    for fila in matriz :
        linea = ""
        for i in range(len(fila)):
            linea += str(fila[i])
            if i < (len(fila) -1 ):
                linea += ","
        archivo.write(linea +"\n")

