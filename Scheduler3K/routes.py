import os
from flask import render_template, url_for, redirect, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
from Scheduler3K import app, bcrypt, db
from Scheduler3K.models import User, Group
from Scheduler3K.forms import RegistrationForm, LoginForm, GroupForm, GroupChangeForm, group_list

show_diagrams = False
ALLOWED_EXTENSIONS = set(['pdf'])


# Creating dict from db data
def show_groups():
    return {item.group_number: item.group_number for item in Group.query.all()}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/home')
def home_page():
    title = 'Scheduler3K'
    return render_template('home.html', title=title, show_diagrams=show_diagrams)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    title = 'Регистрация'

    if current_user.is_authenticated:
        return redirect(url_for('home_page'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')

        if form.is_curator.data is True:
            group = 'None'
            user = User(username=form.username.data,
                        is_curator=form.is_curator.data, password=hashed_password, group_number=group)
        else:
            user = User(username=form.username.data,
                        is_curator=form.is_curator.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Аккаунт создан', 'success')
        return redirect(url_for('login_page'))
    return render_template('register.html', title=title, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    title = 'Вход'
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home_page'))
        else:
            flash('Неправильный логин или пароль', 'danger')
    return render_template('login.html', title=title, form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    return redirect(url_for('home_page'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account_page():
    title = 'Аккаунт'
    form = GroupForm()
    form2 = GroupChangeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.file_name.data:
                file = form.file_name.data
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                group = Group(group_number=form.group_number.data)
                db.session.add(group)
                db.session.commit()
                flash('Группа добавлена', 'success')
                return redirect(url_for('account_page'))

        if form2.validate_on_submit():
            print(type(str(form2.group_number.data)))
            print(type(current_user.group_number))
            current_user.group_number = str(form2.group_number.data)
            db.session.commit()
            flash('Группа обновлена', 'success')
            return redirect(url_for('account_page'))
    elif request.method == 'GET':
        return render_template('account.html', title=title, form=form, form2=form2)
    return render_template('account.html', title=title, form=form, form2=form2)


@app.route('/timetable/<group>')
def timetable_page(group):
    title = 'Расписание'
    return render_template('timetable.html', title=title, group=group)


@app.context_processor
def context_processor():
    return dict(group_list=[*show_groups()])
