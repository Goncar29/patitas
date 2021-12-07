import enum

class Especie(enum.Enum):
	P = "Perro"
	G = "Gato"

class Sexo(enum.Enum):
	H = "Hembra"
	M = "Macho"
	S = "Sin especificar"

class Edad(enum.Enum):
	C = "Cachorro"
	A = "Adulto"

class Tamanio(enum.Enum):
	C = "Chico"
	M = "Mediano/Grande"

class Orejas(enum.Enum):
	C = "Caídas"
	P = "En punta"
	O = "Otro"

class Pelaje(enum.Enum):
	C = "Corto"
	L = "Largo"
	P = "Sin pelo"

class EstadoMascota(enum.Enum):
	A = "En adopción"
	E = "Encontrado"

class EstadoPublicacion(enum.Enum):
	S = "No publicado"
	P = "Publicado"
