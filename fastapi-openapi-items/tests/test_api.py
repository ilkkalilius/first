from fastapi.testclient import TestClient


def test_openapi_endpoint_works(client: TestClient) -> None:
    response = client.get("/openapi.json")

    assert response.status_code == 200
    payload = response.json()
    assert "paths" in payload
    assert "/api/items" in payload["paths"]


def test_create_item(client: TestClient) -> None:
    response = client.post(
        "/api/items",
        json={"name": "Keyboard", "description": "Mechanical keyboard"},
    )

    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Keyboard"


def test_get_item(client: TestClient) -> None:
    create_response = client.post(
        "/api/items",
        json={"name": "Mouse", "description": "Wireless mouse"},
    )
    item_id = create_response.json()["id"]

    response = client.get(f"/api/items/{item_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "Mouse"


def test_list_items(client: TestClient) -> None:
    client.post("/api/items", json={"name": "Monitor", "description": "27 inch"})
    client.post("/api/items", json={"name": "Laptop stand", "description": None})

    response = client.get("/api/items")

    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 2
    assert payload[0]["name"] == "Monitor"
    assert payload[1]["name"] == "Laptop stand"
