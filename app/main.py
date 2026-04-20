from fastapi import FastAPI
from app.routers import clientes, usuarios
from app.database.database import crear_tabla

crear_tabla()

app = FastAPI()

app.include_router(usuarios.router)