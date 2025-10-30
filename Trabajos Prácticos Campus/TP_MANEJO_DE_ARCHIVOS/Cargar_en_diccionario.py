
def productos_cargados(nombre_archivo,datos):
    nuevo_producto_dic = {
    'nombre': datos[0],
    'precio': (datos[1]),
    'cantidad': (datos[2])
    }



    # --- Configuración ---
nombre_archivo = r'C:\Users\carri\Documents\GitHub\Programacion1_com4_JuanM\Trabajos Prácticos Campus\TP_MANEJO_DE_ARCHIVOS\productos.txt'

# --- 1. Crear la lista vacía ---
# Aquí guardaremos todos los diccionarios
productos = [] 

print(f"Cargando productos desde '{nombre_archivo}'...")

try:
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        
        # Saltamos el encabezado
        next(archivo)
        
        # --- 2. Iterar y cargar los datos ---
        for linea in archivo:
            linea_limpia = linea.strip()
            
            if linea_limpia: # Asegurarnos de que no es una línea vacía
                # "Manzanas,2.50,10" -> ['Manzanas', '2.50', '10']
                datos = linea_limpia.split(',')
                
                # --- 3. Crear el diccionario (¡La parte clave!) ---
                # Asignamos cada dato a su clave correspondiente
                # ¡Importante! Convertimos precio y cantidad a números
                nuevo_producto_dic = {
                    'nombre': datos[0],
                    'precio': float(datos[1]),  # Convertimos a número decimal
                    'cantidad': int(datos[2])   # Convertimos a número entero
                }
                
                # --- 4. Agregar el diccionario a la lista ---
                productos.append(nuevo_producto_dic)

    print("¡Carga completada!")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta: {nombre_archivo}")
except Exception as e:
    print(f"Ocurrió un error inesperado durante la carga: {e}")

# --- 5. (Opcional) Mostrar la lista resultante ---
# Imprimimos la lista completa para verificar que se cargó bien.
print("\n--- Contenido de la lista 'productos' ---")
print(productos)

# Puedes imprimirlo de forma más legible (opcional)
print("\n--- Productos cargados (uno por uno) ---")
for p in productos:
    print(p)