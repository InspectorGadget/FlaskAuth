from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://NICETRY:PASSWORD@gaehub.com/flask_auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'RTG'

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

from app.routes import routes, auth, register