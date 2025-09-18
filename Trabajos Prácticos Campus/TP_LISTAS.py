# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.
lista_multiplo= list(range(0,101,4))
print(lista_multiplo)


# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. 
penultimo_elemento=['hola', 'UTN', 0.5, 4, False ]
print(penultimo_elemento[-2])


# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla.
lista_vacia=[]
for i in range(3):
    palabras=input(f'Ingresa la palabra Nro {i+1}: ')
    lista_vacia.append(palabras)

print(lista_vacia)


# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. 
animales = ["perro", "gato", "conejo", "pez"]

animales[1]='loro'
animales[-1]='oso'
print(animales)


# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7] #Acá se crea la lista y se le agregan elementos.
numeros.remove(max(numeros))# Acá con la funcion max se busca el numero mayor y con remove se elimina el numero buscado.
print(numeros)# Se imprime la lista sin el elemento que se eliminó.









































