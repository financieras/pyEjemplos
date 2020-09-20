#string.join(iterable)                 devuelve un string
hastacuatro=['1','2','3','4']          #lista
print('-'.join(hastacuatro))           #1-2-3-4
metales=("Plata","Oro","Platino")      #tupla
print(' # '.join(metales))             # Plata # Oro # Platino
cadena='murcielago'                    #string
print(', '.join(cadena))               # m, u, r, c, i, e, l, a, g, o
dic={'Al':13,'Fe':'26','Pb':82}        #diccionario
print(' & '.join(dic))                 # Al & Fe & Pb
#################################
frase="La suerte está echada"
lista=frase.split(); print(lista)      #['La', 'suerte', 'está', 'echada']
cita=' '.join(lista); print(cita)      #La suerte está echada
guiones='H-o-l-a'
lista=guiones.split('-'); print(lista) #['H', 'o', 'l', 'a']
numeros=''.join(lista); print(numeros) #Hola
