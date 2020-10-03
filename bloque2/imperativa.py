# Programación imperativa, también llamada programación estructurada
clientes=[
    {'Nombre': 'Ana', 'Apellido':'Ruiz', 'dni':'1234'},
    {'Nombre': 'Jose', 'Apellido':'Gil', 'dni':'5678'}
]
print(clientes)
def buscar_cliente(clientes,dni):
    for c in clientes:
        if (dni==c['dni']):
            print('{} {}'.format(c['Nombre'],c['Apellido']))
            return
    print('Cliente no encontrado')
buscar_cliente(clientes,'1234')
buscar_cliente(clientes,'010101')
def borrar_cliente(clientes,dni):
    for i,c in enumerate(clientes):
        if(dni==c['dni']):
            del(clientes[i])
            print(str(c),' --> BORRADO')
            return
    print('Cliente no encontrado')
borrar_cliente(clientes,'0000')
borrar_cliente(clientes,'5678')
print(clientes)
def nuevo_cliente(clientes,su_nombre,su_apellido,su_dni):
    clientes.append(dict(Nombre=su_nombre,Apellido=su_apellido,dni=su_dni))
    return
nuevo_cliente(clientes,'Pedro','Soto','9753')
print(clientes)