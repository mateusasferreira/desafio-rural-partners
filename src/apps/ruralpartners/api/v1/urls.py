from rest_framework import routers

from apps.ruralpartners.api.v1 import views

rural_partners_router = routers.SimpleRouter()
rural_partners_router.register(r"producers", views.ProducerViewSet)
rural_partners_router.register(r"rural_properties", views.RuralPropertyViewSet)
rural_partners_router.register(
    r"agricultural_cultures", views.AgriculturalCultureViewSet
)
