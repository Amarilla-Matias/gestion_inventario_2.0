import psycopg2
from datetime import datetime
def conectar():
    conexion = psycopg2.connect(
        host="localhost",
        database="inventario_db",
        user="postgres",
        password="Tortilla2026!"
    )
    return conexion

def agregar_producto_db(codigo, nombre, precio, stock):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO productos (codigo, nombre, precio, stock)
    VALUES (%s, %s, %s, %s)
    """, (codigo, nombre, precio, stock))

    conexion.commit()
    conexion.close()

def obtener_productos_db():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    conexion.close()
    return productos

def obtener_codigo_producto_db(codigo):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE codigo = %s", (codigo,))
    producto = cursor.fetchone()
    conexion.close()
    return producto

def actualizar_stock_db(codigo, nuevo_stock):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE productos SET codigo= %s, stock= %s""",
        (codigo, nuevo_stock,)
    )

    conexion.commit()
    conexion.close()

def eliminar_producto_db(codigo):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM productos WHERE codigo = %s", (codigo,))
    filas_afectadas = cursor.rowcount

    conexion.commit()
    conexion.close()
    return filas_afectadas

#-------------------------------- VENTAS -------------------------------
def guardar_ventas_db(id_producto, cantidad, total):
    conexion = conectar()
    cursor = conexion.cursor()

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO ventas (id_producto, cantidad, total, fecha_hora)
    VALUES  (%s, %s, %s, %s)
    """,(id_producto, cantidad, total, fecha_hora))

    conexion.commit()
    conexion.close()

def obtener_ventas_db():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM ventas")
    ventas = cursor.fetchall()

    conexion.close()
    return ventas
#---------------------------------- CLIENTES -----------------------------
def agregar_clientes_db(nombre, apellido, cedula_ruc, celular, correo):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO clientes(nombre, apellido, cedula_ruc, celular, correo) 
    VALUES(%s, %s, %s, %s, %s)
    """, (nombre, apellido, cedula_ruc, celular, correo))

    conexion.commit()
    conexion.close()

def listar_clientes_db():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    conexion.close()
    return clientes

def actualizar_cliente_db( nombre, apellido, cedula_ruc, celular, correo):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE clientes
        SET nombre = %s, apellido=%s,  celular=%s, correo = %s 
        WHERE cedula_ruc = %s
        """,
        (nombre, apellido, celular, correo, cedula_ruc)
    )

    conexion.commit()
    conexion.close()

#-----------------------PERSONAL------------------------------

def agregar_personal_db(nombre, apellido, cedula_ruc, telefono, correo, direccion):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO personal(nombre, apellido, cedula_ruc, telefono, correo, direccion)
        VALUES(%s, %s, %s, %s, %s, %s)
        """,(nombre, apellido, cedula_ruc, telefono, correo, direccion))

    conexion.commit()
    conexion.close()

def listar_personal_db():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""SELECT * FROM personal""")
    personal = cursor.fetchall()

    conexion.close()
    return personal

def actualizar_personal_db(nombre, apellido, cedula_ruc, telefono, correo, direccion):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE personal 
        SET nombre = %s, apellido = %s, telefono = %s, correo = %s, direccion = %s
        WHERE cedula_ruc = %s
        """, (nombre, apellido, telefono, correo, direccion, cedula_ruc))
    
    conexion.commit()
    conexion.close()

def eliminar_personal_db(cedula_ruc):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM productos WHERE cedula_ruc = %s", (cedula_ruc,))
    filas_afectadas = cursor.rowcount

    conexion.commit()
    conexion.close()
    return filas_afectadas

#-----------------------ROLES------------------------------

def agregar_rol_db(nombre_rol):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO roles(nombre_rol)
        VALUES(%s)
        """,(nombre_rol,))

    conexion.commit()
    conexion.close()

def listar_roles_db():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""SELECT * FROM roles""")
    personal = cursor.fetchall()

    conexion.close()
    return personal

def actualizar_rol_db(nombre_rol, id):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""UPDATE roles SET nombre_rol = %s WHERE id = %s """, (nombre_rol, id))
    
    conexion.commit()
    conexion.close()

def eliminar_rol_db(id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM roles WHERE id = %s", (id,))
    filas_afectadas = cursor.rowcount

    conexion.commit()
    conexion.close()
    return filas_afectadas