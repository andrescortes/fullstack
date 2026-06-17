from django.urls import path

from apps.products.api.views.general_views import (
    MeasureUnitListAPIView,
    IndicatorListAPIView,
    CategoryProductListAPIView
)

urlpatterns = [
    path('measure-units', MeasureUnitListAPIView.as_view(), name='measure-unit-list'),
    path('indicators', IndicatorListAPIView.as_view(), name='indicator-list'),
    path('category-products', CategoryProductListAPIView.as_view(), name='category-product-list'),
]