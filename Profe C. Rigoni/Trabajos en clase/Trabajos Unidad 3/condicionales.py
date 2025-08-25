fecha_actual = input("Ingrese el dia y la fecha en formato DD/MM: ")

#Divide las partes del dia con la fecha completa

partes = fecha_actual.split(",")

dia_semana = partes[0].strip().lower()
fecha = partes[1].strip()

#Divide la fecha "DD/MM"
fecha_partes = fecha.split("/")
dia_DD = int(fecha_partes[0])
mes_MM = int(fecha_partes[1])

if dia_DD < 1 or dia_DD > 31:
    print("El Dia es incorrecto")

if mes_MM < 1 or mes_MM > 12:
    print("El Mes es incorrecto")


if dia_semana != 'jueves' and dia_semana != 'viernes':
    exam = input("¿Hubo examenes?(Responder con si o no)").lower()
    if exam == 'si':
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
        porcentaje_aprobados = aprobados / (aprobados + desaprobados) * 100
        print(f"El porcentaje de aprobados es de: {porcentaje_aprobados}")
else:
    if dia_semana == 'jueves':
        asistencia = int(input("Ingrese el porcentaje de asistencia:"))
        if asistencia > 50:
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")
if dia_semana == 'viernes':
    if (dia_DD == 1 and (mes_MM == 1 or mes_MM == 7)):
        print("Comienzo de nuevo ciclo")
        alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel = float(input("Ingrese el arancel en $ por cada alumno: "))
        ingreso_total = alumnos * arancel
        print(f"El ingreso total en $ es: {ingreso_total}")
