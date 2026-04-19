
from database import obtener_producto_db, actualizar_stock_db, guardar_ventas_db
def vender_producto():
    print("FACTURACION-VENTAS")
    while True:
        id_producto = input("Ingrese el ID del producto: ")
        producto = obtener_producto_db(id_producto)
        if producto is None:
            print("ID no existe, intente nuevamente.")
            continue
        id_db = producto[0]
        nombre = producto[1]
        precio = producto[2]
        stock = producto[3]
        print (f"Producto:{nombre}")
        print (f"Stock Disponible:{stock} ")
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                if cantidad <= 0:
                    print("Cantidad invalida. Debe ser mayor a 0.")
                elif cantidad > stock:
                    print(f"Stock Insuficiente. Solo quedan {producto['stock']} unidades disponibles.")
                else: 
                    total = precio * cantidad
                    guardar_ventas_db(id_producto, nombre, cantidad, total)
                    nuevo_stock = stock - cantidad
                    actualizar_stock_db(id_producto, nuevo_stock)
                    venta = {
                        "id": id_db,
                        "nombre" : nombre,
                        "cantidad": cantidad,
                        "total": total, 
                    } 
                    print("Total a pagar: ", total)  
                    print(f"Stock restante: ", nuevo_stock)
                    break   
            except ValueError:
                print("Solo se permiten numeros")
        print("Desea realizar otra venta? (s/n)")
        respuesta=input("Ingrese su Respuesta: ")
        if respuesta != "s":
            break