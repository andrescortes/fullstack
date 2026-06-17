from rest_framework import serializers

from apps.products.models import MeasureUnit, CategoryProduct, Indicator


class IndicatorSerializer(serializers.ModelSerializer):
    """Indicator Serializer"""

    class Meta:
        """Meta class"""
        model = Indicator
        exclude = ('state',)


class CategoryProductSerializer(serializers.ModelSerializer):
    """Category Product Serializer"""

    class Meta:
        """Meta class"""
        model = CategoryProduct
        exclude = ('state',)


class MeasureUnitSerializer(serializers.ModelSerializer):
    """Measure Unit Serializer"""

    class Meta:
        """Meta class"""
        model = MeasureUnit
        exclude = ('state',)
