edad=5
#print('Solo tiene '+edad+' años')         #TypeError
print('Solo tiene '+str(edad)+' años')    #Solo tiene 5 años
print('Solo tiene {} años'.format(edad))  #Solo tiene 5 años
p=a=s=2
print(p,a,s)
x=2
y=3
print(16 - 2 * 5 // 3 + 1)
a, b, c = 21, 10, 0

print("Valor de variable 'a':", a)
print("Valor de variable 'b':", b)

c = a + b
print("Operador = | El valor de variable 'c' es ", c)

c += a
print("Operador += | El valor de variable 'c' es ", c)

c *= a
print("Operador *= | El valor de variable 'c' es ", c)

c /= a 
print("Operador /= | El valor de variable 'c' es ", c)

c = 2
c %= a
print("Operador %= | El valor de variable 'c' es ", c)

c **= a
print("Operador **= | El valor de variable 'c' es ", c)

c //= a
print("Operador //= | El valor de variable 'c' es ", c)