from datetime import timedelta

from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.forms import LoginForm, RegisterForm
from app.models import User


def init_app(app):
    @app.route('/')
    def index():
        users = User.query.all() # Select * from users
        return render_template('users.html', users=users)


    @app.route('/user/delete/<int:id>')
    def delete(id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

        return redirect(url_for('index'))


    @app.route('/user/<int:id>')
    @login_required
    def unique(id):
        user = User.query.get(id)
        return render_template('user.html', user=user)


    @app.route('/register', methods=['GET','POST'])
    def register():
        form = RegisterForm()

        if form.validate_on_submit():
            user = User()
            user.name = form.name.data
            user.email = form.email.data
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('login'))

        return render_template('register.html', form=form)


    @app.route('/login', methods=['GET','POST'])
    def login():
        form = LoginForm()

        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = User.query.filter_by(email=email).first()

            if not user or not check_password_hash(user.password, password):
                flash('Credênciais incorretas.', 'danger')
                return redirect(url_for('login'))

            login_user(user, remember=remember, duration=timedelta(days=7))
            return redirect(url_for('index'))

        return render_template('login.html', form=form)


    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))
