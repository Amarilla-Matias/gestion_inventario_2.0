from fastapi import APIRouter
from pydantic import BaseModel
from app.database.data_base import actualizar_cliente_db, listar_clientes_db, agregar_clientes_db
router = APIRouter(
    prefix="/clientes",
    tags = ["clientes"]
)

class ClienteUpdate(BaseModel):
    nombre: str
    apellido: str
    celular: str
    correo : str


@router.get("/")
def listar_clientes():
    clientes = listar_clientes_db()

    resultado = []
    for c in clientes:
        resultado.append({
            "id": c[0],
            "nombre": c[1],
            "apellido": c[2],
            "cedula_ruc": c[3],
            "celular": c[4],
            "correo" : c[5]
        })
    return resultado

@router.post("/")
def agregar_cliente(nombre, apellido, cedula_ruc, celular, correo):
    agregar_clientes_db(nombre, apellido, cedula_ruc, celular, correo)
    return {"mensaje": f"Cliente {nombre} creado"}

@router.put("/")
def actualiza_cliente(cedula_ruc: str, cliente: ClienteUpdate):
    actualizar_cliente_db( 
        cliente.nombre, 
        cliente.apellido, 
        cedula_ruc, 
        cliente.celular, 
        cliente.correo)
    return {"mensaje": f"Datos del cliente {cliente.nombre} actualizado"}