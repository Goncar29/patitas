from datos.base_de_datos import BaseDeDatos


def crear_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion):
    crear_mascota_sql = f"""
    INSERT INTO MASCOTAS(NOMBRE, ESPECIE, SEXO, COLOR, EDAD, TAMANO, OREJA, PELAJE, MANCHA, OTRAINFORMACION, LUGAR, DIA, HORA, CELULAR, MASINFORMACION)
    VALUES ('{nombre}', '{especie}', '{sexo}', '{color}', '{edad}', '{tamano}','{oreja}', '{pelaje}', '{mancha}', '{otraInformacion}', '{lugar}', '{dia}','{hora}', '{celular}', '{masInformacion}')
    """


    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_mascota_sql)


def editar_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion):
    editar_mascota_sql = f"""
    INSERT INTO MASCOTAS(NOMBRE, ESPECIE, SEXO, COLOR, EDAD, TAMANO, OREJA, PELAJE, MANCHA, OTRAINFORMACION, LUGAR, DIA, HORA, CELULAR, MASINFORMACION)
    VALUES ('{nombre}', '{especie}', '{sexo}', '{color}', '{edad}', '{tamano}','{oreja}', '{pelaje}', '{mancha}', '{otraInformacion}', '{lugar}', '{dia}','{hora}', '{celular}', '{masInformacion}')
    """


    bd = BaseDeDatos()
    bd.ejecutar_sql(editar_mascota_sql)


def listar_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion):
    listar_mascota_sql = f"""
    INSERT INTO MASCOTAS(NOMBRE, ESPECIE, SEXO, COLOR, EDAD, TAMANO, OREJA, PELAJE, MANCHA, OTRAINFORMACION, LUGAR, DIA, HORA, CELULAR, MASINFORMACION)
    VALUES ('{nombre}', '{especie}', '{sexo}', '{color}', '{edad}', '{tamano}','{oreja}', '{pelaje}', '{mancha}', '{otraInformacion}', '{lugar}', '{dia}','{hora}', '{celular}', '{masInformacion}')
    """


    bd = BaseDeDatos()
    bd.ejecutar_sql(listar_mascota_sql)


def eliminar_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion):
    eliminar_mascota_sql = f"""
    INSERT INTO MASCOTAS(NOMBRE, ESPECIE, SEXO, COLOR, EDAD, TAMANO, OREJA, PELAJE, MANCHA, OTRAINFORMACION, LUGAR, DIA, HORA, CELULAR, MASINFORMACION)
    VALUES ('{nombre}', '{especie}', '{sexo}', '{color}', '{edad}', '{tamano}','{oreja}', '{pelaje}', '{mancha}', '{otraInformacion}', '{lugar}', '{dia}','{hora}', '{celular}', '{masInformacion}')
    """


    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_mascota_sql)