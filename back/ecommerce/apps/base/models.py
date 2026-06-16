from django.db import models


class BaseModel(models.Model):
    """Model definition for BaseModel."""

    id = models.AutoField(primary_key=True)
    state = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)
    deleted_date = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'
