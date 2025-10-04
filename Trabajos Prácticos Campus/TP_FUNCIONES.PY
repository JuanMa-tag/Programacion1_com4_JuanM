# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
## def imprimir_hola_mundo():
##     print('hola mundo')
## imprimir_hola_mundo()


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
# Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
# # def saludar_usuario(nombre):
# #     print(f'¡hola {nombre} que tal!!')
# # nombre_usuario=input('ingresa tu nombre: ')
# # saludar_usuario(nombre_usuario)


# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}')

nombreUsuario =input('Ingresa tu nombre: ')
apellido_usuario=input('Ingresa tu apellido: ')
edad_usuario= int(input('Ingrese su edad: '))
residencia_usuario=input('Ingrese su lugsr de residencia: ')
informacion_personal(nombreUsuario, apellido_usuario, edad_usuario, residencia_usuario)
















