from flask import Flask
from routes import first_route
from models import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///first.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(first_route)

if __name__ == "__main__":
    app.run(debug=True)
