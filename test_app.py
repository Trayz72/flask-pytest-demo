import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.data == b"Automated Testing!"

def test_add(client):
    response = client.get("/add/2/3")
    assert response.data == b"5"
