import csv
import os

CSV_FILE = "catalogo.csv"


# ----------------------------
# Utilidades (VALIDACIONES)
# ----------------------------

def normalizar_titulo(t: str) -> str:
    """
    Devuelve el título normalizado para comparación.
    Requisitos:
    - Quitar espacios sobrantes intermedios y extremos.
    - Pasar a minúsculas.
    implementar y devolver el string normalizado.
    """
    return " ".join(t.strip().split()).lower()



def titulo_valido(t: str) -> bool:
    """
    Un título es válido si, tras normalizar, no queda vacío.
    implementar y devolver True/False.
    """
    return normalizar_titulo(t) !=""


def pedir_titulo(msg: str) -> str:
    """
    Pide un título por input hasta que sea válido según las reglas del enunciado.
    Requisitos:
    - No vacío.
    - Comparación insensible a mayúsculas y con espacios normalizados.
    - Debe devolver el título ya normalizado para mostrar/guardar prolijo.
    implementar bucle de pedido y validación.
    """
    while True:
        # Quitamos espacios al inicio/final
        titulo = input(msg).strip() 
        if titulo_valido(titulo):
            # Devolvemos el título "limpio" (sin .lower())
            return " ".join(titulo.split())
        else:
            print("Error: El título no puede estar vacío. Intente de nuevo.")


def pedir_entero_no_negativo(msg: str) -> int:
    """
    Pide un entero >= 0 (usar validaciones simples como str.isdigit()).
    Debe volver a pedir si el valor no es válido.
    implementar bucle de pedido y validación; devolver int.
    """
    while True:
        valor_str = input(msg).strip()
        if valor_str.isdigit():
            return int(valor_str)
        else:
            print("Debe ingresar un número entero (0 o mayor).")


# ----------------------------
# Persistencia CSV
# ----------------------------

def cargar_catalogo_desde_csv() -> list[dict]:
    """
    Carga el catálogo desde CSV si existe.
    Formato: encabezado TITULO,CANTIDAD
    Requisitos mínimos:
    - Si no existe, devolver lista vacía.
    - Saltar filas inválidas.
    - Convertir CANTIDAD a int cuando corresponda.
        implementar lectura real con csv.DictReader.
    """
    catalogo: list[dict] = []
    try:
        if not os.path.exists(CSV_FILE):
            try:
                with open(CSV_FILE,'w', encoding='utf-8', newline='') as archivo:
                    columnas = ["TITULO", "CANTIDAD"]
                    escritor_csv= csv.DictWriter(archivo, fieldnames=columnas)
                    escritor_csv.writeheader()
                    print(f"ℹ️ Archivo '{CSV_FILE}' no encontrado. Se ha creado con encabezados.")
            except IOError as e:
                print(f"⛔ Error grave: No se pudo crear el archivo '{CSV_FILE}'. Error: {e}")
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if'CANTIDAD' in fila and ["CANTIDAD"].isdigit():
                    fila["CANTIDAD"] = int(fila["CANTIDAD"])
                    catalogo.append(fila)
    except IOError as e:
        print(f"⛔ Error grave: No se pudo leer el archivo '{CSV_FILE}'. Error: {e}")
    return catalogo


def guardar_catalogo_a_csv(catalogo: list[dict]) -> None:
    """
    Guarda el catálogo al CSV (sobrescribe).
    Columnas: TITULO,CANTIDAD (con encabezado)
    Requisitos:
    - Escribir siempre encabezado.
    - Asegurar que CANTIDAD sea entero no negativo.
    TODO: implementar escritura real con csv.DictWriter.
    """
    columnas = ["TITULO", "CANTIDAD"]
    with open(CSV_FILE, 'r', newline='', encoding='utf-8')as archivo:
        escritor= csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerow(catalogo)


# ----------------------------
# Búsquedas y reglas de negocio
# ----------------------------

def buscar_indice_por_titulo(catalogo: list[dict], titulo_busqueda: str) -> int:
    """
    Devuelve el índice del libro cuyo título coincide (comparación normalizada).
    Si no existe, devuelve -1.
        implementar recorrido y comparación con normalización.
    """
    titulo_norm_buscado=input('ingresa e titulo ue desea buscar: ')
    titulo_norm_buscado = normalizar_titulo(titulo_busqueda)
    for fila in catalogo:
        if fila['TITULO']== titulo_norm_buscado:
            
    
    return -1  # TODO


def existe_titulo(catalogo: list[dict], titulo: str) -> bool:
    """
    True si el título ya existe en el catálogo (comparación normalizada).
    TODO: implementar usando buscar_indice_por_titulo.
    """
    return False  # TODO


# ----------------------------
# Operaciones (CRUD / reportes)
# ----------------------------

def ingresar_titulos_multiples(catalogo: list[dict]) -> list[dict]:
    """
    1) Ingresar títulos (múltiples):
        - Pedir cuántos libros cargar.
        - Por cada uno: TITULO (no vacío, no duplicado) y CANTIDAD (>=0).
        - Guardar automáticamente tras cambios.
    Debe devolver el catálogo actualizado.
    TODO: implementar.
    """
    print("→ Ingresar títulos (múltiples): PENDIENTE DE IMPLEMENTAR")
    return catalogo  # TODO


def ingresar_ejemplares(catalogo: list[dict]) -> list[dict]:
    """
    2) Ingresar ejemplares a un título existente (sumar cantidad).
    Requisitos:
    - Verificar existencia del título.
    - Sumar cantidad (>=0).
    - Guardar automáticamente tras cambios.
    Debe devolver el catálogo actualizado.
    TODO: implementar.
    """
    print("→ Ingresar ejemplares: PENDIENTE DE IMPLEMENTAR")
    return catalogo  # TODO


def mostrar_catalogo(catalogo: list[dict]) -> None:
    """
    3) Mostrar catálogo completo (título + stock).
    Requisitos:
    - Formato simple, un libro por línea.
    - Indicar si el catálogo está vacío.
    TODO: implementar.
    """
    print("→ Mostrar catálogo: PENDIENTE DE IMPLEMENTAR")


def consultar_disponibilidad(catalogo: list[dict]) -> None:
    """
    4) Consultar disponibilidad de un título (mostrar cuántos ejemplares hay).
    Requisitos:
    - Verificar existencia del título.
    - Mostrar cantidad disponible.
    TODO: implementar.
    """
    print("→ Consultar disponibilidad: PENDIENTE DE IMPLEMENTAR")


def listar_agotados(catalogo: list[dict]) -> None:
    """
    5) Listar sólo títulos con CANTIDAD == 0.
    Requisitos:
    - Mostrar lista o indicar que no hay agotados.
    TODO: implementar.
    """
    print("→ Listar agotados: PENDIENTE DE IMPLEMENTAR")


def agregar_titulo(catalogo: list[dict]) -> list[dict]:
    """
    6) Agregar título individual (validar duplicados) con cantidad inicial.
    Requisitos:
    - TITULO válido y único.
    - CANTIDAD inicial >= 0.
    - Guardar automáticamente tras cambios.
    Debe devolver el catálogo actualizado.
    TODO: implementar.
    """
    print("→ Agregar título: PENDIENTE DE IMPLEMENTAR")
    return catalogo  # TODO


def actualizar_ejemplares_prestamo_devolucion(catalogo: list[dict]) -> list[dict]:
    """
    7) Actualizar ejemplares:
        - Préstamo: restar 1 sólo si CANTIDAD > 0.
        - Devolución: sumar 1.
        - Guardar automáticamente tras cambios.
    Debe devolver el catálogo actualizado.
    TODO: implementar.
    """
    print("→ Préstamo/Devolución: PENDIENTE DE IMPLEMENTAR")
    return catalogo  # TODO


# ----------------------------
# Menú e interacción (sin globales)
# ----------------------------

def mostrar_menu() -> None:
    print("""
================= MENÚ BIBLIOTECA =================
1 - Ingresar títulos (múltiples)
2 - Ingresar ejemplares
3 - Mostrar catálogo
4 - Consultar disponibilidad
5 - Listar agotados
6 - Agregar título
7 - Actualizar ejemplares (Préstamo/Devolución)
8 - Salir
===================================================
""")


def main() -> None:
    print("📚 Iniciando sistema de Biblioteca…")
    catalogo: list[dict] = cargar_catalogo_desde_csv()
    if len(catalogo) == 0:
        print("ℹ️ Catálogo vacío o CSV no encontrado.")
    else:
        print(f"✅ Catálogo cargado. {len(catalogo)} título(s).")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                catalogo = ingresar_titulos_multiples(catalogo)
            case "2":
                catalogo = ingresar_ejemplares(catalogo)
            case "3":
                mostrar_catalogo(catalogo)
            case "4":
                consultar_disponibilidad(catalogo)
            case "5":
                listar_agotados(catalogo)
            case "6":
                catalogo = agregar_titulo(catalogo)
            case "7":
                catalogo = actualizar_ejemplares_prestamo_devolucion(catalogo)
            case "8":
                print("👋 Saliendo. ¡Hasta luego!")
                break
            case _:
                print("⚠️ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()