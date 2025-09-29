def test_create_person(client):
    person = {"name": "Bob", "age": 33, "address": "Moscow", "work": "Organization"}
    response = client.post("/api/v1/persons", json=person)

    assert response.status_code == 201
    assert "Location" in response.headers


def test_list_persons(client):
    person_first = {"name": "Bob", "age": 33, "address": "Moscow", "work": "Organization"}
    client.post("/api/v1/persons", json=person_first)

    person_second = {"name": "Steve", "age": 34, "address": "Moscow", "work": "Delivery"}
    client.post("/api/v1/persons", json=person_second)

    response = client.get("/api/v1/persons")
    assert response.status_code == 200


def test_delete_person(client):
    person = {"name": "Bob", "age": 33, "address": "Moscow", "work": "Organization"}
    client.post("/api/v1/persons", json=person)

    response = client.delete("/api/v1/persons/1")
    assert response.status_code == 204

    response = client.delete("/api/v1/persons/1")
    assert response.status_code == 404


def test_edit_person(client):
    person = {"name": "Bob", "age": 33, "address": "Moscow", "work": "Organization"}
    client.post("/api/v1/persons", json=person)

    response = client.patch("/api/v1/persons/1", json={"age": 32, "name": "Ivan"})
    assert response.status_code == 200

    data = response.get_json()
    assert data["name"] == "Ivan"
    assert data["age"] == 32


def test_get_person(client):
    person_first = {"name": "Bob", "age": 33, "address": "Moscow", "work": "Organization"}
    client.post("/api/v1/persons", json=person_first)

    response = client.get("/api/v1/persons/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Bob"
    assert data["age"] == 33
    assert data["address"] == "Moscow"
    assert data["work"] == "Organization"
