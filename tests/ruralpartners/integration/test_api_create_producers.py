import pytest


@pytest.mark.django_db
def test_create_producers_unauthorized(api_client):
    response = api_client.post(
        "/api/v1/producers/",
        data={"name": "Foo", "document": "00205164000155"},
        format="json",
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_create_producers_success(api_client_authorized):
    response = api_client_authorized.post(
        "/api/v1/producers/",
        data={"name": "Foo", "document": "00205164000155"},
        format="json",
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_create_producers_invalid_document(api_client_authorized):
    response = api_client_authorized.post(
        "/api/v1/producers/",
        data={"name": "Foo", "document": "99999999999999"},
        format="json",
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_individual_producer_success(api_client_authorized):
    response = api_client_authorized.post(
        "/api/v1/producers/",
        data={"name": "Foo", "entity_type": "INDIVIDUAL", "document": "15470343006"},
        format="json",
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_create_individual_producer_success(api_client_authorized):
    response = api_client_authorized.post(
        "/api/v1/producers/",
        data={"name": "Foo", "entity_type": "INDIVIDUAL", "document": "11111111111"},
        format="json",
    )

    assert response.status_code == 400
