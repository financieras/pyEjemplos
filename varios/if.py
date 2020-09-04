tarta="no"
print("Os invito a tomar un cafe.")
if tarta=="si":
  print("Y además tenemos tarta.")
print("Vamos a mi casa.")

print("-"*60)

tarta=True
print("Os invito a tomar un cafe.")
if tarta:
  print("Y además tenemos tarta.")
print("Vamos a mi casa.")

print("-"*60)

velocidad=80
legal="si"
if velocidad>120:
  legal="no"
print("El auto circula en autopista a velicidad que",legal,"es legal.")

print("-"*60)

def radar(vel):
  legal="si"
  if vel>120:
    legal="no"
  return legal
print("Se ha detectado que",radar(120),"circula a velocidad legal.") #llamada a la función

print("-"*60)

legal=True
def radar(vel):
  if vel>120:
    legal=False
  return legal

velocidad=130
if radar(velocidad):
  print("Usted circula correctamente")
else:
  print("Atención, ha sobrepasado el límite de velocidad en autopista")


