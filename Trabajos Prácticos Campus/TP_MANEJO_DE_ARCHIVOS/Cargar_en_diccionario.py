# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.
def productos_cargados():
    productos=[]
    nombre_archivo = r'C:\Users\carri\Documents\GitHub\Programacion1_com4_JuanM\Trabajos Prácticos Campus\TP_MANEJO_DE_ARCHIVOS\productos.txt'
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas=archivo.readlines()
        for linea in lineas[1:]:
            lista_productos=linea.strip().split(",")
            nuevos_productos={'nombre':lista_productos[0], 'precio':lista_productos[1], 'cantidad':lista_productos[2]}
            productos.append(nuevos_productos)
        return (productos)


