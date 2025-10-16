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
def nombres_claves(clave, valor, registro_numeros): #Funcion para registrar los numeros (keys) y los numeros (values)
    registro_numeros[clave]= valor
    return registro_numeros

registro={}
for i in range(2):
    nombre=input(f'Ingresa el nombre de la persona Nro {i+1}: ')
    numero=int(input('Ahora ingresa su número: '))
    nombres_claves(nombre,numero,registro)
print(registro, '\n') #Se imprimen los numeros registrados

buscar_valor=input('Ingrese el nombre para ver el numero asociado: ')
if buscar_valor in registro:
        print(f'El nombre a sido encontrado, el numero es: {registro[buscar_valor]}')
else:
    print('El nombre no esta registrado')


# 5) Solicita al usuario una frase e imprime:
#  Las palabras únicas (usando un set).
#  Un diccionario con la cantidad de veces que aparece cada palabra.
frase=input('ingrese una frase: ')
palabras = frase.lower().split()
palabras_unicas = set(palabras)
print("\n Palabras Únicas")
print(palabras_unicas)

print("--------------------------")
frecuencia = {}
for palabra in palabras:
  if palabra in frecuencia:
    frecuencia[palabra] += 1
  else:
    frecuencia[palabra] = 1
print(frecuencia)


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
alumnos = {}
print("--- Ingreso de Alumnos y Notas ---")

for i in range(3):
    print('\n------------------------------------------------ ')
    alumno=input(f'ingresa el nombre el alumno Nro {i+1}: ')
    notas_list=[]
    for j in range(3):
        notas=float(input(f'ingresa la nota Nro {j+1}: '))
        notas_list.append(notas)
    alumnos[alumno] = tuple(notas_list)

print('-----Promedios-----')    
for alumno, notas in alumnos.items():
    promedio = sum(notas) /3
    print(f"\nEl promedio de {alumno} es: {promedio:.2f}")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#  Mostrá los que aprobaron ambos parciales.
#  Mostrá los que aprobaron solo uno de los dos.
#  Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
def Los_dos_parciales(primer,segundo):
   #Alumnos que aprobaron AMBOS parciales
    ambos_parciales = primer & segundo
    return print(ambos_parciales)

def Un_solo_parcial(primer,segundo):
    # Alumnos que aprobaron SOLO UNO de los dos parciales
    solo_un_parcial = primer ^ segundo
    return print(solo_un_parcial)

def Todos_los_aprobados(primer,segundo):
    # Lista total de alumnos que aprobaron AL MENOS UN parcial (Unión)
    aprobados = primer| segundo
    return print(aprobados)

parcial_1 = {'Ana', 'Luis', 'Maria', 'Juan', 'Pedro', 'Sofia'}
parcial_2 = {'Carlos', 'Maria', 'Juan', 'Laura', 'Pedro', 'Diego'}
print(f'Alumnos que aprobaron Parcial 1: {parcial_1}')
print(f'Alumnos que aprobaron Parcial 2: {parcial_2}')

#Interseccion
print(f'\nAlumnos que aprobaron ambos parciales:')
Los_dos_parciales(parcial_1,parcial_2)
#Diferencia simétrica
print(f'\nAlumnos que aprobaron solo uno de los dos parciales:')
Un_solo_parcial(parcial_1,parcial_2)
#Unión
print(f'\nLista total de alumnos que aprobaron al menos un parcial:')
Todos_los_aprobados(parcial_1, parcial_2)


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
#  Consultar el stock de un producto ingresado.
#  Agregar unidades al stock si el producto ya existe.
#  Agregar un nuevo producto si no existe.
productos_y_stocks={}
while True:
    print("""Ingrese la opcion que desee
        1. Consultar el stock de un producto ingresado.
        2. Agregar unidades al stock si el producto ya existe.
        3. Agregar un nuevo producto si no existe.""")
    opcion=input()
    if opcion=='1':  #Consultar el stock de un producto ingresado.
        consultar_producto=input('¿Cuál es el producto que desea consultar? ')
        if consultar_producto in productos_y_stocks:
            print(f'El stock del producto "{consultar_producto}" es: {productos_y_stocks[consultar_producto]}')
        else:
            print('El producto no fue agregado')
    elif opcion=='2':  #Agregar unidades al stock si el producto ya existe.
        producto_existente=input('Indique el producto a actualizar: ')
        agregar_stocks=int(input('Ingresa la cantidad de stocks que desea agregar: '))
        productos_y_stocks[producto_existente]+= agregar_stocks
    elif opcion=='3':  #Agregar un nuevo producto si no existe.
        producto_agregar=input('Ingresa el producto que desea agregar: ')
        stock_del_producto=int(input('Ahora ingrese el stock del producto agregado: '))
        productos_y_stocks[producto_agregar]= stock_del_producto
    else:
        break


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.
agenda = {
    ('lunes', '10:00'): 'Reunión de equipo',
    ('martes', '09:00'): 'Cita con el dentista',
    ('miércoles', '15:30'): 'Entregar reporte',
    ('viernes', '20:00'): 'Cena con amigos',
    ('sábado', '11:00'): 'Partido de fútbol'
}

print('--- Agenda de Eventos ---')
while True:
    dia = input('\nIngrese el día que desea consultar (o \'salir\' para terminar): ').lower()
    if dia == 'salir':
        print('¡Hasta luego!')
        break
        
    hora = input(f'Ingrese la hora para el día {dia} (formato HH:MM): ')
    consulta = (dia, hora)
    evento = agenda.get(consulta, 'No hay ninguna actividad programada en esa fecha y hora.')
    print(evento)


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
#  Las capitales sean las claves.
#  Los países sean los valores.
paises_a_capitales = {
    'Argentina': 'Buenos Aires',
    'España': 'Madrid',
    'Francia': 'París',
    'Italia': 'Roma',
    'Japón': 'Tokio'
}

print('--- Diccionario Original ---')
print(paises_a_capitales)
capitales_a_paises = {}
for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais

print('\n--- Diccionario Invertido ---')
print(capitales_a_paises)


