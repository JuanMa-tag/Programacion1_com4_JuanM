from agregar_producto import producto_agregado

# Definimos el nombre del archivo
nombre_archivo = r'C:\Users\carri\Documents\GitHub\Programacion1_com4_JuanM\Trabajos Prácticos Campus\TP_MANEJO_DE_ARCHIVOS\productos.txt'
try:
    # Abrimos el archivo en modo lectura ('r')
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        # se descarta la primera línea (el encabezado)
        next(archivo) #salta 'nombre,precio,cantidad\n'
        print("--- Lista de Productos ---")
        # Iteramos sobre cada línea restante en el archivo
        for linea in archivo:
            #.strip() para quitar espacios y saltos de línea
            linea_limpia = linea.strip()
            #Verificamos que la línea no esté vacía
            datos = linea_limpia.split(',')
            nombre = datos[0]
            precio = datos[1]
            cantidad = datos[2]
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no se encontró.")

print("\n------------------------------------")
print("--- Agregar un nuevo producto ---")
print("------------------------------------")
producto_agregado(nombre_archivo)

#Cargar productos en una lista de diccionarios
# productos_cargados(nombre_archivo,datos)