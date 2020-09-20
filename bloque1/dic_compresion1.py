dic={1:1,2:2,3:3,4:4}
doble={str(k):2*v for k,v in dic.items()}
print(doble)            # {'1': 2, '2': 4, '3': 6, '4': 8}
##########################
cuadrado_impares={}
for i in range(10):
    if i%2!=0:
        cuadrado_impares[i]=i**2
print(cuadrado_impares) # {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
##########################
cuadrado_pares={i:i**2 for i in range(10) if i%2==0}
print(cuadrado_pares)   # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}