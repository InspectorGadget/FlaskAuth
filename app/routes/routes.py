from app import app
from app.models.user import User

@app.route('/')
def index():
    return {'message': 'App is working!'}