import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.items_service import items_service


@pytest.fixture(autouse=True)
def clean_items_service() -> None:
    items_service.clear()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
