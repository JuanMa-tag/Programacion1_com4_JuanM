#TRABAJO PRACTICO DE REPETITIVAS:

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea
for i in range(1,101,1):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num_digitos=int(input('ingresa un numero para saber sus digitos: '))

digitos= len(str(num_digitos))

print(f'Su número contiene {digitos} digitos')

