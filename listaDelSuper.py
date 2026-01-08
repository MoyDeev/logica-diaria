#listas
listaCompras = []

while True:
    print("Ingrese un producto")
    producto = input()
    listaCompras.append(producto)
    print("quieres agregar otro producto?: S=Si, N=No")
    valor = input()
    if valor.lower() == 'n':
        break
        
print(listaCompras)

