def recorrer(texto):                       #La función recibe un string
    for caracter in texto:
        print(caracter, end='')
recorrer("Hola Mundo")
############################################################
def recorrer2(texto):                       #La función recibe un string
    for i in range(len(texto)):
        print(texto[i], end='')
recorrer2("Hola Mundo")
############################################################
