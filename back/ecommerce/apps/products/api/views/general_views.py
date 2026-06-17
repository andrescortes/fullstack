from rest_framework import generics

from apps.products.api.serializers.general_serializers import (
    MeasureUnitSerializer,
    IndicatorSerializer,
    CategoryProductSerializer
)
from apps.products.models import MeasureUnit, Indicator, CategoryProduct


class MeasureUnitListAPIView(generics.ListAPIView):
    """Product list view"""
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        """Return all measure units by active"""
        qs = MeasureUnit.objects.filter(state=True)
        return qs


class IndicatorListAPIView(generics.ListAPIView):
    """Indicator list view"""
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        """Return all indicator by active"""
        qs = Indicator.objects.filter(state=True)
        return qs


class CategoryProductListAPIView(generics.ListAPIView):
    """Category list view"""
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        """Return all category product by active"""
        qs = CategoryProduct.objects.filter(state=True)
        return qs
