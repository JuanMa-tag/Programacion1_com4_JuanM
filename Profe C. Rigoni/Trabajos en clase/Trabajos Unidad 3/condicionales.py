semana = ["lunes","martes","miercoles","jueves","viernes"]

semana1 = input("Ingrese el dia y la fecha en formato DD/MM: ")

#Divide las partes del dia con la fecha completa

partes = semana1.split(",")

dia_semana = partes[0].strip().lower()
fecha = partes[1].strip()

#Divide la
fecha_partes = fecha.split("/")
dia = int(fecha_partes[0])
mes = int(fecha_partes[1])

if dia < 1 or dia > 31:
    print("Dia incorrecto")

if mes < 1 or mes > 12:
    print("Mes incorrecto")

if dia_semana != 'jueves' and dia_semana != 'viernes':
    exam = input("¿Hubo examenes?(Responder con Si o No)").lower
    if exam == 'si':
        aprobados = input(int("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados = input(int("Ingrese la cantidad de alumnos desaprobados"))
        porcentaje = aprobados / (aprobados + desaprobados) * 100
        print(f"El porcentaje de aprobados es de: {porcentaje}")
else:
    if dia_semana == 'jueves':
        asistencia = input(int("Ingrese el porcentaje de asistencia:"))
        if asistencia > 50:
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")
  



    
