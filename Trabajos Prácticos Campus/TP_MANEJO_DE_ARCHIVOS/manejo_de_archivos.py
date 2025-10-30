def metodo_r():
    nombre_archivo = r'C:\Users\carri\Documents\GitHub\Programacion1_com4_JuanM\Trabajos Prácticos Campus\TP_MANEJO_DE_ARCHIVOS\productos.txt'
    try:
        # Abrimos el archivo en modo lectura ('r')
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # se descarta la primera línea (el encabezado)
            next(archivo) #salta 'nombre,precio,cantidad\n'
            for linea in archivo:
            #.strip() para quitar espacios y saltos de línea
                linea_limpia = linea.strip().split()
                #Verificamos que la línea no esté vacía
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")     
           