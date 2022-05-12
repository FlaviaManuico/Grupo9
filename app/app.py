import sys
from datetime import datetime
from flask import Flask, jsonify, request, url_for, render_template, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

#Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/pizza'
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
