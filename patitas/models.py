from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from flask_login import UserMixin
import datetime
import json
import enum
from patitas import app
from .enums import Especie, Sexo, Edad, Tamanio, Pelaje, Orejas, EstadoMascota, EstadoPublicacion


db = SQLAlchemy(app)


class Serializer(object):
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}


class Usuario(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(40), unique=True)
	email = db.Column(db.String(200), unique=True)
	password = db.Column(db.String(32))
	celular = db.Column(db.String(20))
	telefono = db.Column(db.String(20))
	fecha_registro = db.Column(db.DateTime, nullable=True)
	confirmado = db.Column(db.Boolean, nullable=False, default=False)
	fecha_confirmado = db.Column(db.DateTime, nullable=True)
	rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'))
	publicaciones = db.relationship('Mascota', backref='mascota', lazy='dynamic')
	@property
	def serialize(self):
		rol = Rol.query.filter_by(id=self.rol_id).first()
		return {
				'username': self.username,
				'rol': rol.tipo_rol
			}


class Rol(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tipo_rol = db.Column(db.String(40), unique=True)
	usuariorol = db.relationship('Usuario', backref='rol', lazy='dynamic')



class Mascota(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.Unicode(40))
	especie = db.Column(db.Enum(Especie), nullable=False)
	sexo = db.Column(db.Enum(Sexo))
	color = db.Column(db.Unicode(60))
	edad = db.Column(db.Enum(Edad), nullable=False)
	tamanio = db.Column(db.Enum(Tamanio))
	oreja = db.Column(db.Enum(Orejas))
	pelaje = db.Column(db.Enum(Pelaje))
	otra_informacion_mascota = db.Column(db.Unicode(240))
	departamento = db.Column(db.String(1), nullable=False)
	localidad = db.Column(db.Integer, nullable=False)
	calle = db.Column(db.Unicode(120))
	fecha_encuentro = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	mas_informacion_encuentro = db.Column(db.Unicode(240))
	nombre_contacto = db.Column(db.Unicode(100))
	celular_contacto = db.Column(db.Integer, nullable=False)
	telefono_contacto = db.Column(db.Integer)
	estado_mascota = db.Column(db.Enum(EstadoMascota), nullable=False)
	estado_publicacion = db.Column(db.Enum(EstadoPublicacion))
	fecha_publicacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	usuario_publicacion = db.Column(db.Integer, db.ForeignKey('usuario.id'))
	fotos = db.relationship('ImagenMascota', backref='mascota', lazy='dynamic')

	@property
	def serialize(self):
		return {
				'id': self.id,
				'nombre': self.nombre,
				'especie': self.especie.value,
				'sexo': self.sexo.value,
				'color': self.color,
				'edad': self.edad.value,
				'tamanio': self.tamanio.value,
				'oreja': self.oreja.value,
				'pelaje': self.pelaje.value,
				'otra_informacion_mascota': self.otra_informacion_mascota,
				'departamento': self.departamento,
				'localidad': self.localidad,
				'calle': self.calle,
				'fecha_encuentro': self.fecha_encuentro,
				'mas_informacion_encuentro': self.mas_informacion_encuentro,
				'nombre_contacto': self.nombre_contacto,
				'celular_contacto': self.celular_contacto,
				'telefono_contacto': self.telefono_contacto,
				'estado_mascota': self.estado_mascota.value,
				'estado_publicacion': self.estado_publicacion.value,
				'fecha_publicacion': self.fecha_publicacion
			}


class ImagenMascota(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	img = db.Column(db.Text, unique=True, nullable=False)
	nombre = db.Column(db.Text, nullable=False)
	mimetype = db.Column(db.Text, nullable=False)
	mascota_foto = db.Column(db.Integer, db.ForeignKey('mascota.id'))




## Inicializar datos (Migrations)
def insertarDatosIniciales():
	try:
		# ROLES
		rol_auxiliar = Rol(tipo_rol='Administrador')
		db.session.add(rol_auxiliar)
		rol_auxiliar = Rol(tipo_rol='Común')
		db.session.add(rol_auxiliar)
		rol_auxiliar = Rol(tipo_rol='Desactivado')
		db.session.add(rol_auxiliar)

		# USUARIOS
		usuario_auxiliar = Usuario(username='admin', email='admin@patitas.com', password='admin', rol_id = 1, celular='09999999', telefono='22220000', fecha_registro= datetime.datetime.now(), confirmado=True, fecha_confirmado= datetime.datetime.now())
		db.session.add(usuario_auxiliar)
		usuario_auxiliar = Usuario(username='comun', email='comun@patitas.com', password='comun', rol_id = 2, celular='09999999', telefono='22220000', fecha_registro= datetime.datetime.now(), confirmado=True, fecha_confirmado= datetime.datetime.now())
		db.session.add(usuario_auxiliar)
		
		# MASCOTAS
		mascota_auxiliar = Mascota(
				nombre = 'Chicho',
				especie = 'P',
				sexo = 'M',
				color = 'Negro',
				edad = 'A',
				tamanio = 'C',
				oreja = 'C',
				pelaje = 'L',
				otra_informacion_mascota = 'Perro adulto en adopción',
				departamento = 'M',
				localidad = '1234',
				calle = 'Av. 18 de Julio',
				mas_informacion_encuentro = '',
				nombre_contacto = 'Administrador',
				celular_contacto = '091000000',
				telefono_contacto = '29010000',
				estado_mascota = 'A',
				estado_publicacion = 'P',
				usuario_publicacion = 1
		)
		db.session.add(mascota_auxiliar)

		mascota_auxiliar = Mascota(
				nombre = 'Pocha',
				especie = 'G',
				sexo = 'H',
				color = 'Gris',
				edad = 'A',
				tamanio = 'C',
				oreja = 'C',
				pelaje = 'C',
				otra_informacion_mascota = 'Gata perdida',
				departamento = 'F',
				localidad = '222',
				calle = 'Florida',
				mas_informacion_encuentro = 'Se encontró hace 2 días',
				nombre_contacto = 'Administrador',
				celular_contacto = '091000000',
				telefono_contacto = '29010000',
				estado_mascota = 'E',
				estado_publicacion = 'P',
				usuario_publicacion = 1
		)
		db.session.add(mascota_auxiliar)


		# COMMIT
		db.session.commit()
		print('Datos iniciados.')
	except:
		print('')




db.create_all()
insertarDatosIniciales()

	