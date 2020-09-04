from random import randint
print(randint(1,6))

def dado(n=6):                               #valor por defecto para el tamaño del dado
    return randint(1,n)

print("Tiramos el dado y sale:", dado(100))  #si no ponemos argumento se toma el valor por defecto