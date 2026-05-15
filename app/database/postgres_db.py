import psycopg2

def conectar():
    conexion = psycopg2.connect(
        host="localhost",
        database="inventario_db",
        user="postgres",
        password="Tortilla2026!"
    )
    return conexion 
conexion = conectar()
print("Conexion exitosa")
    
def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos(
            id SERIAL PRIMARY KEY,
            codigo VARCHAR(30),
            nombre VARCHAR(100),
            precio NUMERIC(10,2),
            stock INTEGER  
            )
        """)

#   cursor.execute("""
#       ALTER TABLE productos
#       ADD CONSTRAINT codigo_unico UNIQUE (codigo);
#       """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas(
            id SERIAL PRIMARY KEY,
            id_producto INT,
            cantidad INT,
            total NUMERIC(10,2),
            fecha_hora TIMESTAMP,
            FOREIGN KEY (id_producto) REFERENCES productos(id)   
            )
        """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(50),
            apellido VARCHAR(50),
            cedula_ruc VARCHAR(20),
            celular VARCHAR(20),
            correo VARCHAR(50)
            )
        """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS roles(
            id SERIAL PRIMARY KEY,
            nombre_rol VARCHAR(30) UNIQUE
            )
        """)      

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personal(
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(50),
            apellido VARCHAR(50),
            cedula_ruc VARCHAR(20) UNIQUE,
            telefono VARCHAR(20),
            correo VARCHAR(50),
            direccion VARCHAR(150)
            )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE, 
            password_hash VARCHAR(255),
            id_personal INT REFERENCES personal(id),
            id_rol INT REFERENCES roles(id)
            )
        """)

    conexion.commit()
    conexion.close()
crear_tablas()

print("Tablas creadas!")

def agregar_producto():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO productos(
            codigo,
            nombre,
            precio,
            stock
        )
        VALUES (%s, %s, %s, %s)""")
    conexion.commit()
    conexion.close()

def listar_productos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM productos
    """)
    productos = cursor.fetchall()
    for producto in productos:
        print(producto)

    conexion.close()
listar_productos()

    
    