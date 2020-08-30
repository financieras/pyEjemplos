import math 
def area_circulo(radio):
    radio=float(radio)
    return math.pi*radio**2
while True:
    r=input("Indique el radio del círculo o pulsa Enter: ")
    if r=="":
        break
    print("El área de un círculo de radio {} es {}.".format(r,round(area_circulo(r),1)))