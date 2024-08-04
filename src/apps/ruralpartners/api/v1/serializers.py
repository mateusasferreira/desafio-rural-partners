from rest_framework import serializers

from apps.ruralpartners.models import Producer


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ["id", "name", "document", "entity_type"]
