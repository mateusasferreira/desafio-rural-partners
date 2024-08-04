from tabnanny import verbose
from xml.dom.minidom import DocumentType
from django.db import models

from utils.models import AbstractBaseModel
import validate_docbr
from django.core.exceptions import ValidationError


class EntityTypeOptions(models.TextChoices):
    INDIVIDUAL = "INDIVIDUAL", "Pessoa Física"
    COMPANY = "COMPANY", "Pessoa Jurídica"


class Producer(AbstractBaseModel):
    document = models.CharField("Documento", max_length=14)
    entity_type = models.CharField(
        "Tipo de Entidade",
        max_length=20,
        choices=EntityTypeOptions.choices,
        default=EntityTypeOptions.COMPANY,
    )
    name = models.CharField("Nome", max_length=50)

    def _validate_document(self):
        validator = validate_docbr.CNPJ

        if self.entity_type == EntityTypeOptions.INDIVIDUAL:
            validator = validate_docbr.CPF

        if not validator().validate(self.document):
            raise ValidationError("Documento Inválido")

    def clean(self):
        self._validate_document()

    class Meta:
        verbose_name = "Produtor Rural"
        verbose_name_plural = "Produtores Rurais"
        constraints = [
            models.UniqueConstraint(
                fields=["document", "entity_type"], name="unique_document_entity_type"
            )
        ]


class AgriculturalCulture(AbstractBaseModel):
    name = models.CharField("Nome", max_length=20)


class RuralProperty(AbstractBaseModel):
    name = models.CharField("Nome", max_length=50)
    city = models.CharField("Cidade", max_length=50)
    state = models.CharField("Estado", max_length=2)
    total_area_hectares = models.DecimalField(
        "Área total (hectares)", max_digits=10, decimal_places=2
    )
    arable_area_hectares = models.DecimalField(
        "Área Agricultável (hectares)", max_digits=10, decimal_places=2
    )
    vegetation_area_hectares = models.DecimalField(
        "Área de Vegetação (hectares)", max_digits=10, decimal_places=2
    )
    producer = models.ForeignKey(
        Producer, on_delete=models.CASCADE, related_name="rural_properties"
    )
    planted_cultures = models.ManyToManyField(
        AgriculturalCulture,
        related_name="properties",
        verbose_name="Culturas Plantadas",
    )
