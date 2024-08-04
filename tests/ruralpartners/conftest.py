from decimal import Decimal
import pytest

from apps.ruralpartners.models import Producer, RuralProperty


@pytest.fixture
def producer():
    return Producer.objects.create(name="Foo Producer", document="00205164000155")


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
