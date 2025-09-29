from flask import Blueprint, jsonify
from sqlalchemy import text

try:
    from .model import db
except ImportError:
    from model import db

bp = Blueprint("service", __name__)


@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@bp.route("/health/db", methods=["GET"])
def health_db():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"status": "ok", "db": "up"}), 200
    except Exception as e:
        return jsonify({"status": "fail", "db": "down", "error": str(e)}), 503
