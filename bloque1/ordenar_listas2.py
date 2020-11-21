#general números aleatorios en una lista y 
# ordenarlos sin usar sort
import random
lista = random.sample(range(10, 99), 9)                #creamos una lista de 9 números aleatorios entre 10 y 99 sin repetición
print(lista)                                           #imprimimos la lista aleatoria
for i in range(len(lista),1,-1):                       #bucle que va de la longitud de la lista hasta 1 de forma descendente: 9,8,7,6,5,4,3,2,1
    print('~'*40)
    print('i=',i)
    rango=lista[0:i]                                   #creamos una sublista que inicialmente tendrá la misma longitud que lista pero luego tendrá cada vez un número menos ya que el último se va fijando
    print('rango: ',rango)
    indice=rango.index(max(rango))                     #calculamos el índice que ocupa el máximo valor de la sublista
    print('indice=',indice)
    lista[indice],lista[i-1]=lista[i-1],lista[indice]  #permutamos los lugares que ocupan el máximo número de la sublista y el último valor de la sublista
    print('lista permutada=',lista)
print(lista)                                           #imprimimos la lista ya completamente ordenada de menor a mayor
