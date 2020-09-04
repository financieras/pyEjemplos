import random
def juega():
    global numero_elegido
    for _ in range(4):
        numero_elegido=int(input('Introduzca un número entre 1 y 40: '))
        if numero_elegido<numero_secreto: print('El número secreto es mayor.')
        elif numero_elegido>numero_secreto: print('El número secreto es menor.')
        else: break
    return numero_elegido
def comprueba(numero_elegido,numero_secreto):
    if numero_elegido==numero_secreto: print('Felicidades: ha adivinado el número secreto.')
    else: print('Esta vez no lo adivinó: el número secreto era ',str(numero_secreto))
numero_secreto=random.randint(1,40)
numero_elegido=juega()
comprueba(numero_elegido, numero_secreto)