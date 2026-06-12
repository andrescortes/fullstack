from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    """Custom user auth for app"""

    def _create_user(
        self,
        username,
        email,
        name,
        last_name,
        password,
        is_staff,
        is_superuser,
        **extra_fields,
    ):
        user = self.model(
            name=name,
            username=username,
            email=email,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self.db)

    def create_user(self, username, email, name, last_name, **extra_fields):
        """Function to create an user"""
        return self._create_user(
            username, email, name, last_name, password=None, **extra_fields
        )

    def create_superuser(
        self, username, email, name, last_name, password=None, **extra_fields
    ):
        """Function to create a superuser"""
        return self._create_user(
            username, email, name, last_name, password, True, True, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model for the ecommerce application."""

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField("Email", max_length=255, unique=True)
    name = models.CharField("Name", max_length=255, blank=True, null=True)
    last_name = models.CharField("Lastname", max_length=255, blank=True, null=True)
    image = models.ImageField(
        "Image profile", upload_to="profile/", max_length=255, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        """Metadata for User class"""

        verbose_name = "User"
        verbose_name_plural = "Users"

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "name", "last_name"]

    def natural_key(self):
        return self.username

    def __str__(self):
        return f"User {self.username}, with name: {self.last_name} {self.name}"
