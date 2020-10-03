#La clase es como un molde para crear objetos
class Galleta:
    pass
galleta1=Galleta()
galleta2=Galleta()
# La creación de un objeto a partir de su clase se llama instanciación
# Por eso los objetos también se llaman instancias de clase
print(type(galleta1))
print(type(()))
print(type({}))
print(type({1,2,3}))
#Atributos (son una especie de variables internas)
#Nos podremos referir a ellos con un puntito y el nombre del atributo
#Si no existe el atributo se creará automaticamente
una_galleta=Galleta()
una_galleta.sabor="Salado"
una_galleta.colo="Marron"
print("El sabor de esta galleta es",una_galleta.sabor)
class Bizcocho:
    chocolate = False
un_bizcocho = Bizcocho()
print("Veamos si este bizcocho tiene chocolate:",un_bizcocho.chocolate)
un_bizcocho.chocolate = True
print("Veamos si el bizcocho tiene ahora chocolate:",un_bizcocho.chocolate)

#Un método es una función interna dentro de una clase
#Este método se comparte por todos los objetos de la misma clase
#El método init es un método especial que se ejecuta al crear un objeto
#El método init permite además enviarle argumentos durante la instanciación
#Los métodos especiales se escriben rodeados de dos barras bajas __init__


class Cookie:
    chocolate = False
    def __init__(self):
        print("Se acaba de crear una cookie.")
        return
c = Cookie()
print(c)