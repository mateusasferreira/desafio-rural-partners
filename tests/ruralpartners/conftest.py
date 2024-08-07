from decimal import Decimal
from ssl import SO_TYPE
import pytest

from apps.ruralpartners.models import AgriculturalCulture, Producer, RuralProperty


@pytest.fixture
def producer():
    return Producer.objects.create(name="Foo Producer", document="00205164000155")


@pytest.fixture
def soy_culture():
    return AgriculturalCulture.objects.create(name="soy")


@pytest.fixture
def corn_culture():
    return AgriculturalCulture.objects.create(name="corn")


@pytest.fixture
def coffe_culture():
    return AgriculturalCulture.objects.create(name="coffee")


@pytest.fixture
def rural_property(producer):
    return RuralProperty.objects.create(
        name="Foo Property",
        producer=producer,
        city="Goiânia",
        state="GO",
        total_area_hectares=Decimal("100"),
        arable_area_hectares=Decimal("50"),
        vegetation_area_hectares=Decimal("50"),
    )


@pytest.fixture
def second_rural_property(producer, soy_culture, corn_culture):
    instance = RuralProperty.objects.create(
        name="Bar Property",
        producer=producer,
        city="Goiânia",
        state="GO",
        total_area_hectares=Decimal("100"),
        arable_area_hectares=Decimal("50"),
        vegetation_area_hectares=Decimal("50"),
    )
    instance.planted_cultures.add(soy_culture)
    instance.planted_cultures.add(corn_culture)
    return instance


@pytest.fixture
def third_rural_property(producer, corn_culture, coffe_culture):
    instance = RuralProperty.objects.create(
        name="Baz Property",
        producer=producer,
        city="São Paulo",
        state="SP",
        total_area_hectares=Decimal("100"),
        arable_area_hectares=Decimal("75"),
        vegetation_area_hectares=Decimal("25"),
    )
    instance.planted_cultures.add(corn_culture)
    instance.planted_cultures.add(coffe_culture)
    return instance
