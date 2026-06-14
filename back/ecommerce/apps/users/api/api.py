from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from apps.users.api.serializers import UserSerializer
from apps.users.models import User


@api_view(["GET", "POST"])
def user_api_view(request: Request):
    """Entrypoint for users based on function"""

    method = request.method
    if method == "GET":
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        if user_serializer.data is None:
            return Response(data=None, status=204)
        return Response(data=user_serializer.data, status=200)

    if method == "POST":
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid() is False:
            return Response(data=user_serializer.errors, status=400)

        user_serializer.save()
        data = user_serializer.data
        return Response(data=data, status=201)


@api_view(["GET", "PUT", "DELETE"])
def user_detail_api_view(req: Request, pk: int):
    """Retrieve, update and delete an user by id"""

    method = req.method
    methods = ["GET", "PUT", "DELETE"]
    if method not in methods:
        message = {"error": f"Method {method} no allowed"}
        return Response(data=message, status=405)

    if pk is None or pk == 0:
        message = {"error": "UserId is mandatory"}
        return Response(data=message, status=400)

    user = User.objects.filter(id=pk).first()
    if user is None:
        message = {"error": f"User not found with id: {pk}"}
        return Response(data=message, status=404)

    if method == "GET":
        user_serializer = UserSerializer(user, many=False)
        return Response(data=user_serializer.data, status=200)

    if method == "PUT":
        user_serializer = UserSerializer(user, data=req.data)
        if user_serializer.is_valid() is False:
            return Response(data={"error": UserSerializer.errors}, status=400)

        user_serializer.save()
        return Response(data=user_serializer.data, status=200)

    if method == "DELETE":
        user.delete()
        return Response(data={"message": f"User with id: {pk} was deleted"}, status=204)
