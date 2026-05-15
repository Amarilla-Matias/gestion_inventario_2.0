from fastapi import APIRouter
from pydantic import BaseModel
from app.database.data_base import obtener_codigo_producto_db, guardar_ventas_db, actualizar_stock_db, obtener_ventas_db
router = APIRouter(
    prefix ="/ventas",
    tags=["ventas"]
)

class Venta(BaseModel):
    codigo: str
    cantidad: int

@router.post("/ventas")
def registrar_venta(venta: Venta):
    codigo = venta.codigo
    cantidad = venta.cantidad
    producto = obtener_codigo_producto_db(codigo)
    if producto is None:
        return{"error": "Producto no existe"}
    
    stock_actual = producto[4]
    precio = producto[3]
    id_producto = producto[0]

    if cantidad <= 0:
        return{"error": "Cantidad Invalida"}
    if cantidad > stock_actual:
        return {"error": f"Stock insudiciente, solo quedan {stock_actual} unidades"}
    
    total = precio * cantidad
    guardar_ventas_db(id_producto, cantidad, total)

    nuevo_stock = stock_actual - cantidad
    actualizar_stock_db(codigo, nuevo_stock)

    return{
        "mensaje": "Ventas resgistrada",
        "producto": codigo,
        "cantidad": cantidad,
        "total": total,
        "stock_restante": nuevo_stock 
        }

@router.get("/ventas")
def listar_ventas():
    ventas = obtener_ventas_db()

    resultado = []
    for v in ventas:
        resultado.append({
            "id": v[0],
            "id_producto": v[1],
            "cantidad": v[2],
            "total": v[3],
            "fecha_hora": v[4]
        })
    return resultado