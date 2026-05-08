from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import bcrypt, jwt

from models import db
from routes.auth_routes import auth_bp
from routes.opportunity_routes import opportunity_bp


app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

jwt.init_app(app)
bcrypt.init_app(app)

db.init_app(app)
app.register_blueprint(auth_bp, url_prefix='/api/auth')

app.register_blueprint(opportunity_bp, url_prefix='/api/opportunities')


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return {
        'message': 'Qatar Foundation Backend Running'
    }


if __name__ == '__main__':
    app.run(debug=True)