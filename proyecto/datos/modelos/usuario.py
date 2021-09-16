from datos.base_de_datos import BaseDeDatos


def crear_usuario(email, clave):
    crear_usuario_sql = f"""
        INSERT INTO USUARIOS(EMAIL, CLAVE)
        VALUES ('{email}, {clave}')
    """


    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)


def editar_usuario(email, clave):
    editar_usuario_sql = f"""
        INSERT INTO USUARIOS(EMAIL, CLAVE)
        VALUES ('{email}, {clave}')
    """


    bd = BaseDeDatos()
    bd.ejecutar_sql(editar_usuario_sql)


def listar_usuario(email, clave):
    listar_usuario_sql = f"""
        INSERT INTO USUARIOS(EMAIL, CLAVE)
        VALUES ('{email}, {clave}')
    """


    bd = BaseDeDatos()
    bd.ejecutar_sql(listar_usuario_sql)




def eliminar_usuario(email, clave):
    eliminar_usuario_sql = f"""
        INSERT INTO USUARIOS(EMAIL, CLAVE)
        VALUES ('{email}, {clave}')
    """


    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_usuario_sql)