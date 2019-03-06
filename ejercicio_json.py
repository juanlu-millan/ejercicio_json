import json
with open("champions.json") as fichero:
    doc=json.load(fichero)

from funciones import listanombres
from funciones import goleadores
from funciones import fechapartido

while (True):
    print('''
Elige una opcion:
1.Lista el nombre de todos los equipos de la Champions
2.Cuenta la cantidad de victorias,empates y derrotas del equipo de elijas
3.Pide un equipo y te dice la cantidad de goles que ha marcado
4.Introduce la fecha del partido,muestra los equipos y el resultado final
5.Top 5 de máximos goleadores
0-Salir''')
    opcion=int(input("Opcion: "))

    if opcion==1:
        # Lista el nombre de todos los equipos de la Champions

        for equipos in listanombres(doc):
            print("-",equipos)

# Cuenta la cantidad de victorias,empates y derrotas del equipo de elijas

# Pide un equipo y te dice la cantidad de goles que ha marcado

        # Introduce la fecha del partido,muestra los equipos y el resultado final
    if opcion==4:
        fecha = input("Dime una fecha (año-mes-día): ")
        print("")
        print ("Resultados de %s"%fecha)
        for equipo1,equipo2,resultado1,resultado2 in fechapartido(fecha,doc):
            print (equipo1,"-",equipo2,"(",resultado1,"-",resultado2,")")

        # Top 5 de máximos goleadores
    elif opcion==5:
        print ("TOP 5 de UCF:")
        for jugador,gol in goleadores(doc):
            print(jugador,"-",gol)

    elif opcion == 0:
        break;
    else:
        print ("Esa opcion no existe")
