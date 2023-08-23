#dependecias de flask
from flask import Flask 
#dependecia de configuracion
from .config import Config
#dependecias de modelos
from flask_sqlalchemy import SQLAlchemy
#Dependecias de migraciones
from flask_migrate import Migrate
from .mi_blueprint import mi_blueprint
from app.products import products


#dependencia bootstrap 
from flask_bootstrap import Bootstrap




#crear el objeto Flask
app = Flask(__name__)
#configuracion del objeto flask
app.config.from_object(Config)

#vincular blueprints del proyecto
app.register_blueprint(mi_blueprint)
app.register_blueprint(products)


#crear el objeto de modelo:
db = SQLAlchemy(app)


# crear el objetivo de migracion:
migrate = Migrate(app, db)

#crear objeto bootstrap
bootstrap = Bootstrap(app)



#importar los modelos de .models
from .models import Cliente, Producto, Venta, Detalle