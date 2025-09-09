
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
#------------------------------------------------
#------- HEMISFERIO NORTE ------- 
else:
    if hemisferio == 'norte':
        ## Primera Estación: (VERANO)
        if (mes_del_año == 'enero') or (mes_del_año == 'febrero'):
            if dia >= 1 and dia <31:
                 print('¡¡INVIERNO!!')
        ## Segunda Estacion: (OTOÑO)            
        elif (mes_del_año == 'abril') or (mes_del_año == 'mayo'):
            if dia >= 1 and dia <=31:
                print('¡¡OTOÑO!!')         











      