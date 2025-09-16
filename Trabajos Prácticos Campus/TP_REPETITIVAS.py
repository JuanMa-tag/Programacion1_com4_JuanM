#TRABAJO PRACTICO DE REPETITIVAS:

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea
for i in range(1,101,1):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
num_digitos=int(input('ingresa un numero para saber sus digitos: '))
cont=0
if num_digitos ==0:
    cont+=1
else:
    while num_digitos > 0:
        num_digitos //= 10
        cont+=1

print(f'Su número contiene {cont} digitos')

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
suma=0
num1=int(input('Ingresa el primer número: '))
num2=int(input('Ingresa el segundo número: '))
for i in range(num1+1,num2):
    suma= suma+i

print(f'La suma de los numeros {num1} y {num2} es {suma}')


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
salir=1
acumulado=0
while salir==1:
    print('INGRESA UN 0 PARA SALIR')
    num=int(input('Ingresa el úmero para sumar: '))
    acumulado= acumulado+ num
    if num ==0:
        salir=0
        print(f'El total acumulado es {acumulado}')


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
termino=0
contador=0

num_aleat=random.randint(0,9)

while termino==0:
    num_usuario=int(input('Ingresa el número: '))
    if num_aleat == num_usuario:
        termino+=1
    contador+=1

print(f'El numero de intentos es: {contador} ')


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
numero_suma=0
numero1=int(input('Ingresa un número: '))
for i in range(0,numero1):
    numero_suma=numero_suma+i

print(numero_suma+numero1)


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos.
par=0
impar=0
negativo=0
positivo=0  

for i in range(0,100):
    numeros=int(input('Ingresa el número: '))
    if numeros % 2 ==0: 
        par+=1
    
    if numeros % 2 !=0: 
        impar+=1
    
    if numeros > 0: 
        positivo+=1  
    
    if numeros < 0: 
        negativo+=1       
   
print(f'Los números pares son: {par}')
print(f'Los números impares son: {impar}')
print(f'Los números positivos son: {positivo}')
print(f'Los números negativos son: {negativo}')


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. 
media=0
suma_media=0
rango=100
for i in range(0,rango):
    num_media=int(input('Ingresa el número: '))
    suma_media= suma_media + num_media
    media=suma_media / rango
print(f'La media de los números es: {media}')


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
invertido = 0

num_invertir = int(input('Ingrese un número que quiera invertir: '))
while num_invertir > 0:
    digito_num = num_invertir % 10         
    invertido = invertido * 10 + digito_num 
    num_invertir = num_invertir // 10            

print(f'El número invertido es: {invertido}')
