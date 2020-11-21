#Generar un número entero aleatorio entre 2 y 20. A este número le llamaremos target
#Generar una lista de números enteros entre -10 y 10. La lista puede tener desde un mínimo de dos elementos a un máximo de 6
#La lista debe contener dos números que sumados nos den el target
#El programa generará un target y una lista y verificará que se cumple la condición de la suma. En caso de que no se cumpla seguirá generando otro target y otra lista hasta conseguirlo. 
#La solución debe ser única. Solo puede haber un par de número que sumados den el target
#Ejemplo 1: [-8, 1, 4, 9] Target: 10
#Ejemplo 2: [-5, -4, 3, 5, 8] Target: 4
import random
def genera():
    while True:
        lista = random.sample(range(-10, 11), random.randint(2,6))
        lista.sort()
        #print(lista)
        target=random.randint(2,21)
        #print('Target:',target)
        if comprueba(lista, target):
            print(lista,'Target:',target)
            break
def comprueba(lista,target):
    cumple=0
    for i,v in enumerate(lista):
        for j,w in enumerate(lista):
            if i!=j and v+w==target:cumple+=1
    if cumple==2: 
        return True
genera()
genera()
genera()
genera()
genera()
genera()