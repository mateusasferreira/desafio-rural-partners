import pytest


@pytest.mark.django_db
def test_list_producers_success(api_client_authorized, producer):
    response = api_client_authorized.get("/api/v1/producers/")

    assert response.status_code == 200
    assert response.json()["count"] == 1


@pytest.mark.django_db
def test_get_producer_details_success(api_client_authorized, producer):
    response = api_client_authorized.get(f"/api/v1/producers/{producer.pk}/")

    assert response.status_code == 200
    assert response.json()["id"] == producer.pk
