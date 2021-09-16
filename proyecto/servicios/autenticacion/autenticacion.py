from datos.modelos import usuario as modelo_usuario
from datos.modelos import mascota as modelo_mascota
from datos.modelos import foto as modelo_foto


def crear_usuario(email, clave):
    modelo_usuario.crear_usuario(email, clave)

def editar_usuario(email, clave):
    modelo_usuario.editar_usuario(email, clave)

def listar_usuario(email, clave):
    modelo_usuario.listar_usuario(email, clave)

def eliminar_usuario(email, clave):
    modelo_usuario.eliminar_usuario(email, clave)


def crear_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion):
    modelo_mascota.crear_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion)

def editar_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion):
    modelo_mascota.editar_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion)

def listar_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion):
    modelo_mascota.listar_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion)

def eliminar_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion):
    modelo_mascota.eliminar_mascota(nombre, especie, sexo, color, edad, tamano, oreja, pelaje, mancha, otraInformacion, lugar, dia, hora, celular, masInformacion)


def crear_foto(nombreDelArchivo, descripcion, tipoDeArchivo):
    modelo_foto.crear_foto(nombreDelArchivo, descripcion, tipoDeArchivo)

def editar_foto(nombreDelArchivo, descripcion, tipoDeArchivo):
    modelo_foto.editar_foto(nombreDelArchivo, descripcion, tipoDeArchivo)

def listar_foto(nombreDelArchivo, descripcion, tipoDeArchivo):
    modelo_foto.listar_foto(nombreDelArchivo, descripcion, tipoDeArchivo)

def eliminar_foto(nombreDelArchivo, descripcion, tipoDeArchivo):
    modelo_foto.eliminar_foto(nombreDelArchivo, descripcion, tipoDeArchivo)

