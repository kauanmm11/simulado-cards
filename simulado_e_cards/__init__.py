from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '416e7e3da3790330038b0a7f997ef687'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"

database = SQLAlchemy(app)

from simulado_e_cards import routes