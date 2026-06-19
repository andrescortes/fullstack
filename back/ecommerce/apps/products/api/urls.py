from django.urls import path

from apps.products.api.views.general_views import (
    MeasureUnitListAPIView,
    IndicatorListAPIView,
    CategoryProductListAPIView
)
from apps.products.api.views.product_view import ProductListAPIView

urlpatterns = [
    path('products', ProductListAPIView.as_view(), name='product-list'),
    path('products/measure-units', MeasureUnitListAPIView.as_view(), name='measure-unit-list'),
    path('products/indicators', IndicatorListAPIView.as_view(), name='indicator-list'),
    path('products/category-products', CategoryProductListAPIView.as_view(), name='category-product-list'),
]
