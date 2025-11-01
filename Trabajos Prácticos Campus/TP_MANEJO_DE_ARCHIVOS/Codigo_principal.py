from agregar_producto import producto_agregado
from Cargar_en_diccionario import productos_cargados
from Mostrar_el_producto import mostrar_prod
from Guardar_productos import guardar_productos_actualizados
productos=productos_cargados()
# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:

# Definimos el nombre del archivo
nombre_archivo = r'C:\Users\carri\Documents\GitHub\Programacion1_com4_JuanM\Trabajos Prácticos Campus\TP_MANEJO_DE_ARCHIVOS\productos.txt'
try:
    # Abrimos el archivo en modo lectura ('r')
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas=archivo.readlines()
            for linea in lineas[1:]:
                partes=linea.strip().split(",")
                print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no se encontró.")


print("""
    1.Desea agregar un producto
    2.cargar en dicconario
    3.Mostrar productos
        """)
opcion=int(input('Ingresa la opción deseada: '))
match opcion:
    case 1:
        print("\n------------------------------------")
        print("--- Agregar un nuevo producto ---")
        print("------------------------------------")
        producto_agregado(nombre_archivo)
    case 2:
        #Cargar productos en una lista de diccionarios
        print(productos)
    case 3:
        mostrar_prod(productos)
    case 4:
          guardar_productos_actualizados(nombre_archivo, productos)