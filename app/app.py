import sys
from datetime import datetime
from flask import Flask, jsonify, request, url_for, render_template, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

#Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/pizza'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super secret key'
db = SQLAlchemy(app)

#Models
class usuario(db.Model):
    __tablename__ = 'usuarios'
    id=db.Column(db.Integer,primary_key=True)    
    usuario=db.Column(db.String(),nullable=False)
    contrasena=db.Column(db.String(),nullable=False)
    nombre=db.Column(db.String(),nullable=False)
    apellido=db.Column(db.String(),nullable=False)
    email=db.Column(db.String(),nullable=False)
    direccion=db.Column(db.String(),nullable=False)
    telefono=db.Column(db.Integer,nullable=False)
    fechaHora = db.Column(db.DateTime,default= datetime.now())

    def __init__(self,usuario,contrasena,nombre,apellido,email,direccion,telefono):
        self.usuario=usuario
        self.contrasena=self.create_password(contrasena)
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.direccion=direccion
        self.telefono=telefono

    def create_password(self,password):
        return generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.contrasena,password)

    def __repr__(self):
        return f'Usuario: id={self.id}, usuario={self.usuario}, contrasena={self.contrasena}, nombre={self.nombre}, apellido={self.apellido}, email={self.email}, direccion={self.direccion}, telefono={self.telefono},fechaHora={self.fechaHora}'

class producto(db.Model):
    __tablename__ = 'productos'
    id=db.Column(db.Integer,primary_key=True)
    comida = db.Column(db.String(),nullable=False)
    precio= db.Column(db.Integer, nullable=False)
     
    def __repr__(self):
        return f'Producto: id={self.id} comida={self.comida}, precio={self.precio}'

class pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer(), primary_key=True)
    descripcion = db.Column(db.String(),nullable=False)
    precio = db.Column(db.Float, nullable=False)
    cliente = db.Column(db.String(), nullable=False)
    fechaHora = db.Column(db.DateTime, nullable=False)
    delivery = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Pedido: id={self.id} descripcion={self.descripcion} precio={self.precio} cliente={self.cliente} fechaHora={self.fechaHora} delivery={self.delivery}'

db.create_all()

@app.route('/', methods=['GET'])
def index():
    return render_template('ingresar.html')


@app.route('/guidos/login', methods=['POST'])
def log_in():
    username= request.form.get('NombreDeUsuario','')
    password= request.form.get('Contraseña','')
    user= usuario.query.filter_by(usuario=username).first()
    if user is not None and user.verify_password(password):
        session['username'] = username
        return render_template("pizzas.html")
    else:
        flash('Usuario o contraseña incorrecta')
        return redirect(url_for('index'))
        
@app.route('/registrarse',methods=['GET'])
def registrar():
    return render_template('registro.html')

@app.route('/guidos/create_user',methods=['POST'])
def create_user():
    try:       
        user= request.form.get('usuario','')
        email= request.form.get('email','')
        contrasena= request.form.get('contrasena','')
        nombre= request.form.get('nombre','')
        apellido= request.form.get('apellido','')
        direccion= request.form.get('direccion','')
        telefono= request.form.get('telefono','')
        respuesta=[user,contrasena,nombre,apellido,email,direccion,telefono]
        user_base= usuario.query.filter_by(usuario=user).first()
        email_base= usuario.query.filter_by(email=email).first()
        
        if '' in respuesta :
            print(respuesta)
            session['registro'] = user
            flash('Por favor llene todos los casilleros')
            return redirect(url_for('registrar'))
        else:
            if user_base==None and email_base==None:
                new_user= usuario(user,contrasena,nombre,apellido,email,direccion,telefono)
                db.session.add(new_user)
                db.session.commit()
            else:
                if user_base.usuario==user or email_base.email==email:
                    session['registro'] = user
                    flash('Usuario o correo ya usado')
                    return redirect(url_for('registrar'))
                else:
                    new_user= usuario(user,contrasena,nombre,apellido,email,direccion,telefono)
                    db.session.add(new_user)
                    db.session.commit()
        
    except Exception as e:
        print(e)
        print(sys.exc_info())
        db.session.rollback()
    finally:
        db.session.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
