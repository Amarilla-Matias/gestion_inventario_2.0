from fastapi import APIRouter
from pydantic import BaseModel
from app.database.data_base import agregar_rol_db, listar_roles_db, actualizar_rol_db, eliminar_rol_db


router = APIRouter(
    prefix= "/rol",
    tags= ["rol"]
)

class rolUpdate(BaseModel):
    nombre_rol: str


@router.post("/personal")
def agregar_rol(nombre_rol):
    agregar_rol_db(nombre_rol)
    return {"mensaje": "Datos cargados exitosamente"}

@router.get("/")
def listar_roles():
    rol = listar_roles_db()

    resultado = []
    for r in rol:
        resultado.append({
            "id": r[0],
            "Nombre": r[1],
        })
    return resultado

@router.put("/{id}")
def actualizar_roles(id:int, rol:rolUpdate):
    actualizar_rol_db(
        rol.nombre_rol,
        id
    )
    return{"mensaje":"Datos actualizados Exitosamentes"}

@router.delete("/{id}")
def eliminar_rol(id):
    eliminar_rol_db(id)
    return{"mensaje":"Datos eliminados Exitosamente!"}