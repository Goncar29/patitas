import sqlite3


sql_tabla_roles = '''
CREATE TABLE ROLES (
IDROL INTEGER PRIMARY KEY AUTOINCREMENT,
TIPOROL TEXT
)
'''


sql_tabla_usuarios = '''
CREATE TABLE USUARIOS (
IDROLUSUARIOS INTEGER PRIMARY KEY AUTOINCREMENT,
EMAIL VARCHAR(50) NOT NULL UNIQUE,
CLAVE VARCHAR(50) NOT NULL UNIQUE,
INGRESOCONFACEBOOK, 
INGRESOCONTWITTER
)
'''


sql_tabla_mascotas = '''
CREATE TABLE MASCOTAS (
IDROLMASCOTAS INTEGER PRIMARY KEY AUTOINCREMENT,
NOMBRE TEXT,
ESPECIE TEXT,
SEXO TEXT,
COLOR TEXT,
EDAD INTEGER,
TAMANO TEXT,
OREJA TEXT,
PELAJE TEXT,
MANCHA VARCHAR(50),
OTRAINFORMACION VARCHAR(255),
LUGAR TEXT,
DIA VARCHAR(50),
HORA VARCHAR(50),
CELULAR INTEGER,
MASINFORMACION VARCHAR(255)
)
'''


sql_tabla_fotos = '''
CREATE TABLE FOTOS (
IDROLMASCOTAS INTEGER PRIMARY KEY AUTOINCREMENT,
NOMBREDELARCHIVO VARCHAR(50),
DESCRIPCION VARCHAR(255),
ARCHIVO BLOB
)
'''


sql_tabla_roles_usuarios = '''
CREATE TABLE ROLES_USUARIOS (
IDROL INTEGER PRIMARY KEY AUTOINCREMENT,
IDROLUSUARIOS INTEGER PRIMARY KEY AUTOINCREMENT
)
'''


sql_tabla_usuarios_mascotas = '''
CREATE TABLE USUARIOS_MASCOTAS (
IDROLUSUARIOS INTEGER PRIMARY KEY AUTOINCREMENT,
IDROLMASCOTAS INTEGER PRIMARY KEY AUTOINCREMENT
)
'''


sql_tabla_mascotas_fotos = '''
CREATE TABLE MASCOTAS_FOTOS (
IDROLMASCOTAS INTEGER PRIMARY KEY AUTOINCREMENT,
IDROLMASCOTAS INTEGER PRIMARY KEY AUTOINCREMENT
)
'''


if __name__ == '__main__':
    try:
        print('Creando Base de Datos...')
        conexion = sqlite3.connect('/home/carlos/EDX/proyecto/patitas.db')

        print('Creando tablas...')
        conexion.execute(sql_tabla_roles)
        conexion.execute(sql_tabla_usuarios)
        conexion.execute(sql_tabla_mascotas)
        conexion.execute(sql_tabla_fotos)
        conexion.execute(sql_tabla_roles_usuarios)
        conexion.execute(sql_tabla_usuarios_mascotas)
        conexion.execute(sql_tabla_mascotas_fotos)

        conexion.close()
        print('Creacion Finalizada.')
    except Exception as e:
        print(f'Error creando base de datos {e}', e)