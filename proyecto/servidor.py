from flask import Flask, request
from servicios.autenticacion import autenticacion

app = Flask(__name__)

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    if 'email' not in datos_usuario:
        return 'El email de usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'clave es requerida', 412
    autenticacion.crear_usuario(datos_usuario['email'], datos_usuario['clave'])
    return 'OK', 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)


@app.route('/usuarios', methods=['DELETE'])
def eliminar_usuario():
    datos_usuario = request.get_json()
    autenticacion.eliminar_usuario(datos_usuario['email'], datos_usuario['clave'])
    return 'OK', 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)


@app.route('/login', methods=['POST'])
def crear_login():
    datos_login = request.get_json()
    if 'email' not in datos_login:
        return 'El email es requerido', 412
    if 'clave' not in datos_login:
        return 'La clave es requerida', 412
    autenticacion.crear_login(datos_login['email'], datos_login['clave'])
    return 'OK', 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)


@app.route('/mascotas', methods=['POST'])
def crear_mascota():
    datos_mascota = request.get_json()
    if 'nombre' not in datos_mascota:
        return 'El email es requerido', 412
    if 'celular' not in datos_mascota:
        return 'La clave es requerida', 412
    autenticacion.crear_mascota(datos_mascota['nombre'], datos_mascota['especie'], datos_mascota['sexo'],
                                datos_mascota['color'], datos_mascota['edad'], datos_mascota['tamano'],
                                datos_mascota['oreja'], datos_mascota['pelaje'], datos_mascota['mancha'],
                                datos_mascota['otraInformacion'], datos_mascota['lugar'], datos_mascota['dia'],
                                datos_mascota['hora'], datos_mascota['celular'], datos_mascota['masInformacion'])
    return 'OK', 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)


@app.route('/mascotas', methods=['PUT'])
def editar_mascota():
    datos_mascota = request.get_json()
    autenticacion.editar_mascota(datos_mascota['nombre'], datos_mascota['especie'], datos_mascota['sexo'],
                                 datos_mascota['color'], datos_mascota['edad'], datos_mascota['tamano'],
                                 datos_mascota['oreja'], datos_mascota['pelaje'], datos_mascota['mancha'],
                                 datos_mascota['otraInformacion'], datos_mascota['lugar'], datos_mascota['dia'],
                                 datos_mascota['hora'], datos_mascota['celular'], datos_mascota['masInformacion'])
    return 'OK', 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)


@app.route('/mascotas', methods=['GET'])
def listar_mascota():
    datos_mascota = request.get_json()
    autenticacion.listar_mascota(datos_mascota['nombre'], datos_mascota['especie'], datos_mascota['sexo'],
                                 datos_mascota['color'], datos_mascota['edad'], datos_mascota['tamano'],
                                 datos_mascota['oreja'], datos_mascota['pelaje'], datos_mascota['mancha'],
                                 datos_mascota['otraInformacion'], datos_mascota['lugar'], datos_mascota['dia'],
                                 datos_mascota['hora'], datos_mascota['celular'], datos_mascota['masInformacion'])
    return 'OK', 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)