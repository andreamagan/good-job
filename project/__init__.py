from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.config import ConfigDB

app = Flask(__name__)
app.config.from_object(ConfigDB)

db = SQLAlchemy(app)