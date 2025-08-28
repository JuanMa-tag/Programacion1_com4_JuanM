#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad_usuario= int(input('ingrese su edad: '))
if edad_usuario > 18:
    print('Es mayor de edad')
print(' ')

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# # mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# # mensaje “Desaprobado”.
nota = float(input('ingrese su nota: '))
if nota>= 6:
    print('Aprobado')
else:
    print('Desaprobado')
print(' ')
 
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par".
numero= int(input('ingrese un número par: '))
if numero % 2 == 0:
    print('Ha ingresado un número par')
else:
    print('Por favor, ingrese un número par')