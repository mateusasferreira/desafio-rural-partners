from rest_framework import viewsets, permissions

from apps.ruralpartners.api.v1.serializers import (
    AgriculturalCultureSerializer,
    ProducerSerializer,
    RuralPropertyDetailSerializer,
    RuralPropertySerializer,
)
from apps.ruralpartners.models import AgriculturalCulture, Producer, RuralProperty


class ProducerViewSet(viewsets.ModelViewSet):
    serializer_class = ProducerSerializer
    queryset = Producer.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class AgriculturalCultureViewSet(viewsets.ModelViewSet):
    serializer_class = AgriculturalCultureSerializer
    queryset = AgriculturalCulture.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class RuralPropertyViewSet(viewsets.ModelViewSet):
    queryset = RuralProperty.objects.prefetch_related("planted_cultures").all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RuralPropertyDetailSerializer
        return RuralPropertySerializer
