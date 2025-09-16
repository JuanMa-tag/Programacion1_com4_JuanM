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

