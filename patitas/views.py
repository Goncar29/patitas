from flask import Flask, request, jsonify, redirect, url_for, Response, render_template, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from sqlalchemy.inspection import inspect
from sqlalchemy import select, update, delete
import json
import datetime
from werkzeug.utils import secure_filename
from patitas import app
from .models import Usuario, Rol, Mascota, ImagenMascota

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


#####################################################################################################################
## Vistas de LOGIN y SESSION
#####################################################################################################################
@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.query.get(int(usuario_id))


@app.route('/login', methods=['POST'])
def login():
    try:
        username_parm = request.form['username']
        password_parm = request.form['password']
        usuario = Usuario.query.filter_by(username=username_parm).first()
        if usuario and usuario.password == password_parm:
            login_user(usuario)
            return redirect('/me')
        else:
            return render_template('login.html', error='Nombre de usuario o contraseña incorrecta.')
    except:
        return render_template('login.html', error='Algo ha salido mal.')


@app.route('/login', methods=['GET'])
def mostrar_login():
    if current_user.is_authenticated:
        return redirect('/me')
    else:
        return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Ahora estás deslogueado :('


#####################################################################################################################
## Vistas de NAVEGACION
#####################################################################################################################

@app.route('/')
def get_web():
    return redirect(url_for('inicio'))


@app.route('/home')
@login_required
def home():
    return redirect('/inicio')


@app.route('/inicio')
def inicio():
    return render_template('inicio.html', user_logueado=current_user.is_authenticated)


@app.route('/conocenos')
def conocenos():
    return render_template('conocenos.html', user_logueado=current_user.is_authenticated)


@app.route('/encuentra', methods=['GET'])
def encuentra():
    mascotas = Mascota.query
    mascotas = mascotas.filter_by(estado_mascota='E')
    form = request.args
    if 'especie' in form:
        mascotas = mascotas.filter_by(especie=form['especie'])
    if 'sexo' in form:
        mascotas = mascotas.filter_by(especie=form['sexo'])
    if 'tamanio' in form:
        mascotas = mascotas.filter_by(especie=form['tamanio'])
    if 'departamento' in form:
        mascotas = mascotas.filter_by(especie=form['departamento'])

    cantidad_mascotas = mascotas.count()
    mascotas = mascotas.all()
    return render_template('encuentra.html', user_logueado=current_user.is_authenticated, mascotas=mascotas, cantidad_mascotas=cantidad_mascotas)



@app.route('/adopta', methods=['GET'])
def adopta():
    mascotas = Mascota.query
    mascotas = mascotas.filter_by(estado_mascota='A')
    form = request.args
    if 'especie' in form:
        mascotas = mascotas.filter_by(especie=form['especie'])
    if 'sexo' in form:
        mascotas = mascotas.filter_by(especie=form['sexo'])
    if 'tamanio' in form:
        mascotas = mascotas.filter_by(especie=form['tamanio'])
    if 'departamento' in form:
        mascotas = mascotas.filter_by(especie=form['departamento'])

    cantidad_mascotas = mascotas.count()
    mascotas = mascotas.all()
    return render_template('adopta.html', user_logueado=current_user.is_authenticated, mascotas=mascotas, cantidad_mascotas=cantidad_mascotas)


@app.route('/registrar')
def registro():
    return render_template('registrar.html', user_logueado=current_user.is_authenticated)


@app.route('/registro', methods=['GET'])
def formulario():
    if current_user.is_authenticated:
        return redirect('/me')
    else:
        return render_template('registro.html', user_logueado=current_user.is_authenticated)


@app.route('/notfound')
def notfound():
    return render_template('notfound.html', user_logueado=current_user.is_authenticated)


@app.route('/upload')
def upload():
    return render_template('upload.html', user_logueado=current_user.is_authenticated)


@app.route('/web')
def web():
    return render_template('web.html', user_logueado=current_user.is_authenticated)



#####################################################################################################################
## Vistas de USUARIO
#####################################################################################################################


@app.route('/me')
@login_required
def ver_editar_usuario():
    if request.method=="GET":
        if current_user.is_authenticated:
                return render_template('modificar.html', nombre=current_user.nombre,apellido=current_user.apellido,email=current_user.email,username=current_user.username,password=current_user.password, telefono=current_user.telefono, celular=current_user.celular, user_logueado=True)
        else:
            return redirect('/inicio')
    else:
        if current_user.is_authenticated:
            form = request.form
            error = False
            # Faltan controles en los campos
            if not(error):
                if Usuario.query.filter_by(username=form['username']).first() and current_user.username != form['username']:
                    errores[username] = 'Ya existe usuario con ese nombre de usuario.'
                    error = True

                if Usuario.query.filter_by(email=form['email']).first() and current_user.email != form['email']:
                    errores[email] = 'Ya existe usuario con ese email.'
                    error = True

            if error:
                return render_template('modificar.html', errores = errores, user_logueado=True)
            else:
                usuario = Usuario.query.filter_by(username=current_user.username).first()
                usuario.username=form['username']
                usuario.email=form['email']
                usuario.password=form['password']
                usuario.nombre=form['nombre']
                usuario.apellido=form['apellido']
                usuario.celular=form['celular']
                usuario.telefono=form['telefono']
                db.session.merge(usuario)
                db.session.commit()
                return render_template('modificar.html', error= 'Se han confirmado los cambios', nombre=current_user.nombre,apellido=current_user.apellido,email=current_user.email,username=current_user.username,password=current_user.password, telefono=current_user.telefono, celular=current_user.celular, user_logueado=True)
        else:
            return redirect('/inicio')

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    form = request.form
    error = False
    # Faltan controles en los campos
    if not(error):
        if Usuario.query.filter_by(username=form['username']).first():
            error_username = 'Ya existe usuario con ese nombre de usuario.'
            error = True

        if Usuario.query.filter_by(email=form['email']).first():
            error_email = 'Ya existe usuario con ese email.'
            error = True

    if error:
        return render_template('registro.html', error_username = error_username, error_email=error_email)
    else:
        usuario = Usuario(username=form['username'], email=form['email'], password=form['password'], 
                          nombre=form['nombre'], apellido=form['apellido'],
                          celular=form['celular'], telefono=form['telefono'], fecha_registro=datetime.datetime.now(), confirmado=True, fecha_confirmado= datetime.datetime.now())
        
        db.session.add(usuario)
        db.session.commit()

        return render_template('registro_exitoso.html')



@app.route('/usuarios', methods=['GET'])
def ver_usuarios():
    usuarios = Usuario.query.all()
    if not usuarios:
        return "No existen usuarios", 200
    return jsonify([i.serialize for i in usuarios]), 200


@app.route('/verusuarios', methods=['GET'])
def ver_usuarios_template():
    usuarios = Usuario.query.all()
    return render_template('listarusuarios.html', usuarios=usuarios)



@app.route('/usuarios/<string:username>', methods=['GET'])
def ver_usuario(username):
    usuario = Usuario.query.filter_by(username=username).first()
    if not usuario:
        return "No existe el usuario", 404
    return jsonify([usuario.serialize]), 200



@app.route('/usuarios/<string:username>', methods=['DELETE'])
def eliminar_usuario_via_username(username):
    if current_user.is_authenticated:
        sql1 = delete(Usuario).where(Usuario.id == current_user.id)
        db.session.execute(sql1)
        db.session.commit()
        return 'Se ha eliminado el usuario', 200
    else:
        return render_template('notfound.html')


@app.route('/borrarusuario', methods=['DELETE','GET'])
def eliminar_usuario():
    if current_user.is_authenticated:
        sql1 = delete(Usuario).where(Usuario.id == current_user.id)
        db.session.execute(sql1)
        db.session.commit()
        return 'Se ha eliminado el usuario', 200
    else:
        return render_template('notfound.html')

#####################################################################################################################
## Vistas de MASCOTA
#####################################################################################################################

@app.route('/mascotas', methods=['POST'])
@login_required
def crear_mascota():
    try:
        datos_mascota = request.form
        mascota = Mascota(
            nombre=datos_mascota['nombre'],
            especie=datos_mascota['especie'],
            sexo=datos_mascota['sexo'],
            color=datos_mascota['color'],
            edad=datos_mascota['edad'],
            tamanio=datos_mascota['tamanio'],
            oreja=datos_mascota['oreja'],
            pelaje=datos_mascota['pelaje'],
            otra_informacion_mascota=datos_mascota['otra_informacion_mascota'],
            departamento=datos_mascota['departamento'],
            localidad=datos_mascota['localidad'],
            calle=datos_mascota['calle'],
            mas_informacion_encuentro=datos_mascota['mas_informacion_encuentro'],
            nombre_contacto=datos_mascota['nombre_contacto'],
            celular_contacto=datos_mascota['celular_contacto'],
            telefono_contacto=datos_mascota['telefono_contacto'],
            estado_mascota=datos_mascota['estado_mascota'],
            estado_publicacion='P',
            usuario_publicacion=current_user.id
        )
        db.session.add(mascota)
        db.session.commit()

        # Ahora subo imagen (hasta 2?)
        try:
            imagen = request.files['imagen']
            filename = secure_filename(imagen.filename)
            mimetype = imagen.mimetype
            print(mascota.id)
            img = ImagenMascota(mascota_foto= mascota.id, img=imagen.read(), mimetype=mimetype, nombre=filename)
            db.session.add(img)
            db.session.commit()
        except:
            pass

        try:
            imagen = request.files['imagen2']
            filename = secure_filename(imagen.filename)
            mimetype = imagen.mimetype

            img = ImagenMascota(mascota_foto= mascota.id, img=imagen.read(), mimetype=mimetype, nombre=filename)
            db.session.add(img)
            db.session.commit()
        except:
            pass

        return 'Mascota ingresada correctamente.', 200
    except:
        return render_template('registrar.html', error="Ha ocurrido un error, revise los datos.")


@app.route('/mascotas', methods=['GET'])
def listar_mascota():
    lista_mascotas = Mascota.query.all()
    return jsonify([i.serialize for i in lista_mascotas]), 200


@app.route('/upload', methods=['POST'])
def subir_imagen():
    try:
        imagen = request.files['imagen']

        if not imagen:
            return 'No ha subido ninguna imagen', 400
        filename = secure_filename(imagen.filename)
        mimetype = imagen.mimetype

        img = ImagenMascota(img=imagen.read(), mimetype=mimetype, nombre=filename)
        db.session.add(img)
        db.session.commit()

        return 'La imagen ha sido subida!'
    except:
        return 'ERROR', 400


@app.route('/imagen/<int:id>', methods=['GET'])
def mostrar_imagen(id):
    img = ImagenMascota.query.filter_by(id=id).first()
    if not img:
        return "No existe la imagen", 404

    return Response(img.img, mimetype=img.mimetype)


@app.route('/imagen/mascota/<int:id>', methods=['GET'])
def mostrar_imagen_mascota(id):
    img = ImagenMascota.query.filter_by(mascota_foto=id).first()
    if not img:
        img = './templates/no_imagen.png'
        return send_file(img, mimetype='image/gif')
    else:
        return Response(img.img, mimetype=img.mimetype)


#####################################################################################################################
## Manejo de errores
#####################################################################################################################
##@app.errorhandler(500)
##def internal_server_error(e):
##    content = "Internal Server Error: " + str(e) + "<br>"
##    content += error_info(e)
##    return content, 500


##@app.errorhandler(400)
##def bad_request(e):
##    content = "Bad Request: " + str(e) + "<br>"
##    content += error_info(e)
##    return content, 400

##@app.errorhandler(404)
##def not_found(e):
##   content = "Not found" + str(e) + "<br>"
##    content += error_info(e)
##    return content, 404


##@app.errorhandler(401)
##def unauthorized(e):
##    content = "Not autorized" + e + "<br>"
##    content += error_info(e)
##   return content, 401

##def error_info(e):
##	return e


#####################################################################################################################
## Servicio
#####################################################################################################################

if __name__ == '__main__':
    app.run()
