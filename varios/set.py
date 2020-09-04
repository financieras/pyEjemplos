#un SET es un conjunto no ordenado de elementos
palos = {"oros", "copas", "bastos", "espadas"}
print(palos)
print("copas" in palos)   #True
palos.add("picas")        #para añadir un elemento
print(palos)
palos.update(["corazones","tréboles", "rombos"])  #para añadir varios elementos
print(palos)
print(len(palos))         #longitud del conjunto
palos.remove("picas")     #elimina un elemento, si no existe da error
print(palos)
palos.discard("rombos")   #elimina un elemento, si no existe no da error 
print(palos)
carta=palos.pop()         #elimina un elemento, no se sabe cual y va cambiando
print(palos)
print(carta)              #la variable asignada recoge el elemento eliminado
del(palos)                #elimina el conjunto
#print(palos)             #da error ya que hemos eliminado el conjunto
conjunto1={"oros", "copas", "bastos", "espadas"}
conjunto2={"picas", "corazones","tréboles", "rombos"}
conjunto=conjunto1.union(conjunto2)  #une conjuntos sin repetidos
print(conjunto)
set1={'a','b','c'}
set2=set(('x','y','z'))    #podemos crear un conjunto con set()
set1.update(set2)          #une conjuntos sin repetidos
print(set1)

def muestra(conjunto):                 #La función recibe un conjunto
    for elemento in conjunto:
        print(elemento)
estaciones=set(('primavera','verano','otoño','invierno'))
muestra(estaciones)    

















