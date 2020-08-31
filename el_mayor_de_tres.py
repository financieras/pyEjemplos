def comprueba(numeros):
    if numeros[0]==numeros[1]==numeros[2]: return "Los tres son iguales."
    else: return max(numeros)
def recaba_datos():
    global numeros
    numeros=[0]*3     #inicializamos una lista de tres elementos
    for i in range(3):
        numeros[i]=int(input("Diga el número {}: ".format(i+1)))
    return numeros
recaba_datos()
print(comprueba(numeros))