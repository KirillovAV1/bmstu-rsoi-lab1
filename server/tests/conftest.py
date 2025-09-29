import os
import pytest

os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")

from sqlalchemy import text
from server.run import create_app
from server.model import db


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config.update(TESTING=True)
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    with app.app_context():
        db.session.execute(text("DELETE FROM person"))
        db.session.commit()
    return app.test_client()
