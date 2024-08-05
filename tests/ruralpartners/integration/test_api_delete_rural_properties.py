import pytest


@pytest.mark.django_db
def test_delete_rural_property_success(api_client_authorized, rural_property):
    response = api_client_authorized.delete(
        f"/api/v1/rural_properties/{rural_property.pk}/"
    )

    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_rural_property_not_found_error(api_client_authorized):
    response = api_client_authorized.delete("/api/v1/rural_properties/999/")

    assert response.status_code == 404
