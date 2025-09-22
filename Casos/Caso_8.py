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
    if opcion=='1':#Ingresar instrumentos
        cantidad_instrumentos= int(input('Ingresa la cantidad de intrumentos a registrar: '))
        for i in range(cantidad_instrumentos):
            instrumentos_ingresar=input('Instrumento Nro '+ str(i+1)+': ')
            if instrumentos_ingresar not in instrumentos:
                instrumentos.append(instrumentos_ingresar)
            else:
                print('Instrumento repetido, ingresa otro')   
                instrumentos_ingresar=input('Instrumento Nro '+ str(i+1)+': ')
                instrumentos.append(instrumentos_ingresar)
    elif opcion=='2':#Ingresar unidades disponibles
        for i in range(len(instrumentos)):
            cantidad=int(input('Ingresa la cantidad para "'+ instrumentos[i]+'": '))
            if cantidad< 0:
                print('La cantidad no es valida')
                cantidad=int(input('Ingresa la cantidad para "'+ instrumentos[i]+'": '))
                unidades.append(cantidad)
            else:
                unidades.append(cantidad)
    elif opcion=='3':#Mostrar inventario
        for i in range(len(instrumentos)):
            print('"'+str(instrumentos[i])+ ': '+ str(unidades[i])+ ' unidades"')
    elif opcion=='4':#Consultar unidades por instrumento
        buscar_instrumento=input('Ingresa el instrumento a consultar: ')
        if buscar_instrumento not in instrumentos:
                print('El instrumento no existe')
        for i in range(len(instrumentos)):
            if buscar_instrumento == instrumentos[i]:
                print(''+str (unidades[i]) + ' unidades')
    elif opcion=='5':#Listar faltantes
        for i in range(len(instrumentos)):
            if unidades[i]==0:
                print('clase "'+str (instrumentos[i] +'" no disponible'))
    elif opcion=='6':#Agregar instrumento
        agregar_instr=input('Ingresa el instrumento que desea agregar: ')
        if agregar_instr in instrumentos:
            print('El instrumento ya fue ingresado')
            agregar_instr=input('Ingresa el instrumento que desea agregar: ')
            instrumentos.append(agregar_instr) 
        else:
            instrumentos.append(agregar_instr)    
        agregar_unidades=int(input('Ingresa las unidades del instrumento:'))
        if agregar_unidades<0:
            print('La cantidad no es valida')
            agregar_unidades=int(input('Ingresa las unidades del instrumento:'))
            unidades.append(agregar_unidades)   
        else:
            unidades.append(agregar_unidades)   
    elif opcion=='7':# Actualizar unidades (disminuir / aumentar)
        opcion_actualizar=int(input('Ingresa "1" para prestar un instrumento/ "2" para reponer un instrumento:  '))           
        inst_actualizar=input('Ingresa el instrumento que desea actualizar: ')
        for i in range(len(instrumentos)):
            if inst_actualizar not in instrumentos:
                print('El instrumento no es válido')
            else:
                if inst_actualizar==instrumentos[i]:
                    if opcion_actualizar==1:
                        if unidades[i]==0:
                            print('No hay instrumentos disponibles')
                        else:
                            unidades[i]-=1
                    elif opcion_actualizar==2:
                        unidades[i]+=1
    elif opcion=='8':#salir
        break                             
            








































