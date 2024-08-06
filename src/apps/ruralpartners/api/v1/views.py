from email.policy import default
from rest_framework import viewsets, permissions, views, generics
from rest_framework.response import Response
from apps.ruralpartners.api.v1.serializers import (
    AgriculturalCultureSerializer,
    ProducerSerializer,
    RuralPropertyDetailSerializer,
    RuralPropertySerializer,
)
from apps.ruralpartners.models import AgriculturalCulture, Producer, RuralProperty
from django.db.models import Sum, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Round


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


class StatsView(views.APIView):
    def get(self, *args):
        states_count = RuralProperty.objects.values("state").annotate(total=Count("id"))
        cultures_count = AgriculturalCulture.objects.values("name").annotate(
            total_properties=Count("properties")
        )

        percentage_arable_area_expression = Round(
            ExpressionWrapper(
                (Sum("arable_area_hectares") / Sum("total_area_hectares")) * 100,
                output_field=DecimalField(),
            ),
            2,
        )
        percentage_vegetation_area_expression = Round(
            ExpressionWrapper(
                (Sum("vegetation_area_hectares") / Sum("total_area_hectares")) * 100,
                output_field=DecimalField(),
            ),
            2,
        )

        rural_property_stats = RuralProperty.objects.aggregate(
            total_area=Sum("total_area_hectares", default=0),
            total_properties=Count("id"),
            percentage_arable_area=percentage_arable_area_expression,
            percentage_vegetation_area=percentage_vegetation_area_expression,
        )

        return Response(
            {
                # "rural_property_stats": rural_property_stats,
                **rural_property_stats,
                "states_count": states_count,
                "cultures_count": cultures_count,
            }
        )
