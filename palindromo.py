print('ejercicio palindromo')
print('----------')
print('Ingrese una palabra')

palabra = input()
palabraInvertida = ""

es_Palindromo = False

for letra in palabra: 
    palabraInvertida = letra+palabraInvertida

if palabra == palabraInvertida:
    es_Palindromo=True
    print("La palabra: ", palabra, "es palindromo")