lista=['Berlín','París','Roma','Londres']
print([i for i in lista])  #List Comprehension: permiten crear listas de forma concisa
[print(i) for i in lista]  #Haciéndolo iterable
print('~'*20) ########################################
numeros=list(range(10,20))
print(numeros)                  #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print([i for i in numeros if i%2==0])  #Condicional en Lista comprimida
print([i for i in range(100) if i%2==0 if i%5==0])  #Condicional anidado en Lista comprimida
print(["Impar" if i%2==0 else "Par" for i in range(10)]) #Condicional con else