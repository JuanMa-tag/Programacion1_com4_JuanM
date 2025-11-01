# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

def guardar_productos_actualizados(nombre_archivo, productos):
    try:
        archivo_productos_txt = r'C:\Users\carri\Documents\GitHub\Programacion1_com4_JuanM\Trabajos Prácticos Campus\TP_MANEJO_DE_ARCHIVOS\productos.txt'
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("nombre,precio,cantidad\n")      
            # Recorrer la lista y escribir cada producto ---
            for producto in productos:
                # Convertimos los valores (que podrían ser números) 
                # de nuevo a strings
                nombre = str(producto['nombre'])
                precio = str(producto['precio'])
                cantidad = str(producto['cantidad'])
                # Creamos la línea de texto formato CSV
                linea = f"{nombre},{precio},{cantidad}\n"
                # Escribimos la línea en el archivo
                archivo.write(linea)
                
        print(f"\n¡Éxito! Se guardaron {len(productos)} productos en el archivo '{nombre_archivo}'.")
        
    except IOError as e:
        # Buena práctica: manejar errores por si no se puede escribir
        print(f"\nError al guardar el archivo: {e}")

