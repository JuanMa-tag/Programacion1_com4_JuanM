# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.
lista_multiplo= list(range(0,101,4))
print(lista_multiplo)


# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. 
penultimo_elemento=['hola', 'UTN', 0.5, 4, False ]
print(penultimo_elemento[-2])


# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla.
lista_vacia=[]
for i in range(3):
    palabras=input(f'Ingresa la palabra Nro {i+1}: ')
    lista_vacia.append(palabras)

print(lista_vacia)


# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. 
animales = ["perro", "gato", "conejo", "pez"]

animales[1]='loro'
animales[-1]='oso'
print(animales)


# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7] #Acá se crea la lista y se le agregan elementos.
numeros.remove(max(numeros))# Acá con la funcion max se busca el numero mayor y con remove se elimina el numero buscado.
print(numeros)# Se imprime la lista sin el elemento que se eliminó.


# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.
numeros = list(range(10, 31, 5))
print(numeros[0], numeros[1])


# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
print('Antes')
autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1]='99'
autos[2]=True
print('Despues')
print(autos)


# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente.
dobles=[]
dobles.append(10)
dobles.append(20)
dobles.append(30)
print(dobles)


# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append('jugo')
compras[1][1]='tallarines'
compras[0].remove('pan')
print(compras)


# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.
lista_anidada=[15, True,[25.5, 57.9, 30.6], False]
print(lista_anidada)
