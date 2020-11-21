import random

def genera():
    a=random.randint(0,10)
    b=random.randint(0,10)
    return comprueba(a,b)

def comprueba(a,b):
    if a+b >=10: return 'grande'
    else: return 'pequeño'


print(genera())