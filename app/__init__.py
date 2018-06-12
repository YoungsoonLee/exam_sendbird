from flask import Flask
from app.config import DATABASE_URI
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DATABASE
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# Blueprints
from app.routes.routes import api
from app.routes.task import task

# routing
app.register_blueprint(api)
app.register_blueprint(task)
