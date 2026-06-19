from apps.base.api import GeneralListAPIView
from apps.products.models import Product
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(GeneralListAPIView):
    """Product list view"""
    serializer_class = ProductSerializer