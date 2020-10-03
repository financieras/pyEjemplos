#con Programación Orientada a Objetos
class Cliente:
    def __init__(self,dni,nombre,apellido):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido
    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido)
class Empresa:
    def __init__(self,clientes=[]):
        self.clientes=clientes
    def buscar_cliente(self,dni=None):
        for c in self.clientes:
            if c.dni==dni:
                print(c)
                return
        print('Cliente no encontrado')
    def borrar_cliente(self,dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni==dni:
                del(self.clientes[i])
                print(str(c),' --> BORRADO')
                return
        print('Cliente no encontrado')

cliente1=Cliente(nombre='Ana',apellido='Ruiz',dni='1234')
print(cliente1)
cliente2=Cliente('0011','Mario','Diez')
print(cliente2)
empresa_x=Empresa(clientes=[cliente1,cliente2])
print(empresa_x)
print(empresa_x.clientes)
empresa_x.buscar_cliente(dni='0011')
empresa_x.borrar_cliente('0000')
empresa_x.borrar_cliente('0011')
print(empresa_x.clientes)
