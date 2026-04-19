from utils import guardar_inventario
from database import agregar_producto_db, obtener_producto_db ,actualizar_stock_db, eliminar_producto_db, mostrar_productos_db, obtener_ventas_db


def agregar_producto_db_ui():
    print ("AGREGAR PRODUCTO")
     
    id_producto = input("Ingrese ID del producto: ")
    nombre = input("Ingrese el nombre: ")
    precio = float(input("Ingrese el Precio: "))
    stock = int(input ("Ingrese el Stock: "))
     

    agregar_producto_db(id_producto, nombre, precio, stock)   
    print("Producto agregado correctamente.")

def mostrar_inventario_db_ui():
    print ("=== INVENTARIO ===")
    productos = mostrar_productos_db()
    for producto in productos:
        print(f"ID: {producto[0]}|Nombre: {producto[1]}|Precio: {producto[2]}|Stock: {producto[3]}")
        suma = producto[2]*producto[3]
        print(suma)
        print("-------------------------------------------------")
    if not productos:
        print("No hay productos en el Inventario")


def actualizar_stock_db_ui():
    print ("ACTUALIZAR STOCK")
    while True:

        id_producto = input("Ingresa el ID del Producto: ")

        producto =  obtener_producto_db(id_producto)

        if producto is None:
            print ("ID no existe, intente nuevamente.")
            continue
        nombre = producto[1]
        stock_actual = producto[3]

        print(f"Producto: {nombre}")
        print(f"Stock actual: {stock_actual}")
        try:
            nuevo_stock = int(input("Ingrese el nuevo stock: "))
            actualizar_stock_db(id_producto, nuevo_stock)
            print("Stock Actualizado!!!")
        except ValueError:
            print("Solo Numeros")

        respuesta = input("¿Desea actualizar otro producto? (s/n): ")
        if respuesta != "s":
            break
    

def eliminar_producto_db_ui():
    print("ELIMINAR PRODUCTO.")
    while True:
        id_producto= input("Ingrese el ID a eliminar: ")
        producto = obtener_producto_db(id_producto)
        if producto is None:
            print ("ID no existe, intente nuevamente.")
            continue

        print (f"Producto: {producto[1]}")
        print (f"Precio: {producto[2]}")
        print (f"Stock: {producto[3]}")
        
        respuesta = input("Desea eliminar este producto? (s/n):  ")
        if respuesta == "s":
            eliminar_producto_db(id_producto)
            print("Producto Eliminado correctamente!")
        else:
            print("Eliminacion Cancelada!")
        respuesta = input("¿Desea eliminar otro producto? (s/n): ")
        if respuesta != "s":
            break
      

def buscar_producto_db_ui():
    print("Buscar Producto..")
    while True:
        id_producto = input("Ingrese el ID del Producto: ")
        producto = obtener_producto_db(id_producto)
        if producto is None:
            print("ID no existe, intente nuevamente.")
            continue
    
        print (f"ID: {producto[0]}")
        print (f"Producto: {producto[1]}")
        print (f"Precio: {producto[2]}")
        print (f"Stock: {producto[3]}")
        
        respuesta = input("¿Desea buacar otro producto? (s/n): ")
        if respuesta != "s":
            break

def total_inventario_db_ui():
    total = 0
    productos = mostrar_productos_db()
    for producto in productos:  
        subtotal= producto[2] * producto[3]
        print(f"{producto[1]}:{subtotal}")
        total += subtotal
    print("--------------------")
    print(f"Total Inventario:{total}")

def mostrar_historial_db_ui():
    print("=== HISTORIAL DE VENTAS ===")
    ventas = obtener_ventas_db()
    if not ventas:
        print("No hay ventas registradas.")
        return
    for venta in ventas:
        print (f"ID: {venta[0]}")
        print (f"ID_PRODUCTO: {venta[1]})")
        print(f"Producto: {venta[2]}")
        print(f"Cantidad: {venta[3]}")
        print(f"Total: {venta[4]}")
        print("--------------------")
    