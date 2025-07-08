from Funciones import *
import json
import os

# Leer rankings anteriores si existen
if os.path.exists("ranking.json"):
    with open("ranking.json", "r") as f:
        lista_rankings = json.load(f)
else:
    lista_rankings = []

# Agregar el nuevo ranking
nuevo_ranking = crear_diccionario_ranking(datos_juego)
lista_rankings.append(nuevo_ranking)

# Guardar la lista actualizada
with open("ranking.json", "w") as f:
    json.dump(lista_rankings, f, indent=4)