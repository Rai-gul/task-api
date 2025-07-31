from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # create SQLAlchemy instance here (outside create_app)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # or your DB URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # <- This is crucial to link db to the app

    with app.app_context():
        db.create_all()  # create tables

    # Register blueprints here
    from routes.tasks import tasks_bp
    app.register_blueprint(tasks_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
