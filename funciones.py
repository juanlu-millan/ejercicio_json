import json

def listanombres (doc):
    equipos=[]
    for partidos in doc["rounds"]:
        for partido in partidos["matches"]:
            if partido["team1"]["name"] not in equipos:
                equipos.append(partido["team1"]["name"])
    return equipos
