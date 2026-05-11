from fastapi import FastAPI
from app.routers import clientes, productos, ventas, usuarios
from app.database.database import crear_tabla
from gestion_inventario.app.routers import usuarios

crear_tabla()

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(clientes.router)
app.include_router(productos.router)
app.include_router(ventas.router)