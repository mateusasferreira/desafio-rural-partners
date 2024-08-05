import pytest


@pytest.mark.django_db
def test_delete_producers_success(api_client_authorized, producer):
    response = api_client_authorized.delete(f"/api/v1/producers/{producer.pk}/")

    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_producers_not_found_error(api_client_authorized):
    response = api_client_authorized.delete("/api/v1/producers/999/")

    assert response.status_code == 404
