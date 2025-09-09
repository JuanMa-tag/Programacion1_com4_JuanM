
hemisferio= input('Ingrese el hemisferio donde se encuentra (norte/sur): ').lower()
mes_del_año= input('Ingrese un mes del año : ').lower()
dia=int(input('ingrese un dia: '))

#------- HEMISFERIO SUR ------- 
if hemisferio == 'sur':
    ## Primera Estación: (VERANO)
    if (mes_del_año == 'diciembre') or (mes_del_año == 'enero') or (mes_del_año == 'febrero'):
        if mes_del_año == 'diciembre':
            if dia >= 21 and dia <=31:
                print('¡¡VERANO!!')                   
        else: 
             if dia >= 1 and dia <31:
                 print('¡¡VERANO!!')
               

                

    ## Segunda Estacion: (OTOÑO)            
    elif (mes_del_año == 'abril') or (mes_del_año == 'mayo'):
        if dia >= 1 and dia <=31:
                print('¡¡OTOÑO!!')              
    
    if mes_del_año =='marzo':
            if dia <=20:
                print('¡¡VERANO!!')
            else:
                if dia >=21:
                    print('¡¡OTOÑO!!')

    if mes_del_año == 'junio':
            if dia <= 20 :
                print('¡¡OTOÑO!!')
            else:
                if dia >=21:
                    print('¡¡INVIERNO!!')
                               
                           
                





    



            
 






    