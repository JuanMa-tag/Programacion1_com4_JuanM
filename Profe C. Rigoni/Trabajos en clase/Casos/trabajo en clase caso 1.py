titulos=[]
ejemplares=[]
terminar = False
while terminar != True:
    print('---------------------------------------')
    print('--------MENU DE OPCIONES---------')
    print('1. ingresa lista de titulos ')
    print('2. Ingresar lista de ejemplares disponibles "(por título)"')
    print('3. Mostrar catálogo con stock:')
    print('4. Consultar disponibilidad de un título específico')
    print('5. Listar agotados')
    print('6. Agregar título')
    print('7. Ver títulos agotados')
    print('8. Actualizar ejemplares (préstamo/devolución')
    print('9. Ver catálogo')
    print('10. Salir')

    opcion= input('ingresa la opcion: ')


    if opcion == '1': #Ingresar lista de títulos
        cantidad_titulos= int(input('cuantos titulos desea agregar: '))
        for i in range(cantidad_titulos):
            nuevo= input(f'Ingresa el titulo {i+1} : ')
            titulos.append(nuevo)


    elif opcion == '2': #Ingresar lista de ejemplares disponibles (por título):
        for i in range(cantidad_titulos):
            nuevos=input(f'ingresa los ejemplares para "{titulos[i]}" : ')
            ejemplares.append(nuevos)


    elif opcion == '3': #Mostrar catálogo con stock
        if len(titulos)==0:
            print('No hay titulos')
        else:
            for i in range(len(titulos)):
                print(f'"{titulos[i]}" tiene: {ejemplares[i]} copias')


    elif opcion == '4': #Consultar disponibilidad de un título específico
        buscar= input('ingresa el titulo que desea buscar (sin errores): ')
        if buscar in titulos:
            encon= titulos.index(buscar)
            print(f'"{titulos[encon]}" tiene {ejemplares[encon]} copias')
        else:
            print('¡Titulo no encontrado!')


    elif opcion =='5': #Listar agotados (0 ejemplares)
        for i in range(cantidad_titulos):
            if ejemplares[i] == '0':
                print(f'Los ejemplares agotados son: "{titulos[i]}" ')


    elif opcion== '6': #Agregar título
        nuevo_titulo=input('Ingresa el titulo que quieres agregar: ')
        titulos.append(nuevo_titulo)
        copias_nuevas=int(input('ingresa la cantidad de copias del titulo ingresado: '))
        ejemplares.append(copias_nuevas)


    elif opcion =='7': #Ver títulos agotados
        for i in range(cantidad_titulos):
            if ejemplares[i] == '0':
                print(f'Los titulos sin copias son: "{titulos[i]}" ')


    elif opcion =='8': #Actualizar ejemplares (préstamo/devolución)
        act_ejemp=input('1. prestamo - 2.devolucion: ')
        if act_ejemp =='1':
                titulo_prestado=input('Ingresa el titulo que fue prestado: ')
                if titulo_prestado in titulos:
                    pos= titulos.index(titulo_prestado)
                    nueva_cantidad= int(input(f'Ingrese la cantidad de ejemplares para "{titulo_prestado}": '))
                    ejemplares[pos]= nueva_cantidad
                    print(f'El número de ejemplares de "{titulo_prestado}" se actualizó a {ejemplares[pos]}')
        elif act_ejemp =='2':
                titulo_devuelto= input('ingresa el titulo que fue devuelto: ')
                if titulo_devuelto in titulos:
                    posi= titulos.index(titulo_devuelto)
                    cantidad_actualizada= int(input(f'Ingrese la cantidad de ejemplares para "{titulo_devuelto}": '))
                    ejemplares[posi]= cantidad_actualizada
                    print(f'El número de ejemplares de "{titulo_devuelto}" se actualizó a {ejemplares[posi]}')

    elif opcion=='9': #Ver catálogo:
        print(f'El catalogo de titulos enteros es: {titulos}')


    elif opcion =='10':
       terminar=True



