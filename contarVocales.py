print('Ejercicio contar vocales')
print('-------------------------')
print('Ingresa una palabra')

palabra = ""

palabra = input()
vocales = "aeiouAEIOU"
contador=0

for letra in palabra.lower():
    if letra in vocales:
       contador = contador + 1
       
print('La palabra: ', palabra, 'tiene', contador, 'vocales')