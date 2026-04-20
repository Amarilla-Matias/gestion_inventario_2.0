from fastapi import FastAPI
from app.database.database import obtener_productos_db, actualizar_stock_db, agregar_producto_db, eliminar_producto_db

app = FastAPI()

@app.get("/")
def inicio():
    return{"mensaje": "API todo cheto!"}

@app.get("/productos")
def listar_productos():
    productos = obtener_productos_db()

    resultado = []
    for p in productos:
        resultado.append({
            "id": p[0],
            "nombre": p[1],
            "precio": p[2],
            "stock": p[3]
        })
    
    return resultado

@app.post("/productos")
def crear_productos(id, nombre, precio, stock):
    id_producto = agregar_producto_db(id,nombre, precio, stock)
    return {"mensaje": "Producto creado", "id": id_producto}    

@app.put("/productos/{id_producto}")
def actualizar_producto(id_producto, nuevo_stock):
    actualizar_stock_db(id_producto, nuevo_stock)
    return {"mensaje": f"stock del producto {id_producto} actualizado"}

@app.delete("/productos/{id_producto}")
def eliminar_producto(id_producto):
    eliminar_producto_db(id_producto)
    return{"mensaje:" f"Producto {id_producto} eliminado"}
