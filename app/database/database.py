import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BD_PATH = os.path.join(BASE_DIR, "inventario.db")

print(BD_PATH)

def conectar():
    conexion = sqlite3.connect(BD_PATH)
    conexion.execute("PRAGMA foreing_keys = ON")
    return conexion

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id TEXT PRIMARY KEY,
        nombre TEXT,
        precio REAL,
        stock INTEGER
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_producto TEXT,
        nombre TEXT,
        cantidad INTEGER,
        total REAL,
        FOREIGN KEY (id_producto) REFERENCES productos(id)          
    )
    """)
    conexion.commit()
    conexion.close()

def migrar_tabla_ventas():
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("ALTER TABLE ventas ADD COLUMN fecha_hora TEXT")
        conexion.commit()
    except Exception as e:
        print("La columna ya existe o hubo un error:", e)
    finally:
        conexion.close()

def agregar_producto_db(id, nombre, precio, stock):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO productos (id, nombre, precio, stock)
    VALUES (?, ?, ?, ?)
    """, (id, nombre, precio, stock))

    conexion.commit()
    conexion.close()

def mostrar_productos_db():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    return productos

    conexion.close()

def obtener_productos_db():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    conexion.close()
    return productos

def obtener_producto_db(id_producto):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    conn.close()
    return producto


def actualizar_stock_db(id_producto, nuevo_stock):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE productos SET stock = ? WHERE id = ?",
        (nuevo_stock, id_producto)
    )

    conexion.commit()
    conexion.close()

def eliminar_producto_db(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))

    conexion.commit()
    conexion.close()

def guardar_ventas_db(id_producto, nombre, cantidad, total):
    conexion = conectar()
    cursor = conexion.cursor()

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO ventas (id_producto, nombre, cantidad, total, fecha_hora)
    VALUES  (?, ?, ?, ?, ?)
    """,(id_producto, nombre, cantidad, total, fecha_hora))

    conexion.commit()
    conexion.close()

def obtener_ventas_db():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM ventas")
    ventas = cursor.fetchall()

    conexion.close()
    return ventas



