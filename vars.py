from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor, CKEditorField, upload_fail, upload_success
import os
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from passlib.hash import sha256_crypt


application  = Flask(__name__)

#pas1 = sha256_crypt.encrypt("11111111")

basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:11111111@localhost/congac'
application.config['SECRET_KEY'] = "aadadfasdasd"
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user2:11111111@ec2-16-170-7-86.eu-north-1.compute.amazonaws.com/congac'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Lokomotiv1@database-1-instance-1.chv893ja4f5u.eu-north-1.rds.amazonaws.com/congac'

application.config['ALLOWED_CONTENT'] = True
application.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
# app.config['CKEDITOR_ENABLE_CSRF'] = True  # if you want to enable CSRF protect, uncomment this line
application.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')
application.config['CKEDITOR_PKG_TYPE'] = 'full'

db = SQLAlchemy(application) 
ckeditor = CKEditor(application)
#ckeditor.config['allowedContent'] = True

