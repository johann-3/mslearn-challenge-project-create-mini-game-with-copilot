import random

def obtener_entrada():
    eleccion = input("Ingrese piedra, papel o tijera: ").lower()
    while eleccion not in ['piedra', 'papel', 'tijera']:
        print("Entrada no válida, por favor ingrese piedra, papel o tijera")
        eleccion = input("Ingrese piedra, papel o tijera: ").lower()
    return eleccion

def obtener_eleccion_computadora():
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)

def determinar_ganador(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        return "Empate"
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijera') or \
        (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
        (eleccion_usuario == 'tijera' and eleccion_computadora == 'papel'):
        return "Usuario gana"
    else:
        return "Computadora gana"

# Inicializar las puntuaciones
puntuacion_usuario = 0
puntuacion_computadora = 0

for i in range(1, 4):
    eleccion_usuario = obtener_entrada()
    eleccion_computadora = obtener_eleccion_computadora()
    print("Usuario eligió:", eleccion_usuario)
    print("Computadora eligió:", eleccion_computadora)
    ganador = determinar_ganador(