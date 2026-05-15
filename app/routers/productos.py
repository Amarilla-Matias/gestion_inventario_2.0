from fastapi import APIRouter
from app.database.database import obtener_productos_db, actualizar_stock_db, eliminar_producto_db
from app.database.data_base import conectar, agregar_producto_db, actualizar_stock_db, obtener_productos_db, obtener_codigo_producto_db, eliminar_producto_db
router = APIRouter(
    prefix ="/productos",
    tags=["productos"])


@router.get("/productos")
def listar_productos():
    productos = obtener_productos_db()

    resultado = []
    for p in productos:
        resultado.append({
            "id": p[0],
            "codigo": p[1],
            "nombre": p[2],
            "precio": p[3],
            "stock": p[4]
        })
    
    return resultado

@router.post("/productos")
def crear_productos(codigo, nombre, precio, stock):
    codigo_existente = obtener_codigo_producto_db(codigo)

    if codigo_existente:
        return {"mensaje": "Codigo de producto ya Existe!"}

    agregar_producto_db(codigo ,nombre, precio, stock)
    return {"mensaje": "Producto creado", "Descripcion": nombre}    

@router.put("/productos")
def actualizar_producto(codigo, nuevo_stock):
    actualizar_stock_db(codigo, nuevo_stock)
    return {"mensaje": f"stock del producto {codigo} actualizado"}

@router.delete("/productos")
def eliminar_producto(codigo: str):
    obtener_codigo_producto_db(codigo)
    return{"mensaje": "Producto eliminado!"}
