from fastapi import APIRouter
from pydantic import BaseModel
from app.database.database import agregar_clientes_db, listar_clientes_db, actualizar_cliente_db

router = APIRouter(
    prefix="/clientes",
    tags = ["clientes"]
)

class ClienteUpdate(BaseModel):
    nombre: str
    apellido: str
    cedula_ruc: str
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
    id_cliente = agregar_clientes_db(nombre, apellido, cedula_ruc, celular, correo)
    return {"mensaje": f"Cliente {nombre} creado"}

@router.put("/{id}")
def actualiza_cliente(id: int, cliente: ClienteUpdate):
    actualizar_cliente_db(
        id, 
        cliente.nombre, 
        cliente.apellido, 
        cliente.cedula_ruc, 
        cliente.celular, 
        cliente.correo)
    return {"mensaje": f"Datos del cliente {cliente.nombre} actualizado"}