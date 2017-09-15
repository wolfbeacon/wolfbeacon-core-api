from api.models.user_model import User
from api.serializers.user_serializer import UserSerializer
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import generics
from api.services import user_service
from rest_framework.response import Response


# POST User

class UserCreate(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    """
    Create a new User
    """
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List details for a User, Update a User, Delete a User
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserHackathons(APIView):
    """
    List All Hackathons User is a part of
    """

    def get(self, request, *args, **kwargs):
        # Get user id
        user_id = self.kwargs['pk']

        # Fetch and return user hackathons
        user_hackathons = user_service.get_user_hackathons(user_id)
        return Response(user_hackathons)
