
hemisferio= input('Ingrese el hemisferio donde se encuentra (norte/sur): ')
mes_del_año= input('Ingrese un mes del año en números: ')
dia=int(input('ingrese un dia: '))
inicio_verano=(12,21)
# HEMISFERIO SUR 
if hemisferio == 'sur':
    if mes_del_año and dia >= inicio_verano or (mes_del_año== 3 and dia <=20):
        print('VERANO')

    



