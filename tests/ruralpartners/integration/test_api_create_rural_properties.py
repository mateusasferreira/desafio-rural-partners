import pytest


@pytest.mark.django_db
def test_create_rural_property_unauthorized(api_client, producer):
    response = api_client.post(
        "/api/v1/rural_properties/",
        data={
            "producer": producer.pk,
            "name": "fazenda foo",
            "state": "SP",
            "city": "Foo",
            "total_area_hectares": 100,
            "arable_area_hectares": 50,
            "vegetation_area_hectares": 50,
        },
        format="json",
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_create_rural_property_success(api_client_authorized, producer):
    response = api_client_authorized.post(
        "/api/v1/rural_properties/",
        data={
            "producer": producer.pk,
            "name": "fazenda foo",
            "state": "SP",
            "city": "Foo",
            "total_area_hectares": 100,
            "arable_area_hectares": 50,
            "vegetation_area_hectares": 50,
        },
        format="json",
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_create_rural_property_with_cultures_success(
    api_client_authorized, producer, soy_culture, corn_culture
):
    response = api_client_authorized.post(
        "/api/v1/rural_properties/",
        data={
            "producer": producer.pk,
            "name": "fazenda foo",
            "state": "SP",
            "city": "Foo",
            "total_area_hectares": 100,
            "arable_area_hectares": 50,
            "vegetation_area_hectares": 50,
            "planted_cultures": [soy_culture.pk, corn_culture.pk],
        },
        format="json",
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_create_rural_property_invalid_area_error(api_client_authorized, producer):
    response = api_client_authorized.post(
        "/api/v1/rural_properties/",
        data={
            "producer": producer.pk,
            "name": "fazenda foo",
            "state": "SP",
            "city": "Foo",
            "total_area_hectares": 100,
            "arable_area_hectares": 60,
            "vegetation_area_hectares": 50,
        },
        format="json",
    )

    assert response.status_code == 400
