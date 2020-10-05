#La encapsulación impide el acceso externo a atributos y métodos
class Ejemplo:
    #los atributos privados comienzan con __
    __atributoprivado = "Soy un atributo inalcanzable desde fuera"
    
    #los métodos privados comienzan con __
    def __metodoprivado(self):
        print("Soy un metodo inalcanzable desde fuera")

e = Ejemplo()
#e.__atributoprivado  #da error
#e.__metodoprivado()  #da error
#Los atributos y métodos no se pueden usar desde fuera (dan error)
#pero si se pueden usar desde dentro

