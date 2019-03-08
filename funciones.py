import json

# 1.Lista el nombre de todos los equipos de la Champions
def listanombres (doc):
    equipos=[]
    for partidos in doc["rounds"]:
        for partido in partidos["matches"]:
            if partido["team1"]["name"] not in equipos:
                equipos.append(partido["team1"]["name"])
    return equipos


# 2.Cuenta la cantidad de victorias,empates y derrotas del equipo de elijas
def balance(equipo,doc):
    victorias = 0
    empates = 0
    derrotas = 0
    for partidos in doc["rounds"]:
        for partido in partidos["matches"]:
            if partido["team1"]["name"] == equipo:
                if partido["score1"] > partido["score2"]:
                    victorias = victorias + 1
                if partido["score1"] == partido["score2"]:
                    empates = empates + 1
                if partido["score1"] < partido["score2"]:
                    derrotas = derrotas + 1
            if partido["team2"]["name"] == equipo:
                if partido["score2"] > partido["score1"]:
                    victorias = victorias + 1
                if partido["score2"] == partido["score1"]:
                    empates = empates + 1
                if partido["score2"] < partido["score1"]:
                    derrotas = derrotas + 1
    return victorias,empates,derrotas

# 3.Pide un equipo y te dice la cantidad de goles que ha marcado

def golesequipo (equipo,doc):
    goles = []
    for partidos in doc["rounds"]:
        for partido in partidos["matches"]:
            if partido["team1"]["name"] == equipo:
                goles.append(partido["score1"])
            if partido["team2"]["name"] == equipo:
                goles.append(partido["score2"])

    golestotales = 0
    for gol in goles:
        golestotales = gol + golestotales
    return golestotales

# 4.Introduce la fecha del partido,muestra los equipos y el resultado final
def fechapartido (fecha,doc):
    equipos1 = []
    equipos2 = []
    resultados1 = []
    resultados2 = []
    for partidos in doc["rounds"]:
        for partido in partidos["matches"]:
            if partido["date"]==fecha:
                equipo1 = partido["team1"]["name"]
                equipos1.append(equipo1)
                equipo2 = partido["team2"]["name"]
                equipos2.append(equipo2)
                resultado1 = partido["score1"]
                resultados1.append(resultado1)
                resultado2 = partido["score2"]
                resultados2.append(resultado2)
    return zip(equipos1,equipos2,resultados1,resultados2)


# 5.Top 5 de máximos goleadores
def goleadores (doc):
    goleadores = []
    goles = []
    totalgoles = []
    for partidos in doc["rounds"]:
        for partido in partidos["matches"]:
            if partido["score1"]>0:
                for goles in partido["goals1"]:
                    goleadores.append(goles["name"])
                    totalgoles.append(goleadores.count(goles["name"]))

            if partido["score2"]>0:
                for goles in partido["goals2"]:
                    goleadores.append(goles["name"])
                    totalgoles.append(goleadores.count(goles["name"]))


    totalgoles.reverse()
    goleadores.reverse()

    return topcinco(totalgoles,goleadores)

def topcinco(totalgoles,goleadores):
    jugadores = []
    goles = []
    for gol,jugador in zip(totalgoles,goleadores):
        if jugador not in jugadores:
            jugadores.append(jugador)
            goles.append(gol)

    golestop = sorted(goles)
    golestop.reverse()
    contador = 0
    golmaximo = golestop[0]

    cincotop = []
    for i in range(0,len(golestop)):
        if len(cincotop)>4:
            break;
        for jugador,gol in zip(jugadores,goles):
            if gol==golmaximo:
                cincotop.append(jugador)
                golestop.append(gol)
        golmaximo = golmaximo-1
    return zip(cincotop[0:5],golestop[0:5])
