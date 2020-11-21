# class Arbol():
#     pass
# arbol_navidad=Arbol()
# arbol_navidad.luz = False
# print("¿Tiene luz el arbol de Navidad?",arbol_navidad.luz)
# def encender(a):
#     a.luz=True
#     return
# encender(arbol_navidad)
# print("¿Tiene luz el arbol de Navidad?",arbol_navidad.luz)


class Arbol():
    def __init__(self):
        self.luz=False
    def encender(self):
        self.luz=True

arbol_navidad=Arbol()

print("¿Tiene luz el arbol de Navidad?",arbol_navidad.luz)

arbol_navidad.encender
print("¿Tiene luz el arbol de Navidad?",arbol_navidad.luz)