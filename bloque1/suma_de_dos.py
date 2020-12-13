'''
Generar un número entero aleatorio entre 2 y 20. A este número le llamaremos target
Generar una lista de números enteros entre -10 y 10. La lista puede tener desde un mínimo de dos elementos a un máximo de 6
La lista debe contener dos números que sumados nos den el target
El programa generará un target y una lista y verificará que se cumple la condición de la suma. En caso de que no se cumpla seguirá generando otro target y otra lista hasta conseguirlo. 
La solución debe ser única. Solo puede haber un par de número que sumados den el target
Ejemplo 1: [-8, 1, 4, 9] Target: 10
Ejemplo 2: [-5, -4, 3, 5, 8] Target: 4
'''
import random
def genera():
  while True:
    #lista con entre 2 y 6 elementos aleatorios que varían entre -10 y +10
    lista = random.sample(range(-10, 11), random.randint(2,6)) 
    lista.sort()                     #ordenamos la lista aunque no es necesario
    #print(lista)
    target=random.randint(2,21)      #target es un número aleatorio entre 2 y 20
    #print('Target:',target)
    if comprueba(lista, target):     #pasamos los dos argumentos a la función comprueba
      print(lista,'Target:',target)  #si comprueba retorna True entonces se imprime la lista y el terget
      break                          #interrumpe el while True ya que en caso contrario sería infinito

def comprueba(lista,target):         #comprueba que en la lista existan dos elementos que sumados de en target
  cumple=0
  for i,v in enumerate(lista):       #i es el index y v es el valor de la lista
    for j,w in enumerate(lista):
      if i!=j and v+w==target:cumple+=1  #compara todas las parejas de elementos de la lista para ver si suman el target
  if cumple==2:        #en toda lista que se imprima la variable cumple es igual a 2. Ejemplo: 2+3=5  3+2=5 
    return True

for n in range(40):                  #generamos 40 listas
  genera()
