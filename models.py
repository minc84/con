from datetime import datetime 
import re
from flask_sqlalchemy import SQLAlchemy
from vars import *
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from flask_login import UserMixin


class Country(db.Model):
	__tablename__ = 'countrys'
	
	id_country = db.Column(db.Integer, primary_key=True, autoincrement=True )
	title_country = db.Column(db.String(140),nullable=False)
	text_country = db.Column(db.Text)
	seo_description_country = db.Column(db.String(240))
	slug_country = db.Column(db.String(140),nullable=False, unique=True)
	pr1 = db.relationship('Factory', backref = 'country', lazy='dynamic')
	# Flask - Login

	def __init__(self, *args,**kwargs):
		super(Country, self).__init__(*args,**kwargs)

	def __repr__(self):
		return self.title_country


class Factory(db.Model):
	__tablename__ = 'factories'

	id_factory = db.Column(db.Integer, primary_key=True, autoincrement=True )
	title_factory = db.Column(db.String(140),nullable=False)
	text_factory = db.Column(db.Text)
	site_factory = db.Column(db.String(140))
	date_factory = db.Column(db.DateTime, default=datetime.now())
	slug_factory = db.Column(db.String(140),nullable=False, unique=True)
	seo_description_factory = db.Column(db.String(240))
	id_country = db.Column(db.Integer, db.ForeignKey('countrys.id_country'))

	pr = db.relationship('Congac', backref = 'factory', lazy='dynamic')

	def __init__(self, *args,**kwargs):
		super(Congac, self).__init__(*args,**kwargs)

	def __repr__(self):
		return self.title_factory


class Congac(db.Model):
	__tablename__ = 'congacs'

	id_cognac = db.Column(db.Integer, primary_key=True, autoincrement=True )
	title_cognac = db.Column(db.String(140),nullable=False)
	text_cognac = db.Column(db.Text)
	date_cognac = db.Column(db.DateTime, default=datetime.now())
	slug_cognac	= db.Column(db.String(140),nullable=False, unique=True)
	id_factory = db.Column(db.Integer, db.ForeignKey('factories.id_factory'))
	seo_description_cognac = db.Column(db.String(240))
	#pr = db.relationship('Country', backref = 'country', lazy='dynamic')

	def __init__(self, *args,**kwargs):
		super(Congac, self).__init__(*args,**kwargs)

	def __repr__(self):
		return self.title_cognac, self.id_factory

class Users(UserMixin, db.Model):
	__tablename__ = 'users'

	user_id = db.Column(db.Integer, primary_key=True, autoincrement=True )
	user_name = db.Column(db.String(140),nullable=False)
	user_mail = db.Column(db.String(140),nullable=False)
	user_psw = db.Column(db.String(140),nullable=False)
	user_date = db.Column(db.DateTime, default=datetime.now())

	def get_id(self):
		return (self.user_id)


class FactoryAdmin(ModelView):
	form_overrides = dict(text_factory=CKEditorField)
	#ckeditor.config(allowedContent = 'true')
	create_template = 'admin/edit.html'
	edit_template = 'admin/edit.html'

class CongacAdmin(ModelView):
	form_overrides = dict(text_cognac=CKEditorField)
	#ckeditor.config(allowedContent = 'true')
	create_template = 'admin/edit.html'
	edit_template = 'admin/edit.html'

class CountryAdmin(ModelView):
	form_overrides = dict(text_country=CKEditorField)
	#ckeditor.config(allowedContent = 'true')
	create_template = 'admin/edit.html'
	edit_template = 'admin/edit.html'

class UsersAdmin(ModelView):
	#form_overrides = dict(text_country=CKEditorField)
	#ckeditor.config(allowedContent = 'true')
	create_template = 'admin/edit.html'
	edit_template = 'admin/edit.html'




	

 #    # Required for administrative interface
	# def __unicode__(self):
	# 	return self.user_name

	# def set_password(self, password):
	# 	self.user_psw = generate_password_hash(password)

	# def check_password(self, password):
	# 	return check_password_hash(self.user_psw, password)




