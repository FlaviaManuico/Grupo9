import sys
from datetime import datetime
from flask import Flask, jsonify, request, url_for, render_template, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/pizza'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super secret key'
db = SQLAlchemy(app)

# Models


class usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(), nullable=False)
    contrasena = db.Column(db.String(), nullable=False)
    nombre = db.Column(db.String(), nullable=False)
    apellido = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    direccion = db.Column(db.String(), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    fechaHora = db.Column(db.DateTime, default=datetime.now())

    def __init__(
            self,
            usuario,
            contrasena,
            nombre,
            apellido,
            email,
            direccion,
            telefono):
        self.usuario = usuario
        self.contrasena = self.create_password(contrasena)
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def create_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.contrasena, password)

    def __repr__(self):
        return f'Usuario: id={self.id}, usuario={self.usuario}, contrasena={self.contrasena}, nombre={self.nombre}, apellido={self.apellido}, email={self.email}, direccion={self.direccion}, telefono={self.telefono},fechaHora={self.fechaHora}'


class producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    comida = db.Column(db.String(), nullable=False)
    precio = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f'Producto: id={self.id} comida={self.comida}, precio={self.precio}'


class pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer(), primary_key=True)
    descripcion = db.Column(db.String(), nullable=False)
    precio = db.Column(db.Float(), nullable=False)
    cliente = db.Column(db.String(), nullable=False)
    fechaHora = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'Pedido: id={self.id} descripcion={self.descripcion} precio={self.precio} cliente={self.cliente}'


db.create_all()
# Entradas
pAjo2 = producto(comida='Pan al Ajo (x2)', precio=4.00)
pAjo4 = producto(comida='Pan al Ajo (x4)', precio=8.00)
pQueso2 = producto(comida='Palitos de Queso (x2)', precio=5.50)
pQueso4 = producto(comida='Palitos de Queso (x4)', precio=11.00)

# Pizzas
PHf = producto(comida='Pizza Hawaiana Familiar', precio=32.90)
PHg = producto(comida='Pizza Hawaiana Grande', precio=22.90)
PHm = producto(comida='Pizza Hawaiana Mediana', precio=16.90)
PHp = producto(comida='Pizza Hawaiana Personal', precio=10.00)
PAf = producto(comida='Pizza Americana Familiar', precio=29.90)
PAg = producto(comida='Pizza Americana Grande', precio=19.90)
PAm = producto(comida='Pizza Americana Mediana', precio=13.90)
PAp = producto(comida='Pizza Americana Personal', precio=7.00)
PPf = producto(comida='Pizza de Pepperoni Familiar', precio=30.90)
PPg = producto(comida='Pizza de Pepperoni Grande', precio=20.90)
PPm = producto(comida='Pizza de Pepperoni Mediana', precio=14.90)
PPp = producto(comida='Pizza de Pepperoni Personal', precio=8.00)
PMf = producto(comida='Pizza Mozarella Familiar', precio=31.90)
PMg = producto(comida='Pizza Mozarella Grande', precio=21.90)
PMm = producto(comida='Pizza Mozarella Mediana', precio=15.90)
PMp = producto(comida='Pizza Mozarella Personal', precio=9.00)

# Lasagnas
lVegetariana = producto(comida='Lasagna Vegetariana', precio=22.90)
lCarne = producto(comida='Lasagna de Carne', precio=20.90)
lHawaiana = producto(comida='Lasagna Hawaiana', precio=22.90)
lQueso = producto(comida='Lasagna de 4 Quesos', precio=24.90)
lChamp = producto(comida='Lasagna de Champiñones', precio=25.90)

# Combos
cpAmericana = producto(comida='Combo Personal - Pizza Americana', precio=11.50)
cpPepperoni = producto(comida='Combo Personal - Pizza Pepperoni', precio=12.50)
cpHawaiana = producto(comida='Combo Personal - Pizza Hawaiana', precio=14.50)
cmAmericana = producto(comida='Combo Mediano - Pizza Americana', precio=25.90)
cmPepperoni = producto(comida='Combo Mediano - Pizza Pepperoni', precio=26.50)
cmHawaiana = producto(comida='Combo Mediano - Pizza Hawaiana', precio=28.50)

# Bebidas
CPersonal = producto(comida='Coca Cola Personal', precio=2.50)
CPersonalSA = producto(comida='Coca Cola Personal Sin Azucar', precio=7.20)
Cp1L = producto(comida='Coca Cola 1L', precio=4.00)
Co1LSA = producto(comida='Coca Cola Sin Azucar 1L', precio=4.20)
Co1_5L = producto(comida='Coca Cola 1.5L', precio=7.00)
Co1_5SA = producto(comida='Coca Cola Sin Azucar 1.5L', precio=7.20)
InP = producto(comida='Inca Kola Personal', precio=2.50)
InPSA = producto(comida='Inca Kola Personal Sin Azucar', precio=2.70)
In1L = producto(comida='Inca Kola 1L', precio=4.00)
In1lSA = producto(comida='Inca Kola Sin Azucar 1L', precio=4.20)
In1_5 = producto(comida='Inca Kola 1.5L', precio=7.00)
In1_5SA = producto(comida='Inca Kola Sin Azucar 1.5L', precio=7.20)
FaP = producto(comida='Fanta Personal', precio=3.20)
SpP = producto(comida='Sprite Personal', precio=3.20)

# Postres
VCh = producto(comida='Volcán de Chocolate', precio=6.00)
RdC6 = producto(comida='Rollos de Canela x6', precio=14.00)
MPdM = producto(comida='Mini Pie de Manzana', precio=6.00)

if len(producto.query.all()) == 0:
    db.session.add_all([pAjo2,
                        pAjo4,
                        pQueso2,
                        pQueso4,
                        PHf,
                        PHg,
                        PHm,
                        PHp,
                        PAf,
                        PAg,
                        PAm,
                        PAp,
                        PPf,
                        PPg,
                        PPm,
                        PPp,
                        PMf,
                        PMg,
                        PMm,
                        PMp,
                        lVegetariana,
                        lCarne,
                        lHawaiana,
                        lQueso,
                        lChamp,
                        cpAmericana,
                        cpPepperoni,
                        cpHawaiana,
                        cmAmericana,
                        cmPepperoni,
                        cmHawaiana,
                        VCh,
                        RdC6,
                        MPdM])
    db.session.add(CPersonal)
    db.session.add(CPersonalSA)
    db.session.add(Cp1L)
    db.session.add(Co1LSA)
    db.session.add(Co1_5L)
    db.session.add(Co1_5SA)
    db.session.add(InP)
    db.session.add(InPSA)
    db.session.add(In1L)
    db.session.add(In1lSA)
    db.session.add(In1_5)
    db.session.add(In1_5SA)
    db.session.add(FaP)
    db.session.add(SpP)
    db.session.commit()


@app.route('/', methods=['GET'])
def index():
    return render_template('ingresar.html')


@app.route('/guidos/login', methods=['POST'])
def log_in():
    username = request.form.get('NombreDeUsuario', '')
    password = request.form.get('Contraseña', '')
    user = usuario.query.filter_by(usuario=username).first()
    if user is not None and user.verify_password(password):
        session['username'] = username
        return render_template("pizzas.html")
    else:
        flash('Usuario o contraseña incorrecta')
        return redirect(url_for('index'))


@app.route('/registrarse', methods=['GET'])
def registrar():
    return render_template('registro.html')


@app.route('/entradas', methods=['GET'])
def ir_entrada():
    return render_template('entradas.html')


@app.route('/pizzas', methods=['GET'])
def ir_pizzas():
    return render_template('pizzas.html')


@app.route('/lasagnas', methods=['GET'])
def ir_lasagnas():
    return render_template('lasagna.html')


@app.route('/combos', methods=['GET'])
def ir_comobos():
    return render_template('combos.html')


@app.route('/bebidas', methods=['GET'])
def ir_bebidas():
    return render_template('bebidas.html')


@app.route('/postres', methods=['GET'])
def ir_postres():
    return render_template('postres.html')


@app.route('/pedidos', methods=['GET'])
def ir_pedidos():
    return render_template('pedidos.html')


@app.route('/guidos/create_user', methods=['POST'])
def create_user():
    try:
        user = request.form.get('usuario', '')
        email = request.form.get('email', '')
        contrasena = request.form.get('contrasena', '')
        nombre = request.form.get('nombre', '')
        apellido = request.form.get('apellido', '')
        direccion = request.form.get('direccion', '')
        telefono = request.form.get('telefono', '')
        respuesta = [
            user,
            contrasena,
            nombre,
            apellido,
            email,
            direccion,
            telefono]
        user_base = usuario.query.filter_by(usuario=user).first()
        email_base = usuario.query.filter_by(email=email).first()

        if '' in respuesta:
            print(respuesta)
            session['registro'] = user
            flash('Por favor llene todos los casilleros')
            return redirect(url_for('registrar'))
        else:
            if user_base is None and email_base is None:
                new_user = usuario(
                    user,
                    contrasena,
                    nombre,
                    apellido,
                    email,
                    direccion,
                    telefono)
                db.session.add(new_user)
                db.session.commit()
            else:
                if user_base.usuario == user or email_base.email == email:
                    session['registro'] = user
                    flash('Usuario o correo ya usado')
                    return redirect(url_for('registrar'))
                else:
                    new_user = usuario(
                        user,
                        contrasena,
                        nombre,
                        apellido,
                        email,
                        direccion,
                        telefono)
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
