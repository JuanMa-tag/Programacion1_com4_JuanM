# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.
def mostrar_prod(productos):
    nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ")
    encontrado = False 
    # Recorremos la lista de productos
    for producto in productos:
        if producto['nombre'].lower() == nombre_buscado.lower():
            print("\n--- Producto Encontrado ---") #Si se encuentra e producto se imprime
            print(f"Nombre:   {producto['nombre']}")
            print(f"Precio:   ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            encontrado = True
            break  # Salimos del bucle porque ya lo encontramos
    if not encontrado:
        print(f"\nLo sentimos, el producto '{nombre_buscado}' no se encuentra en la lista.")