def par_impar(numero):
    if numero%2==0:
        resultado='par'
    else:
        resultado='impar'
    print("El número {} es {}.".format(numero,resultado))
par_impar(21)
#########################################################
def reverso(cadena):
    return cadena[::-1]
texto=input("Introduce un texto para invertir: ")
print('El reverso es: ',reverso(texto))
########################################################
def area_tri(base,altura):
    return base*altura/2
print("El área de un triángulo de base {} y altura {} es {}.".format(10,4,area_tri(10,4)))
