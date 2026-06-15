import os

import pytest
from app.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_root_route(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"status": "ok it work"}


def test_health_route_default_db_url(client, monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    response = client.get("/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"db_url": "not set"}


def test_health_route_with_db_url(client, monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgres://test")
    response = client.get("/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"db_url": "postgres://test"}
