print('ingresa la contraseña')

pwd = input()

pwdUser = "niñoBonito"

while pwd != pwdUser:
    print('vuelva a ingresar su contraseña')
    pwd = input()
    if pwd == pwdUser:
        print('Bienvenido')
