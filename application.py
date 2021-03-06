from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, create_engine
#from datetime import datetime 
from flask import Flask, render_template, url_for, request, redirect, flash
import os
from vars import *
from models import Factory,Congac, FactoryAdmin, CongacAdmin, Users, Country, CountryAdmin, UsersAdmin, ModelView

from sqlalchemy.orm import sessionmaker, session



from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
# from flask_migrate import Migrate
#from flask_script import Manager
from flask_admin.contrib.sqla import ModelView
from forms import RegisterForm, LoginForm
# https://ploshadka.net/flask-delaem-avtorizaciju-na-sajjte/ https://pythonru.com/uroki/15-osnovy-orm-sqlalchemy
# https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login-ru
# https://github.com/flask-admin/flask-admin/blob/master/examples/auth-flask-login/app.py
# https://pythobyte.com/flask-user-authentication-be0198e8/

from flask_security import SQLAlchemyUserDatastore, Security
#from userlogin import UsersLogin 
from flask_admin.contrib.sqla import ModelView
from flask_admin import helpers, expose
from flask_admin.contrib import sqla
from flask_admin import Admin



# migrate = Migrate(app, db)
# manager=Manager(app)
# #manager.add_command('db', MigrateCommand)

login_manager = LoginManager(application)


# login_manager.login_view = 'login'
# login_manager.login_message = 'АВТОРИЗУЙТЕСЬ!!!!'
# login_manager.login_message_category = "success"
#
@login_manager.user_loader
def load_user(user_id):
#since the user_id is just the primary key of our user table, use it in the query for the user
	return Users.query.get(int(user_id))

admin = Admin(application)

admin.add_view(CongacAdmin(Congac, db.session))
admin.add_view(FactoryAdmin(Factory, db.session))
admin.add_view(CountryAdmin(Country, db.session))
admin.add_view(UsersAdmin(Users, db.session))
#admin.add_view(UploadAdmin(path, '/uploads/', name='Upload images'))
# Create admin


# db.drop_all()
# db.session.commit()

# db.create_all()
# db.session.commit()



# def addUser(user_name):
# 	user = db.session.query(Users).filter_by(user_name = user_name).first()
# 	print("Пользователь с таким email уже существует")

# Отвечает за сессию пользователей. Запрещает доступ к роутам, перед которыми указано @login_required

# @login_manager.user_loader
# def load_user(user_id):
# 	print('loader USER')
# 	return UsersLogin().from_db(user_id,db)



@application.route('/', methods=("POST", "GET"))
@application.route('/index', methods=("POST", "GET"))
def index():

	pos = db.session.query(Congac).all()
	#print(pos)
	#pos1 = session.query(Congac1)

	return render_template("index.html", title="Главная", pos = pos)

@login_required
@application.route('/congac/<alias>')
def showPost(alias):
	alias = alias

	post = db.session.query(Factory,Congac).join(Congac, Factory.id_factory == Congac.id_factory).filter(Congac.slug_cognac == alias)
	return render_template("post.html", title="Коньяк", post = post)


@application.route('/factory/<alias_factory>')
def showFactory(alias_factory):
	alias_factory = alias_factory
	factory = db.session.query(Factory).filter(Factory.slug_factory == alias_factory)# завод
	congac = db.session.query(Factory,Congac).join(Congac, Factory.id_factory == Congac.id_factory).filter(Factory.slug_factory == alias_factory)
	country = db.session.query(Factory,Country).join(Country, Factory.id_country == Country.id_country).filter(Factory.slug_factory == alias_factory)
	return render_template("factory.html", title="Завод", factory = factory, congac = congac, country = country)

@application.route('/country/<alias_country>')
def showCountry(alias_country):
	alias_country = alias_country
	country = db.session.query(Country).filter(Country.slug_country == alias_country) 
	return render_template("country.html", title="Страна", country = country)


# @app.route('/register',methods=['POST','GET'])
# def register():
# 	forms = RegisterForm()
# 	if request.method == "POST":
# 		hash = generate_password_hash(forms.user_psw.data)
		 
# 		res = db.session.add(Users(user_name = forms.user_name.data, user_mail = forms.user_email.data, user_psw = hash))
# 		db.session.commit()		
# 		return self.render('master.html')
		
# 	return render_template('register.html', forms=forms)


# @app.route('/login',methods=['POST','GET'])
# def login():
# 	forms = LoginForm()
# 	if request.method == "POST":
# 		user = db.session.query(Users).filter(Users.user_mail == forms.email.data).first_or_404()
#  		#psw = db.session.query(Users).filter(Users.user_psw == forms.psw.data).first()
#  		#print(user.user_psw)
# 		if user and check_password_hash(user.user_psw, forms.psw.data):
# 			login_user(user)
# 			return redirect(url_for('profile'))

# 		flash("хьюстон у нас проблемы!!!",'error')

# 	return render_template('login.html', forms=forms)		

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))



# @app.route('/profile')
# @login_required
# def profile():
#     return render_template('profile.html', name=current_user.user_name, mail =current_user.user_mail )

@application.route("/register", methods=["POST", "GET"])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
			hash = generate_password_hash(request.form['psw'])
			res = addUser(form.user_name.data, form.user_mail.data, hash)
			if res:
				flash("Вы успешно зарегистрированы", "success")
				return redirect(url_for('login'))
			else:
				flash("Ошибка при добавлении в БД", "error")
 
	return render_template("register.html", title="Регистрация", form=form)


@application.route('/files/<filename>')
def uploaded_files(filename):
	path = app.config['UPLOADED_PATH']
	return send_from_directory(path, filename)


@application.route('/upload', methods=['POST'])
def upload():
	f = request.files.get('upload')
	extension = f.filename.split('.')[-1].lower()
	if extension not in ['jpg', 'gif', 'png', 'jpeg']:
		return upload_fail(message='Image only!')
	f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
	url = url_for('uploaded_files', filename=f.filename)
	return upload_success(url=url)




# if __name__ == '__main__':
#       app.run(host=os.getenv('IP', '127.0.0.1'), debug=True,
#             port=int(os.getenv('PORT', 4000)))

if __name__ == "__main__":
	application.run(debug=True)