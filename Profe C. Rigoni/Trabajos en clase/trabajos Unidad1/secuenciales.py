#Calculadora de propinas en un restaurante
#Pedir al usuario el monto total de la cuenta.  3500
monto_total =float(input('ingresa el monto tota de la cuenta'))
#Calcular la propina sugerida al 10%.  350.0
propina10= monto_total*0.10
print('La propina de 10% es: ', propina10)
#Calcular la propina sugerida al 15%.  525.0
propina15= monto_total*0.15
print('la propina del 15% es: ', propina15)
#Calcular el total a pagar en ambos casos (cuenta + propina). 3850.0 - 4025.0
print('Total si aplico el 10%: ', monto_total+propina10)
print('Total si aplico el 15%: ', monto_total+propina15)
#Mostrar todos los resultados en pantalla.