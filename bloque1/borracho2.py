# El caminar del borracho
# Un paseo aleatorio en dos dimensiones
# Se parte del punto (0,0) del plano cartesiano
# Cada paso que se da es de longitud r
# El ángulo con el que se da cada paso es aleatorio
import random
import math
import matplotlib.pyplot as plt
random.seed()
n=100000 # número de pasos
r=1 # longitud del paso
x1=y1=x2=y2=0 # punto de partida (x,y)=(0,0)
lista1x=[x1]
lista1y=[y1]
lista2x=[x2]
lista2y=[y2]
for i in range(n):
    angulo1=random.random()*360
    angulo2=random.random()*360
    x1+=r*math.cos(angulo1)
    y1+=r*math.sin(angulo1)
    x2+=r*math.cos(angulo2)
    y2+=r*math.sin(angulo2)
    lista1x.append(x1)
    lista1y.append(y1)
    lista2x.append(x2)
    lista2y.append(y2)

plt.plot(lista1x,lista1y)
plt.plot(lista2x,lista2y,'--r')
 
plt.show()