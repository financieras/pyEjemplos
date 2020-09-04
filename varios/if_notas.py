nota=float(input("Introduzca la nota: "))                                   #calificación de un examen
if nota<5:
    print("calificación: Suspenso")
elif nota<7:
    print("calificación: Aprobado")
elif nota<9:
    print("calificación: Notable")
else:
    print("calificación: Sobresaliente")
