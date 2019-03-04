import json
with open("champions.json") as fichero:
    doc=json.load(fichero)

from funciones import listanombres
# Lista el nombre de todos los equipos de la Champions

for equipos in listanombres(doc):
 print("-",equipos)

# Cuenta la cantidad de victorias,empates y derrotas del equipo de elijas

# Pide un equipo y te dice la cantidad de goles que ha marcado

# Introduce la fecha del partido,muestra los equipos y el resultado final

# Top 5 de máximos goleadores
