cadena='Lo importante es no dejar de hacerse preguntas'
frase=cadena.split()
print(frase)
#crear un diccionario con la longitud de cada palabra
dic={palabra:len(palabra) for palabra in frase}
print(dic)
#crear un diccionario con la letra inicial de cada palabra
inicial={palabra:palabra[0].upper() for palabra in frase}
print(inicial)
#elevar al cuadrado los números impares entre 5 y 12 incluidos ambos
print({n:pow(n,2) for n in range(12) if n>=5 if n%2==1})