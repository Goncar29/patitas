from flask import Flask

app = Flask(__name__)
app.secret_key = 'estoesunapassword1'
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data/basededatos.db'

from patitas import models
from patitas import views
