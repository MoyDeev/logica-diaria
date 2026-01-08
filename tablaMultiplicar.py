print('ejercicio tabla de multiplicar')
print('----------')
print('Que tabla de multiplicar quieres ver?')

valor = int(input())

for i in range(1,11):
    #5x1 = 5
    mul = valor*i
    print(valor, "x", i, "=", mul)

print("Hasta donde quieres que llege tu multiplicacion?")
valorFinal = int(input())
for i in range(1,valorFinal+1):
    mul2 = valor*i
    print(valor, "x", i, "=", mul2)
