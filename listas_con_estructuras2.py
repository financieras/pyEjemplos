lista=['Berlín','París','Roma','Londres']
print(enumerate(lista))
print('~'*20) ########################################
for contador,elemento in enumerate(lista):
    print(contador,": ",elemento)
print('~'*20) ########################################
for i,j in enumerate(lista,1):      #poniendo el 1 el contador comienza en 1
    print(i,": ",j)
print('~'*20) ########################################
print(list(enumerate(lista,1)))     #[(1, 'Berlín'), (2, 'París'), (3, 'Roma'), (4, 'Londres')]
print(type(list(enumerate(lista,1))[0]))     #<class 'tuple'>
