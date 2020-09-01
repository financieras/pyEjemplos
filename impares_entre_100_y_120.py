#Generar números impares entre 100 y 120
lista=[]
for i in range(101,120):
    lista.append(i)
    i=i+2
print(lista)
#########################################
lista=[]
for i in range(101,120,2):
    lista.append(i)
print(lista)
#########################################
lista=[]
i=101
while i<120:
    lista.append(i)
    i=i+2
print(lista)
#########################################
lista=[]
for i in range(100,120):
    if i%2!=0:
        lista.append(i)
print(lista)
#########################################