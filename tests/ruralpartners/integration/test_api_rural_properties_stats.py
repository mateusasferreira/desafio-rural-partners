import pytest


@pytest.mark.django_db
def test_rural_properties_stats_endpoint(
    api_client_authorized, rural_property, second_rural_property, third_rural_property
):
    response = api_client_authorized.get("/api/v1/rural_properties/stats/")

    assert response.status_code == 200
    assert response.json() == {
        "total_property_area": 300.0,
        "total_arable_area": 175.0,
        "total_vegetation_area": 125.0,
        "total_properties": 3,
        "states_count": [{"state": "GO", "total": 2}, {"state": "SP", "total": 1}],
        "cultures_count": [
            {"name": "coffee", "total_properties": 1},
            {"name": "corn", "total_properties": 2},
            {"name": "soy", "total_properties": 1},
        ],
    }
