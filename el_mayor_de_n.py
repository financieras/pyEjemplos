#Ejercicio el_mayor_de_n
#Generar aleatoriamente n números y decir cuál es el mayor o si son todos iguales. n va de 2 a 9
import random
def genera(n):
    numeros=[]
    for i in range(n): numeros.append(random.randint(0,9))
    return numeros
def lanza_proceso():
    distintos=True
    while distintos:
        n=random.randint(2,9)
        numeros=genera(n)
        if max(numeros)==min(numeros): print(numeros,"Son todos iguales."); distintos=False
        else: print(numeros,"El mayor es: ",max(numeros))
lanza_proceso()