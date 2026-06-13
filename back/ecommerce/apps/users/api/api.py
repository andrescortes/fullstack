from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.api.serializers import UserSerializer
from apps.users.models import User


class UserAPIView(APIView):
    """Entrypoint for users"""

    def get(self, request):
        """
        Retrieve all users
        """
        print(f"request: {request}")
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        if user_serializer.data is None:
            return Response(data=None, status=204)
        return Response(data=user_serializer.data, status=200)
