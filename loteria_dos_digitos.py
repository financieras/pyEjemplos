from random import randint
def loteria():
    a=randint(1,9)        #empieza en 1 para evitar valores inferiores a 10
    while True:
        b=randint(0,9)
        if b!=a: break
    return a*10+b
print(loteria())