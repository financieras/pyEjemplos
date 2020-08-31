lista=['leche','queso','fruta','jamón']
for elemento in lista:
    print(elemento)
print('~'*20) ########################################
for i in range(len(lista)):
    print(i,lista[i])
print('~'*20) ########################################
i=0
while i<len(lista):
    print('Comprar:',lista[i])
    i+=1
print('~'*20) ########################################