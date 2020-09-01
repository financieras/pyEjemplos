lista=[] #Generar números impares entre 100 y 120   #Método 1
for i in range(101,120,2):
    lista.append(i)
print(lista)
lista=[]
i=101                                               #Método 2
while i<120:
    lista.append(i)
    i=i+2
print(lista)
lista=[]                                            #Método 3
for i in range(100,120):
    if i%2!=0:
        lista.append(i)
print(lista)
print([i for i in range(101,120,2)])                #Método 4
[print(i) for i in range(101,120) if i%2==0]        #Método 5