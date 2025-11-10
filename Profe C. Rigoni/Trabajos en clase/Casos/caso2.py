alumnos=[]
asistencias=[]
terminar=1
while True:
    print("""
        1.Ingresar nombres de estudiantes
        2.Mostrar listado con asistencias
        3.Consultar asistencias por estudiante
        4.Listar estudiantes con asistencia "0"
        5.Marcar asistencia
        6.Salir""")
    opcion=input('INGRESA LA OPCIÓN: ')
    if opcion=='1':  # 1.	Ingresar nombres de estudiantes: (Registrar los alumnos del curso)
        cant=int(input('ingresa la cantidad de alumnos que desea ingresar: '))
        for i in range(cant):
            alumno_agregado=input(f"Alumno {i+1}: ")
            alumnos.append(alumno_agregado)
            asistencias.append(0)
    elif opcion=='2':  #Mostrar listado con asistencias
        for i in range(len(alumnos)):
            print(f'{alumnos[i]} : {asistencias[i]} asistencias ')
    elif opcion=='3': #Consultar asistencias por estudiante
        nombre_buscar=input('Ingeresa el nombre del alumno que desea encontrar: ')
        for i in range(len(alumnos)):
            if nombre_buscar in alumnos[i]:
                print(f'{asistencias[i]} asistencias')
    elif opcion=='4':#Listar estudiantes con asistencia 0
            for i in range(len(asistencias)):
                if asistencias[i] == 0:
                    print(f'{alumnos[i]} : {asistencias[i]} asistencias')
    elif opcion== '5':
        nombre_alumno=input('Ingresa el nombre del alumno: ')
        for i in range(len(alumnos)):
            if nombre_alumno in alumnos[i]:
                asis=int(input("Ingresar cantidad de asistencias a sumar: "))
                asistencias[i]+=asis
                print(f'El alumno ahora tiene {asistencias[i]} asistencias')
    elif opcion=='6':
        break