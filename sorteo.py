#este es un sorteo
import random

participantes = []
cantidad = 0

while cantidad < 5:
    print("ingresa el nombre del participante")
    participante = input()
    participantes.append(participante)
    cantidad = cantidad+1
    if cantidad == 5:
        break
        
print("Haz llenado la lista para el concurso")
ganador = random.choice(participantes)
print("El ganador es: ", ganador)
    