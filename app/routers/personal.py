from fastapi import APIRouter
from pydantic import BaseModel
from app.database.data_base import agregar_personal_db, listar_personal_db, actualizar_personal_db, eliminar_personal_db


router = APIRouter(
    prefix= "/personal",
    tags= ["Personal"]
)

class personoslUpdate(BaseModel):
    nombre: str
    apellido: str
    telefono: str
    correo: str
    direccion: str


@router.post("/personal")
def agregar_personal(nombre, apellido, cedula_ruc, telefono, correo, direccion):
    agregar_personal_db(nombre, apellido, cedula_ruc, telefono, correo, direccion)
    return {"mensaje": "Datos cargados exitosamente"}

@router.get("/")
def listar_personal():
    personal = listar_personal_db()

    resultado = []
    for p in personal:
        resultado.append({
            "id": p[0],
            "Nombre": p[1],
            "Apellido": p[2],
            "Cedula o Ruc": p[3],
            "Telefono": p[4],
            "Correo": p[5],
            "Direccion": p[6],
        })
    return resultado

@router.put("/personal")
def actualizar_personal(cedula_ruc: str, personal: personoslUpdate):
    actualizar_personal_db(
        personal.nombre,
        personal.apellido,
        cedula_ruc,
        personal.telefono,
        personal.correo,
        personal.direccion
    )
    return{"mensaje":"Datos actualizados Exitosamentes"}

@router.delete("/delete/cedula_ruc")
def eliminar_personal(cedula_ruc):
    eliminar_personal_db(cedula_ruc)
    return{"mensaje":"Datos eliminados Exitosamente!"}