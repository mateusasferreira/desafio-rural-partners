from rest_framework import viewsets, permissions

from apps.ruralpartners.api.v1.serializers import ProducerSerializer
from apps.ruralpartners.models import Producer


class ProducerViewSet(viewsets.ModelViewSet):
    serializer_class = ProducerSerializer
    queryset = Producer.objects.all()
    permission_classes = [permissions.IsAuthenticated]
