from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)

from app import routes
