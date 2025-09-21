instrumentos=[]
unidades=[] 

while True: 
    print('MENU DE OPCIONES')
    print("""
          1.Ingresar instrumentos
          2.Ingresar unidades disponibles
          3.Mostrar inventario
          4.Consultar unidades por instrumento
          5.Listar faltantes
          6.Agregar instrumento
          7.Actualizar unidades (disminuir / aumentar)
          8.Salir""")
    opcion=input('Ingresa la opción: ')
    if opcion=='1':
        cantidad_instrumentos= int(input('Ingresa la cantidad de intrumentos a registrar: '))
        for i in range(cantidad_instrumentos):
            instrumentos_ingresar=input('Instrumento Nro '+ str(i+1)+': ')
            instrumentos.append(instrumentos_ingresar)
    elif opcion=='2':
        for i in range(len(instrumentos)):
            cantidad=int(input('Ingresa la cantidad para "'+ instrumentos[i]+'": '))
            unidades.append(cantidad)
    elif opcion=='3':
        for i in range(len(instrumentos)):
            print('"'+str(instrumentos[i])+ ': '+ str(unidades[i])+ ' unidades"')






































