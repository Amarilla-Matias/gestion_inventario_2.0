from fastapi import FastAPI
from app.routers import personal, clientes, productos, ventas, usuarios, roles
from app.database.database import crear_tabla
from app.routers import usuarios

crear_tabla()

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(roles.router)
app.include_router(personal.router)
app.include_router(clientes.router)
app.include_router(productos.router)
app.include_router(ventas.router)