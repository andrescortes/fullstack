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

    def create(self, validated_data):
        """override function to create new user from serialized data"""

        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """override function to update existing user"""

        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    """User list serializer"""

    class Meta:
        """Metadata for User model"""
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            "id": data.get('id'),
            "username": data.get('username'),
            "email": data.get('email'),
            "name": data.get('name'),
            "isSuperUser": data.get('is_superuser'),
            "isStaff": data.get('is_staff'),
        }


class UserTestSerializer(serializers.Serializer):
    """User test serializer"""

    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):
        """Validate user name property"""
        if "developer" == value:
            raise serializers.ValidationError("Developer is keyword reserved")
        return value

    def validate(self, data):
        """function that validated all fields"""
        return data

    def create(self, validated_data):
        """override function to create new user from serialized data"""
        print(f"validated data: {validated_data}")
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """override function to update existing user"""
        print(f"instance: {instance}")
        print(f"validated_data: {validated_data}")
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
