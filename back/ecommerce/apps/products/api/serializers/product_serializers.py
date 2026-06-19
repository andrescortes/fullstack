from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""

    class Meta:
        """Meta class"""
        model = Product
        exclude = ('state', 'created_date', 'updated_date', 'deleted_date')
