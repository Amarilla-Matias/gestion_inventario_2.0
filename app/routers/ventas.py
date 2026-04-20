from fastapi import FastAPI
from pydantic import BaseModel
from app.database.database import obtener_producto_db, actualizar_stock_db, guardar_ventas_db, obtener_ventas_db

app = FastAPI()

class Venta(BaseModel):
    id_producto : int
    cantidad: int

@app.post("/ventas")
def registrar_venta(venta: Venta):
    producto = obtener_producto_db(venta.id_producto)
    if producto is None:
        return{"error": "Producto no existe"}
    
    id_producto, nombre, precio, stock = producto

    if venta.cantidad <= 0:
        return{"error": "Cantidad Invalida"}
    if venta.cantidad > stock:
        return {"error": "Stock insudiciente. solo quedan {stock} unidades"}
    
    total = precio * venta.cantidad
    guardar_ventas_db(venta.id_producto, nombre, venta.cantidad, total)

    nuevo_stock = stock - venta.cantidad
    actualizar_stock_db(venta.id_producto, nuevo_stock)

    return{
        "mensaje": "Ventas resgistrada",
        "producto": nombre,
        "cantidad": venta.cantidad,
        "total": total,
        "stock_restante": nuevo_stock 
        }

@app.get("/ventas")
def listar_ventas():
    ventas = obtener_ventas_db()

    resultado = []
    for v in ventas:
        resultado.append({
            "id": v[0],
            "id_producto": v[1],
            "nombre": v[2],
            "cantidad": v[3],
            "total": v[4],
            "fecha_hora": v[5]
        })
    return resultado