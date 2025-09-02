letras_abc="abcdefghijklmnopqrstuvxyz"
cant=5
for cant in range(5):
    print('-------------------------')
    print('OFICIAL', 1+cant)
    mensaje = input("Ingrese su mensaje: ")
    corrimiento=int(input("Ingrese el corrimiento deseado: "))
    for letra_mensaje in mensaje:
         if letra_mensaje in letras_abc:
              for i in range(len(letras_abc)):
                  if letra_mensaje == letras_abc[i]:
                      nueva_pos=(i + corrimiento)%26
                      nueva_letra= letras_abc[nueva_pos]
                      cifrado=cifrado+nueva_letra
    print(cifrado)









