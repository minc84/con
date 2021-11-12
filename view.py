from flask import render_template
from models import Congac




@app.route('/', methods=("POST", "GET"))
@app.route('/index', methods=("POST", "GET"))

def index():	
	return render_template("index.html", title="Главная")