from decimal import Decimal
import pytest
from apps.ruralpartners.models import (
    EntityTypeOptions,
    Producer,
    RuralProperty,
)
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_create_producer_success():
    producer = Producer(name="Foo Producer", document="00205164000155")

    producer.save()

    assert hasattr(producer, "id")


@pytest.mark.django_db
def test_create_producer_invalid_document():
    producer = Producer(name="Foo Producer", document="99999999999999")

    with pytest.raises(ValidationError, match="Documento Inválido"):
        producer.save()


@pytest.mark.django_db
def test_create_individual_producer_success():
    producer = Producer(
        name="Foo Producer",
        entity_type=EntityTypeOptions.INDIVIDUAL,
        document="15470343006",
    )

    producer.save()

    assert hasattr(producer, "id")


@pytest.mark.django_db
def test_create_individual_producer_invalid_document():
    producer = Producer(
        name="Foo Producer",
        entity_type=EntityTypeOptions.INDIVIDUAL,
        document="11111111111",
    )

    with pytest.raises(ValidationError, match="Documento Inválido"):
        producer.save()


@pytest.mark.django_db
def test_create_rural_property(producer):
    property = RuralProperty(
        name="Foo Property",
        producer=producer,
        city="Goiânia",
        state="GO",
        total_area_hectares=Decimal("100"),
        arable_area_hectares=Decimal("50"),
        vegetation_area_hectares=Decimal("50"),
    )

    property.save()

    assert hasattr(property, "id")


@pytest.mark.django_db
def test_create_rural_property_area_exceeding_error(producer):
    property = RuralProperty(
        name="Foo Property",
        producer=producer,
        city="Goiânia",
        state="GO",
        total_area_hectares=Decimal("100"),
        arable_area_hectares=Decimal("60"),
        vegetation_area_hectares=Decimal("50"),
    )

    with pytest.raises(
        ValidationError,
        match="A soma das áreas agricultável e de vegetação não deve ultrapassar a área total",
    ):
        property.save()


@pytest.mark.django_db
def test_rural_property_can_have_multiple_cultures(rural_property):
    rural_property.planted_cultures.create(name="soja")
    rural_property.planted_cultures.create(name="milho")

    assert rural_property.planted_cultures.count() == 2
