#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad_usuario= int(input('ingrese su edad: '))
if edad_usuario > 18:
    print('Es mayor de edad')
print(' ')

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# # mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# # mensaje “Desaprobado”.
nota = float(input('ingrese su nota: '))
if nota>= 6:
    print('Aprobado')
else:
    print('Desaprobado')
print(' ')
 
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par".
numero= int(input('ingrese un número par: '))
if numero % 2 == 0:
    print('Ha ingresado un número par')
else:
    print('Por favor, ingrese un número par')
print(' ')

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
edad_ola= int(input('ingrese su edad: '))
if edad_ola <12:
    print('Niño/a')
elif edad_ola >= 12 and edad_ola < 18:
    print('Adolescente')
elif edad_ola >= 18 and edad_ola < 30:
    print('Adulto/a joven')
elif edad_ola >= 30:
    print('Adulto/a')
print(' ')

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"
contraseña= input('ingrese una contraseña entre 8 y 14 caracteres: ')
long_contraseña= len(contraseña)
if long_contraseña >= 8 and long_contraseña <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')










    # 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
frase= input('ingrese un palabra o frase: ')
vocales= ['a','e','i','o','u','A','E','I','O','U']
if frase[-1] in vocales:
    print(frase + '!')
else:
    print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas.
# 2. Si quiere su nombre en minúsculas.
# 3. Si quiere su nombre con la primera letra mayúscula.
nombre= input('Ingrese su nombre: ')
print('ingrese un numero 1, 2 o 3 : ')
print('ingrese 1 si quiere su nombre en mayúscula')
print('ingrese 2 si quiere su nombre en minúscula')
print('ingrese 3 si quiere su nombre en formato título')
num_opcion= input('ingrese su opción: ')
if num_opcion== '1':
    print(nombre.upper())
elif num_opcion== '2':
    print(nombre.lower())
elif num_opcion== '3':
    print(nombre.title())
print(' ')

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
magnitud= int(input('ingrese la magnitud del terremoto: '))
if magnitud< 3:
    print('Muy leve (imperceptible)')
elif magnitud >= 3 and magnitud < 4:
    print('Leve (ligeramente perceptible).')
elif magnitud >= 4 and magnitud < 5:
    print('Moderado (sentido por personas, pero generalmente no causa daños).')
elif magnitud >= 5 and magnitud < 6:
    print('Fuerte (puede causar daños en estructuras débiles).')
elif magnitud >= 6 and magnitud < 7:
    print('Muy Fuerte (puede causar daños significativos).')
elif magnitud >= 7:
    print('Extremo (puede causar graves daños a gran escala).')

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio= input('Ingrese el hemisferio donde se encuentra (norte/sur): ').lower()
mes_del_año= input('Ingrese un mes del año : ').lower()
dia=int(input('ingrese un dia: '))

#------- HEMISFERIO SUR ------- 
if hemisferio == 'sur':
    ## Primera Estación: (VERANO)
    if (mes_del_año == 'enero') or (mes_del_año == 'febrero'):
         if dia >= 1 and dia <31:
                 print('¡¡VERANO!!')
               
    ## Segunda Estacion: (OTOÑO)            
    elif (mes_del_año == 'abril') or (mes_del_año == 'mayo'):
        if dia >= 1 and dia <=31:
                print('¡¡OTOÑO!!')              
    ## Tercera Estación: (INVIERNO)
    elif (mes_del_año == 'julio') or (mes_del_año == 'agosto'):
        if dia >= 1 and dia <=31:
                print('¡¡INVIERNO!!')


    # ---------MESES CON ESTACIONES COMPARTIDAS---------
    # Marzo: (Verano-Otoño)
    if mes_del_año =='marzo':
            if dia <=20:
                print('¡¡VERANO!!')
            else:
                if dia >=21:
                    print('¡¡OTOÑO!!')
    #Junio: (Otoño-Invierno)
    if mes_del_año == 'junio':
            if dia <= 20 :
                print('¡¡OTOÑO!!')
            else:
                if dia >=21:
                    print('¡¡INVIERNO!!')
    #Septiembre: (Invierno-Primavera)
    if mes_del_año == 'septiembre':
            if dia <= 20 :
                print('¡¡INVIERNO!!')
            else:
                if dia >=21:
                    print('¡¡PRIMAVERA!!')
    #Diciembre: (Primavera-Verano)
    if mes_del_año == 'diciembre':
            if dia <= 20 :
                print('¡¡PRIMAVERA!!')
            else:
                if dia >=21:
                    print('¡¡VERANO!!')
    #-----------------------------------------------
 #------- HEMISFERIO NORTE-------- 
else:
    if hemisferio == 'norte':
        ## Primera Estación: (INVIERNO)
        if (mes_del_año == 'enero') or (mes_del_año == 'febrero'):
            if dia >= 1 and dia <31:
                 print('¡¡INVIERNO!!')
        ## Segunda Estacion: (OPRIMAVERA)            
        elif (mes_del_año == 'abril') or (mes_del_año == 'mayo'):
            if dia >= 1 and dia <=31:
                print('¡¡PRIMAVERA!!')         
        ## Tercera Estación: (VERANO)
        elif (mes_del_año == 'julio') or (mes_del_año == 'agosto'):
            if dia >= 1 and dia <=31:
                print('¡¡VERANO!!')
    # ---------MESES CON ESTACIONES COMPARTIDAS---------
        # Marzo: (Invierno-Primavera)
        if mes_del_año =='marzo':
                if dia <=20:
                    print('¡¡INVIERNO!')
                else:
                     if dia >=21:
                            print('¡¡PRIMAVERA!!')    
        #Junio: (Primavera-Verano)
        if mes_del_año == 'junio':
                if dia <= 20 :
                    print('¡¡PRIMAVERA!!')
                else:
                    if dia >=21:
                        print('¡¡VERANO!')
        #Septiembre: (Verano-Otoño)
        if mes_del_año == 'septiembre':
                if dia <= 20 :
                    print('¡¡VERANO!!')
                else:
                    if dia >=21:
                        print('¡¡OTOÑO!!')
        #Diciembre: (Otoño-Invierno)
        if mes_del_año == 'diciembre':
                if dia <= 20 :
                    print('¡¡OTOÑO!!')
                else:
                    if dia >=21:
                        print('¡¡INVIERNO!!')


