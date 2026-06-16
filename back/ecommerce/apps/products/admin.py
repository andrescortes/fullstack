from django.contrib import admin

from apps.products.models import Product, CategoryProduct, MeasureUnit, Indicator

# Register your models here.
admin.site.register(MeasureUnit)
admin.site.register(CategoryProduct)
admin.site.register(Indicator)
admin.site.register(Product)
