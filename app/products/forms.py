from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


#FORMULARIO DE REGISTRO DE NUEVO PRODUCTO
class NewProductForm(FlaskForm):
    nombre = StringField("Ingrese nombre:")
    precio = StringField("Ingrese su precio:")
    submit = SubmitField ("Registrarse")

