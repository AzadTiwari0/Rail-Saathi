# Flask app initialization
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('../database/config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from app import routes, auth, bookings, trains
