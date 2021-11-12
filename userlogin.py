from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from vars import *
from models import Users
from flask_sqlalchemy import SQLAlchemy

class UsersLogin():
	def from_db(self, user_id,db):
		self.__user = db.session.query(Users).get(user_id)
		return self

	def create(self,user):
		self.__user = user
		return self

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.__user[user_id])