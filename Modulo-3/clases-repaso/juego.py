import random

jugador_a = random.randint(1, 100)
jugador_b = random.randint(1, 100)

print(f'puntos a = {jugador_a}, puntos b = {jugador_b}')

while True:
    who_atack = random.randint(1, 10)
    if who_atack % 2:
        print(f'{who_atack % 2} ataca A')
        defensa = random.randint(1, 50)
        if defensa % 0 != 0:
            jugador_b = jugador_b - random.randint(1, 3)
        
    else:
        print(f'{who_atack % 2} ataca B')
        jugador_a = jugador_a - random.randint(1, 3)

    if jugador_a <= 0:
        print('gabo el jugador B')
        break
    if jugador_b <= 0:
        print('gabo el jugador A')
        break

print('fin del juego')
