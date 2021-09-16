from datos.base_de_datos import BaseDeDatos


def crear_foto(nombreDelArchivo, descripcion, tipoDeArchivo):
    crear_foto_sql = f"""
    INSERT INTO FOTOS(NOMBREDELARCHIVO, DESCRIPCION, TIPODEARCHIVO)
    VALUES ('{nombreDelArchivo}', '{descripcion}', '{tipoDeArchivo}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_foto_sql)


def editar_foto(nombreDelArchivo, descripcion, tipoDeArchivo):
    editar_foto_sql = f"""
    INSERT INTO FOTOS(NOMBREDELARCHIVO, DESCRIPCION, TIPODEARCHIVO)
    VALUES ('{nombreDelArchivo}', '{descripcion}', '{tipoDeArchivo}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(editar_foto_sql)


def listar_foto(nombreDelArchivo, descripcion, tipoDeArchivo):
    listar_foto_sql = f"""
    INSERT INTO FOTOS(NOMBREDELARCHIVO, DESCRIPCION, TIPODEARCHIVO)
    VALUES ('{nombreDelArchivo}', '{descripcion}', '{tipoDeArchivo}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(listar_foto_sql)


def eliminar_foto(nombreDelArchivo, descripcion, tipoDeArchivo):
    eliminar_foto_sql = f"""
    INSERT INTO FOTOS(NOMBREDELARCHIVO, DESCRIPCION, TIPODEARCHIVO)
    VALUES ('{nombreDelArchivo}', '{descripcion}', '{tipoDeArchivo}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_foto_sql)