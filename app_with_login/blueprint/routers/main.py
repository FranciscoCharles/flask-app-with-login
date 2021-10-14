from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user
from flask import Blueprint, request
from app_with_login.ext.database import db
from app_with_login.models import User
from sqlalchemy.exc import SQLAlchemyError


bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    errors = None
    name = ''
    email = ''
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        if name and email and password:
            try:
                user = User(name, email, password)
                query_user = User.query.filter_by(email=email).first()
                
                if not query_user:
                    db.session.add(user)
                    db.session.commit()
                    login_user(user)
                    return redirect(url_for('.home'))

                else:
                    errors = 'Usuario  ja existe!'
            except SQLAlchemyError:
                errors = 'Ocorreu um erro desconhecido, tente Novamente!'
        else:
            errors = 'Campos invalidos!'

    return render_template('register.html', errors=errors, name=name, email=email)

@bp.route('/login', methods=['GET', 'POST'])
def login():    
    errors = None
    email = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email and password:
            try:
                user = User.query.filter_by(email=email).first()
                if not user or not user.verify_password(password):
                    errors = 'Email ou Senha invalidos!'
                else:
                    login_user(user)
                    return redirect(url_for('.home'))
            except SQLAlchemyError:
                errors = 'Ocorreu um erro desconhecido, tente Novamente!'
        else:
            errors = 'Campos invalidos!'
    return render_template('login.html', email=email, errors=errors)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.login'))

def init_app(app):
    app.register_blueprint(bp)