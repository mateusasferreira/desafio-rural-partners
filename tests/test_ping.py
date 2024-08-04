from rest_framework.test import APIClient


def test_ping():
    client = APIClient()

    response = client.get("/ping")

    assert response.status_code == 200
    assert response.content == b"pong"
