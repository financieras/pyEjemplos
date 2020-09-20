historia = {
  "Apolo": 11,
  "astronauta": "Neil Armstrong",
  "año": 1969
}
print(historia)                   # {'Apolo': 11, 'astronauta': 'Neil Armstrong', 'año': 1969}
historia["Apolo"]='XI'            # Cambiamos el valor de la clave Apolo
print(historia)                   # {'Apolo': 'XI', 'astronauta': 'Neil Armstrong', 'año': 1969}
print("año" in historia)          # True
print(len(historia))
historia["módulo"]="Eagle"
print(historia)  # {'Apolo': 'XI', 'astronauta': 'Neil Armstrong', 'año': 1969, 'módulo': 'Eagle'}
historia.pop("astronauta")
print(historia)                   # {'Apolo': 'XI', 'año': 1969, 'módulo': 'Eagle'}
ficcion = historia.copy()
ficcion["año"]=2022
print("historia es = ", historia) # historia es =  {'Apolo': 'XI', 'año': 1969, 'módulo': 'Eagle'}
print("ficcion es  = ", ficcion)  # ficcion es  =  {'Apolo': 'XI', 'año': 2022, 'módulo': 'Eagle'}
del ficcion["Apolo"]
print(ficcion)                   # {'año': 2022, 'módulo': 'Eagle'}
ficcion.clear()
print(ficcion)                   # {}
del ficcion                      # del también borra el diccionario entero
#print(ficcion)                  # esta línea provocaría un error
print("_"*40)
#Otra forma de construir un diccionario, con el constructor dict()
pantalla = dict(marca="LG", resolución="4K", pulgadas=32)
print(pantalla)

# Diccionarios anidados
amigos = {
  "colega1" : {
    "nombre" : "Pedro",
    "año" : 2001
  },
  "colega2" : {
    "nombre" : "Silvia",
    "año" : 2004
  },
  "colega3" : {
    "nombre" : "Isa",
    "año" : 2003
  }
}
print(amigos) #{'colega1': {'nombre': 'Pedro', 'año': 2001}, 'colega2': {'nombre': 'Silvia', 'año': 2004}, 'colega3': {'nombre': 'Isa', 'año': 2003}}

#Podemos crear varios diccionarios y otro que los contenga
Intel={"gama":"i3","precio":120}
AMD={"gama":"Ryzen3","precio":90}
micros={"marca1":Intel,"marca2":AMD}
print(micros)
print(micros.keys())