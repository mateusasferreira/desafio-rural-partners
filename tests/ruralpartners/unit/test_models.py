import pytest
from apps.ruralpartners.models import EntityTypeOptions, Producer
from django.core.exceptions import ValidationError


@pytest.mark.django_db
def test_create_producer_success():
    producer = Producer(name="Foo Producer", document="00205164000155")

    producer.full_clean()
    producer.save()

    assert hasattr(producer, "id")


@pytest.mark.django_db
def test_create_producer_invalid_document():
    producer = Producer(name="Foo Producer", document="99999999999999")

    with pytest.raises(ValidationError, match="Documento Inválido"):
        producer.full_clean()


@pytest.mark.django_db
def test_create_individual_producer_success():
    producer = Producer(
        name="Foo Producer",
        entity_type=EntityTypeOptions.INDIVIDUAL,
        document="15470343006",
    )

    producer.full_clean()
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
        producer.full_clean()
