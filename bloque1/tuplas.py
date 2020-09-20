estaciones=('Primavera','Verano','Otoño','Invierno')
type(estaciones)
#Los elementos de una lista son mutables, los elementos de una tupla son inmutables.
#La iteración sobre los elementos de una tupla es más rápida que la iteración sobre una lista.
mi_tupla=(15,'clientes',True,[5,7,9],('a','b','c'),12.35)
tupla_uno=(14,)        #Tupla con un único elemento
a=[3,5,7,9]            #una lista
b=tuple(a)             #se convierte en tupla
print(b)               #(3, 5, 7, 9)
print(estaciones[0])   #'Primavera'
print(mi_tupla[-1])    #12.35
print(mi_tupla[1][0])  #c
print(mi_tupla[3][1])  #7
mi_tupla[3][1]=8       #Podemos cambiar los elementos de una lista dentro de una tupla
print(mi_tupla[3])     #[5, 8, 9]   la lista si es mutable aunque esté dentro de una tupla
del(estaciones)        #podemos borrar una tupla pero no sus elementos
decadas=(10,20,30,40,50,60)
print(decadas[2:5])      #(30, 40, 50)  Operación de corte en tuplas (Slicing)
print(decadas[:3])       #(10, 20, 30)
print(decadas[:])        #(10, 20, 30, 40, 50, 60)   La tupla completa
print(20 in decadas)     #True
print(21 not in decadas) #True
#Las Tuplas son inmutables pero se pueden convertir en listas y viceversa
d=list(decadas)
d.append(75)
d[-1]=70
decadas=tuple(d)
print(decadas)
estaciones=('Primavera','Verano','Otoño','Invierno')
for i in estaciones:
    print(i)
for estacion in estaciones:
    print(estacion,end=', ')  #queda la última coma
print()
texto=''
for estacion in estaciones:
    texto+=estacion+','
print(texto[:-1])             #así no se muestra la última coma
print('~'*40)
print(*estaciones,sep=', ')
print(*(i for i in estaciones if len(i)<7),sep=', ')        #Verano, Otoño