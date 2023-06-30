productos = []

def grabar_producto():
    id_producto = input("Ingrese el ID del producto (3 letras y 3 números): ")
    while not validar_id(id_producto):
        id_producto = input("ID inválido. Ingrese nuevamente: ")

    tipo_producto = input("Ingrese el tipo de producto (8 caracteres o más): ")
    while len(tipo_producto) < 8:
        tipo_producto = input("Tipo de producto inválido. Ingrese nuevamente: ")

    marca = input("Ingrese la marca del producto: ")
    modelo = input("Ingrese el modelo del producto: ")

    stock = int(input("Ingrese el stock del producto (igual o mayor a 10): "))
    while stock < 10:
        stock = int(input("Stock inválido. Ingrese nuevamente: "))

    precio = float(input("Ingrese el precio del producto: "))
    while precio <= 0:
        precio = float(input("Precio inválido. Ingrese nuevamente: "))

    producto = {
        'id': id_producto,
        'tipo': tipo_producto,
        'marca': marca,
        'modelo': modelo,
        'stock': stock,
        'precio': precio
    }
    productos.append(producto)
    print("Producto grabado exitosamente.")

def eliminar_producto(id_producto):
    producto_encontrado = None
    for producto in productos:
        if producto['id'] == id_producto:
            producto_encontrado = producto
            break

    if producto_encontrado:
        productos.remove(producto_encontrado)
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")

def validar_id(id_producto):
    if len(id_producto) != 6:
        return False
    letras = id_producto[:3]
    numeros = id_producto[3:]
    if not letras.isalpha() or not numeros.isdigit():
        return False
    return True

def buscar_producto():
    id_producto = input("Ingrese el ID del producto a buscar: ")
    producto_encontrado = None
    for producto in productos:
        if producto['id'] == id_producto:
            producto_encontrado = producto
            break

    if producto_encontrado:
        print("Información del producto:")
        print(f"ID: {producto_encontrado['id']}")
        print(f"Tipo: {producto_encontrado['tipo']}")
        print(f"Marca: {producto_encontrado['marca']}")
        print(f"Modelo: {producto_encontrado['modelo']}")
        print(f"Stock: {producto_encontrado['stock']}")
        print(f"Precio: {producto_encontrado['precio']}")
    else:
        print("Producto no encontrado.")

def imprimir_reporte():
    print("  Reporte de productos  ")
    for producto in productos:
        print(f"ID: {producto['id']}")
        print(f"Tipo: {producto['tipo']}")
        print(f"Marca: {producto['marca']}")
        print(f"Modelo: {producto['modelo']}")
        print(f"Stock: {producto['stock']}")
        print(f"Precio: {producto['precio']}")
        print("")

def imprimir_cotizacion():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    print("\n=== Cotización ===")
    print(f"Cliente: {nombre_cliente}\n")
    
    cotizacion = []
    continuar = True
    while continuar:
        id_producto = input("Ingrese el ID del producto: ")
        producto = buscar_producto_por_id(id_producto)
        if producto:
            cantidad = int(input("Ingrese la cantidad deseada: "))
            precio_unitario = producto['precio']
            subtotal = precio_unitario * cantidad

            cotizacion.append({
                'producto': producto,
                'cantidad': cantidad,
                'precio_unitario': precio_unitario,
                'subtotal': subtotal
            })
            print("Producto agregado a la cotización.")
        else:
            print("Producto no encontrado.")

        opcion = input("¿Desea agregar otro producto a la cotización? (s/n): ")
        if opcion.lower() != 's':
            continuar = False

    print("\n=== Detalle de la cotización ===")
    print(f"Cliente: {nombre_cliente}\n")

    total = 0
    for item in cotizacion:
        producto = item['producto']
        cantidad = item['cantidad']
        precio_unitario = item['precio_unitario']
        subtotal = item['subtotal']
        
        print(f"Producto: {producto['marca']} {producto['modelo']} ({producto['tipo']})")
        print(f"ID: {producto['id']}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio Unitario: {precio_unitario}")
        print(f"Subtotal: {subtotal}\n")

        total += subtotal

    print(f"Total a pagar: {total}")

def buscar_producto_por_id(id_producto):
    for producto in productos:
        if producto['id'] == id_producto:
            return producto
    return None

def salir():
    print("Saliendo del programa...")
    print("Nombre: [VENTA DE SERVIDORES Y HARDWARE] by Felipito")
    print("Versión del programa: 1.0")
    exit(0)

def mostrar_menu():
    print("=== Venta de Servidores y Hardware ===")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir")
    print("4. Eliminar producto")
    print("5. Imprimir cotización")
    print("6. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        grabar_producto()
    elif opcion == 2:
        buscar_producto()
    elif opcion == 3:
        imprimir_reporte()
    elif opcion == 4:
        id_producto = input("Ingrese el ID del producto a eliminar: ")
        eliminar_producto(id_producto)
    elif opcion == 5:
        imprimir_cotizacion()
    elif opcion == 6:
        salir()
    else:
        print("Opción inválida. Intente nuevamente.")

while True:
    mostrar_menu()
    opcion = int(input("Ingrese una opción: "))
    ejecutar_opcion(opcion)
