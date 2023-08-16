#dependecias de flask
from flask import Flask 
#dependecia de configuracion
from .config import Config
#dependecias de modelos
from flask_sqlalchemy import SQLAlchemy
#Dependecias de migraciones
from flask_migrate import Migrate

#crear el objeto Flask
app = Flask(__name__)
#configuracion del objeto flask
app.config.from_object(Config)

DeprecationWarning

#crear el objeto de modelo:
db = SQLAlchemy(app)
# crear el objetivo de migracion:
migrate = Migrate(app, db)

#importar los modelos de .models
from .models import Cliente, Producto, Venta, Detalle