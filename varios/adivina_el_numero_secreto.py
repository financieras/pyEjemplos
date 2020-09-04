import random
numero_secreto=random.randint(1,100)
while True:
    numero_elegido=int(input("Di un número entre 1 y 100: "))
    if numero_secreto<numero_elegido: print("El nº secreto es menor")
    elif numero_secreto>numero_elegido: print("El nº secreto es mayor")
    else: print("Felicidades, el nº secreto es {}.".format(numero_secreto)); break