habitaciones=[]
estados=[]

while True:
    print('Menu de opciones: ')
    print("""
          1.Ingresar números de habitación
          2.Ingresar estados (0/1) paralelos:
          3.Mostrar estado general
          4.Consultar estado de una habitación:
          5.Listar ocupadas o libres (según lo que se pida)
          6.Agregar habitación
          7.Ver libres
          8.Cambiar estado
          9.Ver todas
          10.Salir
          """)
    opcion=input('Ingresa la opción que desee: ')
    if opcion=='1':
        cant=int(input('Cuantas habitaciones desea ingresar: '))
        for i in range(cant):
            num_hab=input('Ingresa el numero de la habitación: ')
            habitaciones.append(num_hab)
    elif opcion=='2':
        for i in range(len(habitaciones)):
            num_estados = int(input('Ingresa el estado de la habitación ' + str(habitaciones[i]) + ' : '))
            estados.append(num_estados)
    elif opcion=='3':
        for i in range(len(habitaciones)):
            if estados[i]==0:
                print('La habitación "',(habitaciones[i]),'" libre')
            elif estados[i]==1:
                print('La habitación "',(habitaciones[i]),'" ocupada')    
    elif opcion== '4':
        buscar_hab=input('Ingresa el numero de la habitación: ')
        for i in range(len(habitaciones)):    
            if buscar_hab in habitaciones[i]:
                if estados[i]==0:
                    print('La habitación "',(habitaciones[i]),'" libre')
                elif estados[i]==1:
                    print('La habitación "',(habitaciones[i]),'" ocupada')
    elif opcion=='5':
        elegir=int(input('Ingresa "1" para ver las ocupadas o "0" para ver las libres: '))
        for i in range(len(habitaciones)):
            if elegir==1:
                if estados[i] ==0:
                    print(habitaciones[i])
            elif elegir==0:
                if estados[i] == 1:
                    print(habitaciones[i])
    elif opcion=='6':
        nueva_hab=input('Ingresa la nueva habitación: ')
        nuevo_estado=input('Ingresa el estado, Libre "0"/Ocupada "1": ')
        habitaciones.append(nueva_hab)
        estados.append(nuevo_estado)
    elif opcion=='7':
        for i in range(len(habitaciones)):
            if estados[i] == 0:
                print(habitaciones[i])
    elif opcion== '8':
        cambiar_estado=input('Ingresa la habitación que desea actualizar: ')           
        for i in range(len(habitaciones)):
            if cambiar_estado in habitaciones[i]:
                estados[i]=int(input('Ingresa el estado de la habitacion: '))
                print('La habitación "',(habitaciones[i]),'" Se actualizo' )
                print(estados[i])
                   
                   











# print('La habitación ',(habitaciones[i]),' ocupada')
           
# print('La habitación ',(habitaciones[i]),)


