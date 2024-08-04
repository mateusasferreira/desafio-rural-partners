from rest_framework import routers

from apps.ruralpartners.api.v1.views import ProducerViewSet

rural_partners_router = routers.SimpleRouter()
rural_partners_router.register(r"producers", ProducerViewSet)
