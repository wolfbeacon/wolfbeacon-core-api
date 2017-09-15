from api.models.user_model import User
from api.serializers.user_serializer import UserSerializer
from rest_framework import mixins
from rest_framework import generics


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

