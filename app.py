#dependecias de flask
from flask import Flask
#dependecias de modelos
from flask_sqlalchemy import SQLAlchemy
#Dependecias de migraciones
from flask_migrate import Migrate
#Dependencia para fecha y hora del sistema
from datetime import datetime

#crear el objeto Flask
app = Flask(__name__)

#Definir 'la cadena de conexion' (connectionstring)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

#crear el objeto de modelo:
db = SQLAlchemy(app)

# crear el objetivo de migracion:
migrate = Migrate(app, db)

#crear los modelos:
class Cliente(db.Model):
    #definir los atributos
    __tablename__="clientes"
    id = db.Column(db.Integer , primary_key = True )
    username = db.Column(db.String(120),
                         nullable = True)
    password = db.Column(db.String(128),
                         nullable = True)
    email = db.Column(db.String(100),
                      nullable = True)
    


class Producto(db.Model):
    #definir los atributos
    __tablename__="productos"
    id = db.Column(db.Integer , primary_key = True )
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(200))



class Venta(db.Model):
    #definir los atributos
    __tablename__="ventas"
    id = db.Column(db.Integer , primary_key = True )
    fecha = db.Column(db.DateTime ,
                       default = datetime.utcnow)
    #clave foranea:
    cliente_id = db.Column(db.Integer, 
                           db.ForeignKey('clientes.id'))

    
class Detalle(db.Model):
    #definir los atributos
    __tablename__="detalles"
    id = db.Column(db.Integer , primary_key = True )
    producto_id = db.Column(db.Integer, 
                            db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer, 
                            db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)
    