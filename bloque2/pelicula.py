class Pelicula:
    # Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado una pelicula',self.titulo)
    
    # Destructor de clase
    def __del__(self):
        print('Se ha borrado la película',self.titulo)

    # Redifinimos el método string
    def __str__(self):
        return '{} lanzada en {} con una duración de {} minutos'.format(self.titulo,self.lanzamiento,self.duracion)

    # Redefinir el método Length
    def __len__(self):
        return self.duracion

#Los métodos especiales no se aplican poniendo puntito sino pasándoles parámetros

p = Pelicula("El Padrino",175,1972)
#del(p)
print(p)
str(p)
print('La duración de la película es de {} minutos.'.format(len(p)))
