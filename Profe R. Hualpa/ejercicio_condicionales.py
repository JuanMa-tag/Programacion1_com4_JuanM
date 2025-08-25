#Ejercicio 6: Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. 
 #Dicha calificación se compone de los siguientes porcentajes:
 #55% del promedio de sus tres calificaciones parciales.
 #30% de la calificación del examen final.
 #15% de la calificación de un trabajo final.

#Calificaciones de los parciales
parcial1 = float(input("Ingrese la calificación del primer parcial: "))
parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
#Calificaciones del examen final y trabajo final
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))
#Calcular el promedio de los parciales
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
#Calcular la calificación final
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print(f"La calificación final es: {calificacion_final}")
print( )
#Ejercicio 7: Conversión de divisas
 #Un programa que lea un monto en dólares y lo convierta a pesos colombianos, 
 #argentinos y euros usando tasas de cambio fijas definidas en el código.

tasa_cop= 4000
tasa_ars= 1360
tasa_eur= 0.86

monto_dolares= float(input('Ingresa el monto en dolares: '))
pesos_colombianos= monto_dolares* tasa_cop
pesos_argentinos= monto_dolares* tasa_ars
euros= monto_dolares* tasa_eur

print(f"Pesos colombianos: {pesos_colombianos: .2f}")
print(f"Pesos argentinos: {pesos_argentinos: .2f}")
print(f"Euros: {euros: .2f}")
print( )

#Ejercicio 8: Viaje en auto
 #Un auto consume 8 litros cada 100 km. El usuario ingresa la distancia en km 
 #y el precio de la gasolina por litro.
 #El programa debe calcular:
 #cuántos litros se necesitan, cuánto costará el viaje,
 #cuántas horas tardará si la velocidad promedio es de 90 km/h.

distancia = float(input("Ingrese la distancia en km: "))
precio_gasolina = float(input("Ingrese el precio de la gasolina por litro: "))

litros_necesarios= (distancia/100)*8
costo_viaje= litros_necesarios* precio_gasolina
tiempo_horas= distancia/90

print(f'litros necesarios: {litros_necesarios: .2f} litros')
print(f'costo del viaje: {costo_viaje: .2f} pesos')
print(f'tiempo del viaje: {tiempo_horas: .2f} horas')
print( )


#Ejercicio 9: Préstamo bancario
#Un cliente solicita un préstamo que deberá pagar en 12 meses con interés fijo mensual del 2%.
#El usuario ingresa el monto solicitado, y el programa debe calcular:
#el monto total a devolver,
#el valor de cada cuota mensual.

prestamo = float(input("Ingrese el monto del préstamo: "))
interes_mensual = 0.02
meses = 12

monto_total = prestamo * (1 + interes_mensual) ** meses
cuota_mensual = monto_total / meses

print(f'Monto total a devolver: {monto_total: .2f} pesos')
print(f'Valor de cada cuota mensual: {cuota_mensual: .2f} pesos')
