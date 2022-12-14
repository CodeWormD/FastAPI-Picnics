from fastapi.testclient import TestClient
from sqlalchemy.orm import Session 
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


city1 = {
    'name': 'Санкт-Петербург'
}


def test_post_city(client):
    response = client.post('/api/v1/city/create/', json=city1)
    assert response.status_code == 200


def test_get_city(client):
    response = client.get('/api/v1/city/?name=Санкт-Петербург')
    assert response.status_code == 200
    assert response.json()['name'] == 'Санкт-Петербург'