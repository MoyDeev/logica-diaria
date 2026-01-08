#agenda telefonica
print("guarda tus contactos")

contactos = {}

for i in range(0,3):
    print("Ingresa el nombre:")
    nombre = input()
    print("ingresa el telefono:")
    telefono=input()
    contactos[nombre] = telefono

print("-----busqueda------")
print("¿A quien quieres llamar?")
nombreLlamada = input()

if nombreLlamada in contactos:
    numero = contactos[nombreLlamada]
    print("llamando a: ", nombreLlamada, "al numero: ", numero)    
else:
    print("contacto no encontrado")