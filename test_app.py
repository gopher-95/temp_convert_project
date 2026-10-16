from fastapi.testclient import TestClient
from app_final import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.json()


def test_convert_fahrenheit():
    response = client.get("/convert/fahrenheit?celsius=20")
    assert response.status_code == 200
    data = response.json()
    assert data["celsius"] == 20.0
    assert data["fahrenheit"] == 68.0


def test_convert_kelvin():
    response = client.get("/convert/kelvin?celsius=20")
    assert response.status_code == 200
    data = response.json()
    assert data["celsius"] == 20
    assert data["kelvin"] == 293.15


def test_convert_all():
    response = client.get("/convert/all?celsius=20")
    assert response.status_code == 200
    data = response.json()
    assert data["celsius"] == 20.0
    assert data["fahrenheit"] == 68.0
    assert data["kelvin"] == 293.15


def test_convert_to_fahrenheit():
    response = client.get("/convert/to/fahrenheit?celsius=20")
    assert response.status_code == 200
    data = response.json()
    assert data["fahrenheit"] == 68.0


def test_convert_to_kelvin():
    response = client.get("/convert/to/kelvin?celsius=20")
    assert response.status_code == 200
    data = response.json()
    assert data["kelvin"] == 293.15


def test_convert_to_unknown_unit():
    response = client.get("/convert/to/rankine?celsius=20")
    assert response.status_code == 400
    assert "rankine" in response.json()["detail"]
