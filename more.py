# engine = create_engine('mysql+pymysql://user:11111111@localhost/congac', pool_recycle=3600)

# Base = declarative_base()



# def slugify(s):
# 	pattern = r'[^/w+]'
# 	return re.sub(pattern,'-',s)

# class Congac(Base):
# 	__tablename__ = 'congacs'

# 	id_cognac = Column(Integer, primary_key=True, autoincrement=True )
# 	title_cognac = Column(String(140),nullable=False)
# 	text_cognac = Column(Text)
# 	date_cognac = Column(DateTime, default=datetime.now())
# 	slug_cognac	= Column(String(140),nullable=False, unique=True)

# 	def __init__(self, *args,**kwargs):
# 		super(Congac, self).__init__(*args,**kwargs)
# 		self.generate_slug()

# 	def generate_slug(self):
# 		if self.title_cognac:
# 			self.slug_cognac = slugify(self.title_cognac)

# 	def __repr__(self):
# 		return f'<Congac id_cognac:{self.id_cognac}, title_cognac:{self.title_cognac}>'


<ul>
<li>	Коньяк: {{c.title_cognac}}</li>
		<li>Описание Коньяка : {{ c.text_cognac |safe}}</li>
          <li>Производитель: {{f.title_factory}}</li>
            <li>Описание: {{f.text_factory | striptags}}</li>

         
              
         </ul>

Выборка по заводам

	pos = db.session.query(Factory,Congac).join(Congac, Factory.id_factory == Congac.id_factory)
	#print(pos)
	#pos1 = session.query(Congac1)

	return render_template("index.html", title="Главная", pos = pos)

#Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)

#Session = sessionmaker(bind=engine)
#session = Session()
# db.create_all()
# db.session.commit()
# # db.drop_all()
# db.session.commit()



@app.route("/register", methods=["POST", "GET"])
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



@app.route('/files/<filename>')
def uploaded_files(filename):
	path = app.config['UPLOADED_PATH']
	return send_from_directory(path, filename)


@app.route('/upload', methods=['POST'])
def upload():
	f = request.files.get('upload')
	extension = f.filename.split('.')[-1].lower()
	if extension not in ['jpg', 'gif', 'png', 'jpeg']:
		return upload_fail(message='Image only!')
	f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
	url = url_for('uploaded_files', filename=f.filename)
	return upload_success(url=url)
