#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print('Hola Mundo!')
print(' ')

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
 #el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
 #por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
 #realizar la impresión por pantalla.
nombre = input('Ingresa tu nombre')
print(f'Hola {nombre}!')

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
 #imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
 #“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
 #años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
 #la impresión por pantalla.
nombre_apellido= input('Inngrese su nombre y apellido')
edad= int(input('Ingrese su edad'))
residencia= input('Ingrese su lugar de residencia (pais o ciudad)')
print(f'Soy {nombre_apellido}, tengo {edad} años y vivo en {residencia}.')
print(' ')

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
 #su perímetro.
radio= float(input('Ingrsa el radio del circulo'))
num_pi=3.1416
perimetro= 2*num_pi * radio
area= num_pi*radio**2
print(f'El perimetro es {perimetro} y el area es {area}')
print(' ')

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
 #cuántas horas equivale.
segundos= int(input('Ingresa la cantidad de segundos'))
horas= segundos/3600
print(f' {segundos} segundos son {horas} horas')
print(' ')

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
 #multiplicar de dicho número.
numero=int(input('Ingresa un número para ver su tabla de multiplicar'))
print(numero,'x 1=', numero*1)
print(numero,'x 2=', numero*2)
print(numero,'x 3=', numero*3)
print(numero,'x 4=', numero*4)
print(numero,'x 5=', numero*5)
print(numero,'x 6=', numero*6)
print(numero,'x 7=', numero*7)
print(numero,'x 8=', numero*8)
print(numero,'x 9=', numero*9)
print(numero,'x 10=', numero*10)
print(' ')

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
 #pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print('Ingresa dos números enteros distintos del 0')
numero1= int(input())
numero2= int(input())
suma= numero1+numero2
resta= numero1-numero2
multiplicacion= numero1*numero2
division= numero1/numero2
print(f'El resultado de sumarlos es: {suma}')
print(f'El resultado de restarlos es: {resta}')
print(f'El resultado de multiplicarlos es: {multiplicacion}')
print(f'El resultado de dividirlos es: {division}')
print(' ')

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
 #de masa corporal. 
altura= float(input('ingresa tu altura en metros'))
peso= float(input('ingresa tu peso en kilogramos'))
indice_de_masa= peso/altura**2
print(f'Su índice de masa corporal es: {indice_de_masa}')
print(' ')

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
 #pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
grados_celsius = float(input('Ingresa la temperatura en grados Celsius: '))
grados_fahrenheit = (grados_celsius * 9/5) + 32
print(f'La temperatura en grados Fahrenheit es: {grados_fahrenheit}')
print(' ')

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
 #dichos números.
num_promedio1 = float(input('Ingresa el primer número: '))
num_promedio2 = float(input('Ingresa el segundo número: '))
num_promedio3 = float(input('Ingresa el tercer número: '))
promedio = (num_promedio1 + num_promedio2 + num_promedio3) / 3
print(f'El promedio de los tres números es: {promedio}')