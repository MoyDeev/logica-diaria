print('ingresa la contraseña')

pwd = input()

pwdUser = "niñoBonito"
intentos = 0

while pwd != pwdUser:
    print('vuelva a ingresar su contraseña')
    pwd = input()
    if pwd != pwdUser:
        intentos = intentos+1
        if intentos == 2:
            print('haz sido bloqueado')
            break

if pwd == pwdUser:
    print("Bienvenido")