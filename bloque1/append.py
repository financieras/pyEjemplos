oferta = ['espagueti', 'pollo', 'tarta', 'agua', 'cerveza']
print(oferta.index('tarta'))           #2
oferta.append('café')    #['espagueti', 'pollo', 'tarta', 'agua', 'cerveza', 'café']
print(oferta)
oferta.remove('agua')    #['espagueti', 'pollo', 'tarta', 'cerveza', 'café']
print(oferta)
oferta.pop()             #['espagueti', 'pollo', 'tarta', 'cerveza']
print(oferta)
oferta.insert(2,'fruta') #['espagueti', 'pollo', 'fruta', 'tarta', 'cerveza']
print(oferta)
oferta.insert(0,'pan')   #['pan', 'espagueti', 'pollo', 'fruta', 'tarta', 'cerveza']
print(oferta)
oferta.sort()
print(oferta)            #['cerveza', 'espagueti', 'fruta', 'pan', 'pollo', 'tarta']
######################################
#import random
from random import randrange,sample
un_aleatorio=randrange(-20,50)
print(un_aleatorio)
lista_aleatoria1=[]
for i in range(5):
    lista_aleatoria1.append(randrange(-20,50))
print(lista_aleatoria1)
lista_aleatoria2=[]
lista_aleatoria2=sample(range(-20,50),5)
print(lista_aleatoria2)
lista_aleatoria=lista_aleatoria1+lista_aleatoria2
lista_aleatoria.sort()
print(lista_aleatoria)