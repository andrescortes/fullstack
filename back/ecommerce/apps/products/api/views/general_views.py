from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import (
    MeasureUnitSerializer,
    IndicatorSerializer,
    CategoryProductSerializer
)


class MeasureUnitListAPIView(GeneralListAPIView):
    """Product list view"""
    serializer_class = MeasureUnitSerializer


class IndicatorListAPIView(GeneralListAPIView):
    """Indicator list view"""
    serializer_class = IndicatorSerializer


class CategoryProductListAPIView(GeneralListAPIView):
    """Category list view"""
    serializer_class = CategoryProductSerializer
