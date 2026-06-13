from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""

    class Meta:
        """Metadata for User model"""

        model = User
        # fields = [
        #     "username",
        #     "email",
        #     "name",
        #     "last_name",
        #     "image",
        #     "is_active",
        #     "is_staff",
        #     # "historical",
        #     "objects",
        # ]
        fields = '__all__'
