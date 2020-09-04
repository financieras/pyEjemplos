a=1; b=10
while a<=b:
    print(a)
    a=a+1

'''
a=1
while True:             #siempre se cumple
    print(a)            #imprime continuamente valores de a hasta que pulsemos CONTROL+C
    a+=1
'''

a = ['cero', 'uno', 'dos', 'tres']
while a:
    print(a.pop(-1))


lista_vacia=[]
if lista_vacia:
    print("Algo tiene")
else:
    print("La lista no contiene elementos")


a=0
while a>=0:
    a+=1
    print("El valor de a es: ", a)
    if a==10:
        print("El valor de a alcanzó el límite")
        break
    print("Aún no hemos llegado al final")
print("Fin del programa")

print("="*40)

a=0
while a<100:
    print("El valor de a es menor de 100, por ahora: ", a)
    a+=10

print("="*40)

password=""        #inicializamos la variable
while password!="spiderman":
    password=str(input("Introduzca la contraseña: "))
print("Contraseña correcta. Puede acceder.")


while True:
    password=str(input("Introduzca la contraseña: "))
    if password=="Madrid2032": break
print("Contraseña correcta. Puede acceder.")




