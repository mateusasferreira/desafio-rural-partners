import pytest

from apps.ruralpartners.models import Producer


@pytest.fixture
def producer():
    return Producer.objects.create(name="Foo Producer", document="00205164000155")
