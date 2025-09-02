#TP bucles 


abecedario="abcdefghijklmnopqrstuvxyz"
mensaje = input("Ingrese su mensaje: ")
corrimiento=int(input("Ingrese el corrimiento deseado: "))
cifrado=""
cant=5
for cant:
for letra_mensaje in mensaje:
    if letra_mensaje in abecedario:
        for i in range(len(abecedario)):
          if letra_mensaje == abecedario[i]:
              nueva_pos=(i + corrimiento)%26
              nueva_letra= abecedario[nueva_pos]
              cifrado=cifrado+nueva_letra
print(cifrado)








