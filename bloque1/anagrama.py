def anagrama(cadena1,cadena2):
    cadena1lista=list(cadena1.lower()) #lo pasamos a minúsculas y lo convertimos en una lista de caracteres
    cadena2lista=list(cadena2.lower())
    cadena1lista.sort()                #lo ordenamos
    cadena2lista.sort()
    return cadena1lista==cadena2lista  #comparamos las listas de caracteres ordenadas, si son iguales dará True

palabra1='Roma'
palabra2='amor'
print("¿Son anagrama {} y {}?: ".format(palabra1,palabra2),anagrama(palabra1,palabra2))