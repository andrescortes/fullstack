from django.urls import path

from apps.users.api.api import user_api_view, user_detail_api_view

urlpatterns = [
    path("users", user_api_view, name="user_api"),
    path("users/<int:pk>", user_detail_api_view, name="user_api_detail"),
]
