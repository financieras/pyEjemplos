import random
lista=['a','b','c','d','e','f','g','h','i','j']
n=len(lista)                         #número de elementos totales de lista
m=random.randint(2,n)                #número de elementos a extraer
print("Lista de partida: ",lista)
random.shuffle(lista)
print('De los {} elementos elegimos {} aleatoriamente: {}'.format(n,m,lista[:m]))
