from flask import Blueprint, request, jsonify
from model import db, Person

bp = Blueprint("persons", __name__, url_prefix="/api/v1/persons")


@bp.route("/<int:id>", methods=["GET"])
def get_person(id):
    person = Person.query.get(id)
    if person:
        return jsonify({
            "id": person.id,
            "name": person.name,
            "age": person.age,
            "address": person.address,
            "work": person.work
        }), 200
    return jsonify({"message": "Not found Person for ID"}), 404


@bp.route("", methods=["GET"])
def list_persons():
    persons = Person.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "age": p.age,
            "address": p.address,
            "work": p.work
        } for p in persons
    ]), 200


@bp.route("", methods=["POST"])
def create_person():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"message": "Invalid data"}), 400

    person = Person(
        name=data.get("name"),
        age=data.get("age"),
        address=data.get("address"),
        work=data.get("work")
    )
    db.session.add(person)
    db.session.commit()
    return "", 201, {"Location": f"/api/v1/persons/{person.id}"}


@bp.route("/<int:id>", methods=["PATCH"])
def edit_person(id):
    person = Person.query.get(id)
    if not person:
        return jsonify({"message": "Not found Person for ID"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid data"}), 400

    for field in ["name", "age", "address", "work"]:
        if field in data:
            setattr(person, field, data[field])

    db.session.commit()
    return jsonify({
        "id": person.id,
        "name": person.name,
        "age": person.age,
        "address": person.address,
        "work": person.work
    }), 200


@bp.route("/<int:id>", methods=["DELETE"])
def delete_person(id):
    person = Person.query.get(id)
    if person:
        db.session.delete(person)
        db.session.commit()
    return "", 204
