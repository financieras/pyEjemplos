def mifuncion(a):
  return len(a)
#Sintaxis: map(función,iterables)
x=map(mifuncion,('Roma','Madrid','Washington'))
print(x)           #es un objeto
print(list(x))     #al convertir el objeto en una lista se hace visible
#################################
def concatena(a,b,c):
  return a+b+c
x = map(concatena,('Estonia','Letonia','Lituania'),('-'*3),('Tallin','Riga','Vilna'))
print(x)           #es un objeto
print(list(x))     #al convertir el objeto en una lista se hace visible
#################################
lista=['abc','xyz']
print(list(map(list,lista)))
#################################