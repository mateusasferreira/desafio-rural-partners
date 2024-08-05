import pytest


@pytest.mark.django_db
def test_list_rural_properties_success(api_client_authorized, rural_property):
    response = api_client_authorized.get("/api/v1/rural_properties/")

    assert response.status_code == 200
    assert response.json()["count"] == 1


@pytest.mark.django_db
def test_get_rural_property_details_success(api_client_authorized, rural_property):
    response = api_client_authorized.get(
        f"/api/v1/rural_properties/{rural_property.pk}/"
    )

    assert response.status_code == 200
    assert response.json()["id"] == rural_property.pk


@pytest.mark.django_db
def test_get_rural_property_details_not_found(api_client_authorized):
    response = api_client_authorized.get(f"/api/v1/rural_properties/999/")

    assert response.status_code == 404
