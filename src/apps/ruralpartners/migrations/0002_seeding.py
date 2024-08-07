# Generated by Django 5.0.7 on 2024-08-07 22:32

from django.db import migrations

from apps.ruralpartners.models import AgriculturalCulture, Producer, RuralProperty


cultures = [{"name": "soja"}, {"name": "milho"}, {"name": "café"}]

producers = [
    {"name": "Produtor1", "document": "72354841000108"},
    {"name": "Produtor2", "entity_type": "INDIVIDUAL", "document": "36411236000168"},
]

rural_properties = [
    {
        "name": "GO1",
        "total_area_hectares": 100,
        "arable_area_hectares": 50,
        "vegetation_area_hectares": 50,
        "city": "Goiânia",
        "state": "GO",
    },
    {
        "name": "GO1",
        "total_area_hectares": 100,
        "arable_area_hectares": 75,
        "vegetation_area_hectares": 25,
        "city": "Goiânia",
        "state": "GO",
    },
    {
        "name": "GO1",
        "total_area_hectares": 100,
        "arable_area_hectares": 100,
        "vegetation_area_hectares": 0,
        "city": "São Paulo",
        "state": "SP",
    },
]


def forwards_func(*args):
    culture_instances = AgriculturalCulture.objects.bulk_create(
        [AgriculturalCulture(**data) for data in cultures]
    )
    producer_instances = Producer.objects.bulk_create(
        [Producer(**data) for data in producers]
    )

    property_1 = RuralProperty.objects.create(
        **rural_properties[0],
        producer=producer_instances[0],
    )
    property_1.planted_cultures.add(culture_instances[0])
    property_2 = RuralProperty.objects.create(
        **rural_properties[1],
        producer=producer_instances[0],
    )
    property_2.planted_cultures.add(*culture_instances[:1])
    property_2 = RuralProperty.objects.create(
        **rural_properties[2],
        producer=producer_instances[1],
    )
    property_2.planted_cultures.add(*culture_instances[1:])


def reverse_func(*args):
    RuralProperty.objects.delete()
    AgriculturalCulture.objects.delete()
    Producer.objects.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("ruralpartners", "0001_initial"),
    ]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
