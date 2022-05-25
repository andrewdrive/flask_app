from flask import Flask
from config import Config
from flask_cors import CORS
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)


migrate = Migrate(app, db)

from app import routes, models