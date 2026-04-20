from inventario_db import agregar_producto_db_ui, mostrar_inventario_db_ui, eliminar_producto_db_ui, buscar_producto_db_ui, total_inventario_db_ui, mostrar_historial_db_ui, actualizar_stock_db_ui
from ventas import vender_producto
from utils import cargar_inventario
from database import crear_tabla, migrar_tabla_ventas

if __name__ == "__main__":
    migrar_tabla_ventas()

crear_tabla()


inventario = cargar_inventario()
historial = []
 
while True:
    print("1 - Agregar Producto")
    print("2 - Mostrar Inventario")
    print("3 - Actualizar Stock")
    print("4 - Vender Producto")
    print("5 - Eliminar Producto")
    print("6 - Buscar Producto")
    print("7 - Total Inventario")
    print("8 - Historial de Ventas")
    print("9 - Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_producto_db_ui()
    elif opcion == "2":
        mostrar_inventario_db_ui()
    elif opcion == "3":
        actualizar_stock_db_ui()
    elif opcion == "4":
        vender_producto()
    elif opcion == "5":
        eliminar_producto_db_ui()
    elif opcion == "6":
        buscar_producto_db_ui()
    elif opcion == "7":
        total_inventario_db_ui()
    elif opcion == "8":
        mostrar_historial_db_ui()
    else:
        break