#general números aleatorios en una lista y 
# ordenarlos sin usar sort
import random
lista = random.sample(range(10, 99), 9)
#lista=[9,8,7,6,5,4,3,2,1]
print(lista)
for j in range(len(lista)-1):
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]
print(lista)
