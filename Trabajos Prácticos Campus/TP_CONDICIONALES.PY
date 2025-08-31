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
print(' ')

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
edad_ola= int(input('ingrese su edad: '))
if edad_ola <12:
    print('Niño/a')
elif edad_ola >= 12 and edad_ola < 18:
    print('Adolescente')
elif edad_ola >= 18 and edad_ola < 30:
    print('Adulto/a joven')
elif edad_ola >= 30:
    print('Adulto/a')
print(' ')

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"
contraseña= input('ingrese una contraseña entre 8 y 14 caracteres: ')
long_contraseña= len(contraseña)
if long_contraseña >= 8 and long_contraseña<= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')

    

    # 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
frase= input('ingrese un palabra o frase: ')
vocales= ['a','e','i','o','u','A','E','I','O','U']
if frase[-1] in vocales:
    print(frase + '!')
else:
    print(frase)