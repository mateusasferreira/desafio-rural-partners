import pytest


@pytest.mark.django_db
def test_update_producers_success(api_client_authorized, producer):
    response = api_client_authorized.put(
        f"/api/v1/producers/{producer.pk}/",
        data={"name": "Foo", "document": "95789873000131"},
        format="json",
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_update_producers_invalid_document(api_client_authorized, producer):
    response = api_client_authorized.put(
        f"/api/v1/producers/{producer.pk}/",
        data={"name": "Foo", "document": "99999999999999"},
        format="json",
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_update_producers_not_found_error(api_client_authorized):
    response = api_client_authorized.put(
        "/api/v1/producers/999/",
        data={"name": "Foo", "document": "99999999999999"},
        format="json",
    )

    assert response.status_code == 404
