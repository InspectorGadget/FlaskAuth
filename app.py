from app import app
from app import db

if __name__ == "__main__":
    db.init_app(app)
    app.run()