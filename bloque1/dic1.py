#Diccionario: estructura iterable de parejas Clave:Valor, No ordenado. Una lista si es ordenada
mi_diccionario={'uno':'one','dos':'two','tres':'three','cuatro':'four'}
print(mi_diccionario['uno'])         #one
palabra='uno'
print("{} en inglés es {}.".format(palabra,mi_diccionario[palabra]))
dic_num={'uno':1,'dos':2,'tres':3,'cuatro':4}
print("Hay {} tazas de café.".format(dic_num['dos']))
elementos={'Litio':('Li',3),'Sodio':('Na',11),'Potasio':('K',19)}  #nº atómico=nº de protones
print("El número atómico del Litio es",elementos['Litio'][1])
d = {'x':1,'y':2,'z':3}
print(list(d))             #['x', 'y', 'z']
print(d.keys())            #dict_keys(['x', 'y', 'z'])
print(d.values())          #dict_values([1, 2, 3])
print(d.items())           #dict_items([('x', 1), ('y', 2), ('z', 3)])
print(list(d.items()))     #[('x', 1), ('y', 2), ('z', 3)]
print(list(iter(d)))       #['x', 'y', 'z']
