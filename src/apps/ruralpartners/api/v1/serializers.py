from rest_framework import serializers

from apps.ruralpartners.models import AgriculturalCulture, Producer, RuralProperty


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"


class AgriculturalCultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriculturalCulture
        fields = ["id", "name"]


class RuralPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = RuralProperty
        fields = "__all__"


class RuralPropertyDetailSerializer(RuralPropertySerializer):
    planted_cultures = AgriculturalCultureSerializer(many=True)
