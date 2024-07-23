from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    # Create Flask app instance
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a9d108e0e581ba50aa01bf74aa60c9ac'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anime_site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Set the login_view for Flask-Login
    login_manager.login_view = 'login'

    # Import routes and models
    with app.app_context():
        from app import routes
        from app.models import Recipe, User
        # to create the tables automatically
        # db.create_all()

    # Define the User loader function for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app