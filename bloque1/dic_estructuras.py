edades={'Ana':20,'Jose':23,'Luis':28}
for key in edades.keys():
    print(key)
####################################################################
for value in edades.values():
    print(value)
####################################################################
for item in edades.items():
    print(item)
####################################################################
for k,v in edades.items():
    print("{} tiene {} años.".format(k,v))
persona='Jose'
print("{} tiene {} años.".format(persona,edades[persona]))
persona='Alberto'
print("{} tiene {} años.".format(persona,edades.get(persona,None)))