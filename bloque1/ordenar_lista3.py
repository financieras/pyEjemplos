#general números aleatorios en una lista y 
# ordenarlos sin usar sort
import random
lista = random.sample(range(10, 99), 9)                #creamos una lista de 9 números aleatorios entre 10 y 99 sin repetición
print(lista)
n=len(lista)
for i,v in enumerate(lista):                           #i es el index y v es el value, aunque nunca usamo v
    print('Index',i,'   Valor:',v)
    print('~'*40)
    print('i=',i)
    print('n-i=',n-i)
    rango=lista[0:n-i]                                 #creamos una sublista que inicialmente tendrá la misma longitud que lista pero luego tendrá cada vez un número menos ya que el último se va fijando
    print('rango: ',rango)
    maxIn=rango.index(max(rango))                      #calculamos el índice que ocupa el máximo valor de la sublista
    print('indice=',maxIn)
    lista[maxIn],lista[n-i-1]=lista[n-i-1],lista[maxIn]  #permutamos los lugares que ocupan el máximo número de la sublista y el último valor de la sublista
    print('lista permutada=',lista)
