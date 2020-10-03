class Galleta():
    pass

#Atributos: variables internas de las clases
#Podemos referirnos a esas variables mediante un puntito y el nombre del atributo
#

una_galleta = Galleta()
otra_galleta = Galleta()
una_galleta.sabor="Salado"
otra_galleta.color="Marrón"
print("El sabor de una_galleta es:",una_galleta.sabor)
print("El color de otra_galleta es:",otra_galleta.color)

#Podemos crear atributos en la clase compartidos por todas las instancias
class Galleta():
    chocolate = False

g=Galleta()
print('¿La galleta tiene chocolate?',g.chocolate)
g.chocolate=True
print('Y ahora ¿tiene chocolate?',g.chocolate)
#Método especial __init__
#Palabra reservada self
class Galleta():
    chocolate = False
    def __init__(self):
        print('Se acaba de crear una galleta.')
g=Galleta()
#Un método es una función interna de la clase
#El método init es un método especial que se ejecuta siempre que se instancia un objeto
class Galleta():
    chocolate = False
    def __init__(self):
        print('Se acaba de crear una galleta.')
    def chocolatear(self):
        self.chocolate = True #imprescindible poner self. ya que en caso contrario chocolate sería una variable interna de la función y no trabajaría sobre el atributo interno de clase (chocolate) definido arriba
g=Galleta()
g.chocolatear()
print("¿Tiene chocolate la galleta creada?",g.chocolate)
#crearemos un nuevo método
class Galleta():
    chocolate = False
    def __init__(self):
        print('Se acaba de crear una galleta.')
    def chocolatear(self):
        self.chocolate = True #imprescindible poner self. ya que en caso contrario chocolate sería una variable interna de la función y no trabajaría sobre el atributo interno de clase (chocolate) definido arriba
    def tiene_chocolate(self):
        if self.chocolate:
            print('Soy una galleta chocolateada')
        else:
            print('Soy una galleta sin chocolate.')
g=Galleta()
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()
#Ahora vamos a añadir más argumentos en la creación del objeto
class Galleta():
    chocolate = False
    def __init__(self,sabor,forma):
        self.sabor=sabor
        self.forma=forma
        print('Se acaba de crear una galleta {} y {}.'.format(sabor,forma))
    def chocolatear(self):
        self.chocolate = True #imprescindible poner self. ya que en caso contrario chocolate sería una variable interna de la función y no trabajaría sobre el atributo interno de clase (chocolate) definido arriba
    def tiene_chocolate(self):
        if self.chocolate:
            print('Soy una galleta chocolateada')
        else:
            print('Soy una galleta sin chocolate.')
g=Galleta('vainillada','redonda')
print(g)
#galletita=Galleta() #esto da error pq no se han pasado los argumentos requeridos sabor y forma
class Galleta():
    chocolate = False
    def __init__(self,sabor=None,forma=None):
        self.sabor=sabor
        self.forma=forma
        if sabor is not None and forma is not None:
            print('Se acaba de crear una galleta {} y {}.'.format(sabor,forma))
    def chocolatear(self):
        self.chocolate = True #imprescindible poner self. ya que en caso contrario chocolate sería una variable interna de la función y no trabajaría sobre el atributo interno de clase (chocolate) definido arriba
    def tiene_chocolate(self):
        if self.chocolate:
            print('Soy una galleta chocolateada')
        else:
            print('Soy una galleta sin chocolate.')
g=Galleta()
print("La galleta sin argumentos se ha creado",g)


