from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel


class MeasureUnit(BaseModel):
    """Measure Unit Model"""
    description = models.CharField(max_length=50, blank=False, null=False, unique=True)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'MeasureUnit'
        verbose_name_plural = 'MeasureUnits'

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):
    """Category Product Model"""

    description = models.CharField(max_length=50, blank=False, null=False, unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'CategoryProduct'
        verbose_name_plural = 'CategoryProducts'

    def __str__(self):
        return self.description


class Indicator(BaseModel):
    """Discount for a product"""

    discount = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=50, blank=False, null=False, unique=True, verbose_name="discount")
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicators'

    def __str__(self):
        return f"Discount of the category {self.description}: {self.discount}%"


class Product(BaseModel):
    """Product Model"""

    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    description = models.CharField(max_length=50, blank=False, null=False)
    img = models.ImageField(upload_to="products/", blank=True, null=True)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicators'

    def __str__(self):
        return f"Discount of the category {self.description}: {self.discount}%"
