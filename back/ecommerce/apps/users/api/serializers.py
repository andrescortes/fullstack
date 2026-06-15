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


class UserTestSerializer(serializers.Serializer):
    """User test serializer"""

    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):
        if "developer" == value:
            raise serializers.ValidationError("Developer is keyword reserved")
        return value

    def validate(self, data):
        return data

    def create(self, validated_data):
        print(f"validated data: {validated_data}")
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(f"instance: {instance}")
        print(f"validated_data: {validated_data}")
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
