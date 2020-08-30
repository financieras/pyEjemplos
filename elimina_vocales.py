def procesa(texto):
    vocales=('a','e','i','o','u')
    texto=texto.replace('o','0')
    texto=texto.replace('O','0')
    for vocal in vocales:
        texto=texto.replace(vocal,'')
        texto=texto.replace(vocal.upper(),'')
    return texto
texto="Viajaremos a Oviedo, Alicante o a Bilbao."
print(procesa(texto))

def procesa2(texto):
    texto=texto.replace('a','')
    texto=texto.replace('e','')
    texto=texto.replace('i','')
    texto=texto.replace('o','0')
    texto=texto.replace('u','')
    texto=texto.replace('A','')
    texto=texto.replace('E','')
    texto=texto.replace('I','')
    texto=texto.replace('O','0')
    texto=texto.replace('U','')
    return texto