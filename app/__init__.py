from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
##importr config 
from .config import Config

##crear objeto de app
app = Flask(__name__)

##configura el objeto flask
app.config.from_object(Config)

##objeto SQLAlchemy
db = SQLAlchemy(app)

#objeto para las migraciones
migrate = Migrate(app, db)

#importar las rutas

from . import routes 

#importar los modelos
from .models import Medico, Paciente, Consultorio, Cita

##ejecutar el objeto
if __name__== "__main__":
    app.run()