# 1) Dado el diccionario precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#antes
print('Antes')
print(precios_frutas, '\n')

#se agregan mas frutas
precios_frutas ['Naranja']=1200 
precios_frutas ['manzana']=1500
precios_frutas['pera']=2300

#despues
print('Despues')
print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#antes
print('Antes')
print(precios_frutas, '\n')

#se agregan mas frutas
precios_frutas ['Naranja']=1200 
precios_frutas ['Manzana']=1500
precios_frutas['Pera']=2300

#despues
print('Despues')
print(precios_frutas, '\n')

#Se actualizan los precios
precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800
print('Precios actualizados')
print(precios_frutas)


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
precios_frutas={'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
#Se guardan en una lista las frutas sin precios usando la funcion .keys()
lista_de_frutas=precios_frutas.keys()
print(lista_de_frutas)


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
#  Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#  Luego, pedí un nombre y mostrale el número asociado, si existe.



# 5) Solicita al usuario una frase e imprime:
#  Las palabras únicas (usando un set).
#  Un diccionario con la cantidad de veces que aparece cada palabra.

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#  Mostrá los que aprobaron ambos parciales.
#  Mostrá los que aprobaron solo uno de los dos.
#  Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
#  Consultar el stock de un producto ingresado.
#  Agregar unidades al stock si el producto ya existe.
#  Agregar un nuevo producto si no existe.

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
#  Las capitales sean las claves.
#  Los países sean los valores.