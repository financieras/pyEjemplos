def recorrer1(texto):                    #La función recibe un string
    for caracter in texto:
        print(caracter, end='')
recorrer1("Hello World")
print()
############################################################
def recorrer2(texto):
    for i in range(len(texto)):         #recorremos las posiciones del string hasta su longitud
        print(texto[i], end='')
recorrer2("Hola Mundo")
print()
############################################################
def recorrer3(texto):
    for i in range(len(texto)):
        print(texto[i:i+1], end='')     #slicing. Método de corte
recorrer3("Buenos días")
print()
############################################################
