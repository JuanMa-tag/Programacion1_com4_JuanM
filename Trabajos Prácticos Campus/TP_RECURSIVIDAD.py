def recursividad(factorial):
    if factorial==0:
        return 1
    else:
        return recursividad(factorial -1)*factorial


opcion=int(input('Ingrese un numero: '))
print(recursividad(opcion))



