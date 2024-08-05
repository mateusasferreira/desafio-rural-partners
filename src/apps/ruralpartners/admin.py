from django.contrib import admin

from apps.ruralpartners.models import AgriculturalCulture, Producer, RuralProperty


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    pass


@admin.register(RuralProperty)
class RuralPropertyAdmin(admin.ModelAdmin):
    pass


@admin.register(AgriculturalCulture)
class AgriculturalCultureAdmin(admin.ModelAdmin):
    pass
