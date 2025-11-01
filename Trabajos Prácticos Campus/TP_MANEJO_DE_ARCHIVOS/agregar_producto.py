# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente
def producto_agregado(nombre_archivo):
    # Pedimos los datos del nuevo producto por teclado
    nuevo_nombre = input("Ingrese el nombre del producto: ")
    nuevo_precio = input("Ingrese el precio: ")
    nueva_cantidad = input("Ingrese la cantidad: ")
    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
            #se agrega el nuevo producto
            nueva_linea = f"\n{nuevo_nombre},{nuevo_precio},{nueva_cantidad}"
            # Escribimos la nueva línea en el archivo
            archivo.write(nueva_linea)
        print(f"Producto '{nuevo_nombre}' agregado correctamente.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al escribir en el archivo: {e}")    