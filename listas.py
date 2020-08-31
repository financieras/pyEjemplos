#Una lista es un conjunto iterable de datos ordenados que van entre corchetes []
[]                                          #una lista vacía
[10, 15, 12]	                                #una lista de tres elementos con números enteros
['azul', 'rojo', 'verde', 'amarillo']       #una lista con strings
[4, 'lunes', 3.14, True, None]              #admite cualquier valor
comida=['spagueti','pollo','tarta']         #asignación a una variable
print(comida)                               # ['spagueti', 'pollo', 'tarta']
comida[0]                                   #'spagueti'   se comienza por el índice=0             
comida[1]                                   #'pollo'
comida[2]                                   #'tarta'
comida[0]='espagueti'                       #reemplazando un elemento
print(comida)                               # ['espagueti', 'pollo', 'tarta']
print(type(comida))                         # <class 'list'>
lista=[comida,23,True,15.60]                #podemos incluir una lista dentro de una lista
print(lista)                                #[['espagueti', 'pollo', 'tarta'], 23, True, 15.6]
print('~'*40) ####################################################################################
bebida=['agua','vino','cerveza']
menu=[comida,bebida]                        #una lista que incluye dos listas
print(menu)                     #[['espagueti', 'pollo', 'tarta'], ['agua', 'vino', 'cerveza']]
print(menu[1][2])                           #'cerveza'
print(comida[len(comida)-1]==comida[-1])    #True
oferta=comida+bebida
print(oferta)                   #['espagueti', 'pollo', 'tarta', 'agua', 'vino', 'cerveza']
lista_completa=['a','b','c','d','e',1,2,3,4]
lista_letras=lista_completa[0:5]            #['a', 'b', 'c', 'd', 'e']
lista_numeros=lista_completa[5:9]           #[1, 2, 3, 4]
print(lista_letras)
print(lista_numeros)
print(lista_completa[:5])                   #['a', 'b', 'c', 'd', 'e']
print(lista_completa[5:])                   #[1, 2, 3, 4]
print(lista_completa[-4:])                  #[1, 2, 3, 4]
print(lista_completa[1::2])                 #['b', 'd', 1, 3]
print('~'*40) ####################################################################################
mi_rango=range(10)
print(mi_rango)               #range(0, 10)
print(type(mi_rango))         #<class 'range'>
numeros=list(range(10))
print(numeros)                #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ceros=[0]*10
print(ceros)                  #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(len(ceros))             #10
del oferta[-2]                #eliminamos el vino
print(oferta)                 #['espagueti', 'pollo', 'tarta', 'agua', 'cerveza']
oferta.append('limonada')     #añadimos al final un elemento
print(oferta)                 #['espagueti', 'pollo', 'tarta', 'agua', 'cerveza', 'limonada']
del ceros[2:]                 # eliminamos desde el elemento de indice 2 incluido hasta el final
print(ceros)                  #[0, 0]
print('tarta' in oferta)      #True
print('fruta' in oferta)      #False
print(oferta[::-1])           #['limonada', 'cerveza', 'agua', 'tarta', 'pollo', 'espagueti']