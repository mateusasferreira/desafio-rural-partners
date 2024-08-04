# Generated by Django 5.0.7 on 2024-08-04 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AgriculturalCulture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
                ),
                ("name", models.CharField(max_length=20, verbose_name="Nome")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Producer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
                ),
                ("document", models.CharField(max_length=14, verbose_name="Documento")),
                (
                    "entity_type",
                    models.CharField(
                        choices=[
                            ("INDIVIDUAL", "Pessoa Física"),
                            ("COMPANY", "Pessoa Jurídica"),
                        ],
                        default="COMPANY",
                        max_length=20,
                        verbose_name="Tipo de Entidade",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Nome")),
            ],
            options={
                "verbose_name": "Produtor Rural",
                "verbose_name_plural": "Produtores Rurais",
            },
        ),
        migrations.CreateModel(
            name="RuralProperty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Atualizado em"),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Nome")),
                ("city", models.CharField(max_length=50, verbose_name="Cidade")),
                ("state", models.CharField(max_length=2, verbose_name="Estado")),
                (
                    "total_area_hectares",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Área total (hectares)",
                    ),
                ),
                (
                    "arable_area_hectares",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Área Agricultável (hectares)",
                    ),
                ),
                (
                    "vegetation_area_hectares",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Área de Vegetação (hectares)",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddConstraint(
            model_name="producer",
            constraint=models.UniqueConstraint(
                fields=("document", "entity_type"), name="unique_document_entity_type"
            ),
        ),
        migrations.AddField(
            model_name="ruralproperty",
            name="planted_cultures",
            field=models.ManyToManyField(
                related_name="properties",
                to="ruralpartners.agriculturalculture",
                verbose_name="Culturas Plantadas",
            ),
        ),
        migrations.AddField(
            model_name="ruralproperty",
            name="producer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rural_properties",
                to="ruralpartners.producer",
            ),
        ),
    ]
