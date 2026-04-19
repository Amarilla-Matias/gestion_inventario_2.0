import json

def guardar_inventario(inventario):
    with open("inventario.json", "w") as archivo:
        json.dump(inventario, archivo)

def cargar_inventario():
    try:
        with open("inventario.json","r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return{}