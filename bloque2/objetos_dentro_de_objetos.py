class Pelicula:
    # Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado una pelicula',self.titulo)
    def __str__(self):
        return '{} ({})'.format(self.titulo,self.lanzamiento)
class Catalogo:
    peliculas=[]
    def __init__(self,peliculas=[]):
        self.peliculas=peliculas
    def agregar(self,p):
        self.peliculas.append(p)
    def mostrar(self):
        for p in self.peliculas:
            print(p)

p1=Pelicula("El Padrino 1",175,1972)
p2=Pelicula("El Padrino 2",202,1974)
#3=Pelicula("El Padrino 3",163,1990)
c=Catalogo([p1])
c.mostrar()
print('~'*20)
c.agregar(p2)
c.mostrar()
print('~'*20)
#Podemos agregar una película al catálogo sin definirla previamente
c.agregar(Pelicula("El Padrino 3",163,1990))
c.mostrar()