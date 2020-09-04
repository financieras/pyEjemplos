from random import randint
lista=['a','b','c','d','e','f','g','h','i','j']
n=len(lista)                         #número de elementos totales de lista
listb=list(range(n))                 #creamos una lista con n números correlativos
m=randint(2,n)                       #número de elementos a extraer
print("Lista de partida: ",lista)
print(listb)
for i in range(n-1,1,-1):
    r=randint(0,i)
    listb[i],listb[r]=listb[r],listb[i]
print(listb)
extraida=[]
for i in range(m):
    extraida.append(lista[listb[i]])
print('De los {} elementos elegimos {} aleatoriamente: {}'.format(n,m,extraida))