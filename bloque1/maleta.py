maxpeso=5000
obj=[2500,1500,3512,412,1345,120]
pesototal=0
for i in range(6):
    pesototal += obj[i]                #añadimos todos los objetos 
    if (pesototal>maxpeso):            #pero si el último objeto añadido hace que se super el peso máximo
        pesototal= pesototal-obj[i]    #en ese caso lo eliminamos (lo restamos)
print (pesototal)
########### Otra versión #################
pesomax=5000
elementos=[2500,1500,3512,412,1345,120]
peso=0
for elemento in elementos:             #recorremos todos los elementos
    if (elemento<=pesomax-peso):       #si el peso del elemento es menor o igula a la capacidad que aun queda en la maleta
        peso+=elemento                 #en ese caso si añadimos el elemento a la maleta
print (peso)
############ Ahora usando random #########
from random import randint             #no importamos la libreria random entera solo importamos randint
pesoMax=5000
total=0
objetos=[]
while total<5*pesoMax:                 #creamos una lista larga de objetos que tienen un peso total de 5 veces el máximo permitido
    objetos.append(randint(1,2000))    #la lista objetos tendrá elementos entre 1 y 2000 gramos
    total=sum(objetos)                 #calculamos total que es el peso total de la lista, se calcula en cada iteración
objetos.sort(reverse=True)             #ordenamos la lista de objetos de mayor a menor
print(objetos)                         #imprimimos la lista larga
print(total)                           #imprimimos el peso total de la lista larga
peso=0                                 #inicializamos la variable peso a cero, será el peso de los objetos que quepan en la maleta
for objeto in objetos:                 #recorremos todos los elementos de la lista larga
    peso+=objeto                       #de momento añadimos el peso de todo elemento de la lista larga
    if peso>pesoMax:                   #si el peso acumulado hasta el momento ya supera el pesoMax entonces hacemso dos cosas:
        peso-=objeto                   #quitamos el peso del último elemento añadido
        objetos.remove(objeto)         #quitamos el último elemento añadido de la lista. Así la lista se ira quedando solo con los elementos que caben
print(objetos)                         #imprimimos la lista corta que contiene solo los elementos que caben en la maleta, los otros se han ido quitando
print(peso)                            #imprimimos el peso de los objetos que caben en la maleta. Este será el peso total de la maleta que no excede el pesoMax
print("falta para llenar la maleta {} gramos.".format(pesoMax-peso))