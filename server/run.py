import os
from flask import Flask

try:
    from .model import db
    from .controller import bp as persons_bp
    from .service import bp as service_bp
except ImportError:
    from model import db
    from controller import bp as persons_bp
    from service import bp as service_bp

def create_app():
    app = Flask(__name__)

    db_url = os.getenv("DATABASE_URL")

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(persons_bp)
    app.register_blueprint(service_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    port = os.getenv("PORT")
    app.run(host="0.0.0.0", port=port)