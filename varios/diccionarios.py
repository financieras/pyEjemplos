midiccionario={"Francia":"París","Alemania":"Frankfurt","Reino Unido":"Londres","España":"Madrid"}
print(midiccionario)
print(midiccionario["Alemania"])  #consulta del valor que corresponde a una clave
midiccionario["Portugal"]="Lisboa"  #añadimos una nueva clave:valor
print(midiccionario)
midiccionario["Alemania"]="Berlín" #modificamos el valor de una clave
print(midiccionario)
del midiccionario["Reino Unido"]  #elimina un elemento
print(midiccionario)
elemento={"nombre":"oro","numero atómico":92, 235:"radioactivo","metal":True} #varios tipos
print(elemento)
tupla=("Intel","AMD")
procesadores={tupla[0]:"i7",tupla[1]:"Ryzen 7"}
print(procesadores)
print(procesadores["AMD"]==procesadores[tupla[1]])  #da True. podemos preguntar dando una clave o el elemento de la tupla
#veamos un diccionario con otros diccionarios y una lista
informa={"geografia":midiccionario, "quimica":elemento,"primos":[2,3,5,7]}
print(informa)

#veamos el método keys que proporciona las claves de un diccionario
print(midiccionario.keys())
#veamos el método values que proporciona los valores de un diccionario
print(midiccionario.values())
#veamos el método len que proporciona la longitud de un diccionario = nº parejas clave:valor
print(len(midiccionario))  #da 4

