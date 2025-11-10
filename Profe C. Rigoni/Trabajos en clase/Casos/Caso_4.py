clases=[]
cupos=[]
while True:
    print('----MENU DE OPCIONES----')
    print("""
        1.Ingresar lista de clases
        2.Ingresar cupos por clase
        3.Mostrar clases con cupo
        4.Consultar cupo de una clase
        5.Listar clases sin cupo
        6.Agregar clase
        7.Actualizar cupos (inscribir/baja)
        8.Salir
    """)
    opcion=input('Ingresa la opcion deseada: ')
    if opcion=='1':
        cant=int(input('Ingresa la cantidaad de clases que desea agregar: '))
        for i in range(cant):
            clase_ingresada=input('Ingresa la clase: ')
            if clase_ingresada==' ':
                print('clase no valida ')
            elif clase_ingresada in clases:
                print('La clase ingresada ya fue registrada ')
            else:
                clases.append(clase_ingresada)        
    elif opcion=='2':
        for i in range(len(clases)):
            print('Ingresa el cupo para cada clase')
            cupos_ingresado=int(input('"'+ str(clases[i])+'": '))
            if cupos_ingresado <= 0:
                print('El número del cupo no es valido')
            else:
                cupos.append(cupos_ingresado)
    elif opcion=='3':
        for i in range(len(clases)):
            print('Clase "'+ clases[i]+ '": '+ str(cupos[i])+ ' cupos')
    elif opcion=='4':
        buscar_clase=input('Ingresa la clase que desea consultar: ')
        for i in range(len(clases)):
            if buscar_clase in clases[i]:
                    print('"',clases[i],'"')
                    print(cupos[i],' cupos disponibles')
                    break
            else:
                if buscar_clase not in clases[i]:
                    print('La clase no fue encontrada') 
                    break       
    elif opcion=='5':
        for i in range(len(clases)):
            if cupos[i]==0:
                print('La clase ',clases[i], ' no tiene cupos disponibles')
    elif opcion=='6':
        nueva_clase=input('Ingresa la nueva clase: ')
        if nueva_clase==' ':
            print('clase no valida ')
        else:
            clases.append(nueva_clase)
            nuevo_cupos=int(input('Ingresa la cantidad de cupos disponibles: '))
            cupos.append(nuevo_cupos)
    elif opcion =='7':
        alumno=int(input('Ingresa  1. Para inscribir un alumno/  2. Para  dar de baja a un alumno: '))
        clase_del_alumno=input('Ingresa la clase que quieras actualizar: ')
        for i in range(len(clases)):
            if clase_del_alumno == clases[i]:
                if alumno ==1:
                    if cupos[i]==0:
                        print('La clase no tiene cupos disponibles')
                    else:
                        cupos[i]= cupos[i]-1
                elif alumno==2:
                    cupos[i]= cupos[i]+1
    elif opcion=='8':
        print('GRACIASS')
        break
