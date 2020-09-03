def sumar(num1,num2): return num1+num2
def restar(num1,num2):return num1-num2
def multiplicar(num1,num2): return num1*num2
def dividir(num1,num2): return num1/num2
while True:
    opcion=input(''' Menú: \n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n0. Finalizar\n''')
    if opcion in ('1','2','3','4'):
        num1=float(input("Introduzca el primer número: "))
        num2=float(input("Introduzca el segundo número: "))
        if opcion=='1': print(num1,'+',num2,'=',sumar(num1,num2))
        elif opcion=='2': print(num1,'-',num2,'=',restar(num1,num2))
        elif opcion=='3': print(num1,'*',num2,'=',multiplicar(num1,num2))
        elif opcion=='4': print(num1,'/',num2,'=',dividir(num1,num2))
    else: print("Programa finalizado"); break
