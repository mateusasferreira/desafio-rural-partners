import pytest


@pytest.mark.django_db
def test_patch_rural_property_success(api_client_authorized, rural_property):
    response = api_client_authorized.patch(
        f"/api/v1/rural_properties/{rural_property.pk}/",
        data={"name": "Fazenda Foo"},
        format="json",
    )
    # breakpoint()
    assert response.status_code == 200


@pytest.mark.django_db
def test_patch_rural_property_invalid_area(api_client_authorized, rural_property):
    response = api_client_authorized.patch(
        f"/api/v1/rural_properties/{rural_property.pk}/",
        data={"arable_area_hectares": 99999999},
        format="json",
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_patch_rural_property_not_found_error(api_client_authorized):
    response = api_client_authorized.patch(
        "/api/v1/rural_properties/999/",
        data={"name": "Fazenda Foo"},
        format="json",
    )

    assert response.status_code == 404


@pytest.mark.django_db
def test_put_rural_property_success(api_client_authorized, rural_property, soy_culture):
    response = api_client_authorized.put(
        f"/api/v1/rural_properties/{rural_property.pk}/",
        data={
            "producer": rural_property.producer.pk,
            "name": "fazenda foo",
            "state": "SP",
            "city": "Foo",
            "total_area_hectares": 10000,
            "arable_area_hectares": 5000,
            "vegetation_area_hectares": 5000,
            "planted_cultures": [soy_culture.pk],
        },
        format="json",
    )
    # breakpoint()
    assert response.status_code == 200
