#JUEGO: piedra, papel o tijera
import random

opciones = ['piedra', 'papel', 'tijera']

while True:
    print('------------------------------------------')
    print('--- Juego: Piedra, Papel o Tijera ---')
    print('Elige una opción:')
    print('1. Piedra')
    print('2. Papel')
    print('3. Tijera')
    print('4. Salir')
    eleccion = input('Ingresa el número de tu opción: ')
    if eleccion == '4':
        print('¡Gracias por jugar!')
        break
    if eleccion not in ['1', '2', '3']:
        print('Número inválido. Intenta de nuevo.')
        continue
    jugador = opciones[int(eleccion)-1]
    computadora = random.choice(opciones)
    print(f'Tú elegiste: {jugador}')
    print(f'La computadora eligió: {computadora}')
    if jugador == computadora:
        print('¡Empate!')
    elif (jugador == 'piedra' and computadora == 'tijera') or \
         (jugador == 'papel' and computadora == 'piedra') or \
         (jugador == 'tijera' and computadora == 'papel'):
        print('¡Ganaste!')
    else:
        print('¡Perdiste!')
