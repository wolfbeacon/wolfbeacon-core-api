from api.models.user_model import User
from api.serializers.user_serializer import UserSerializer
from rest_framework import mixins
from rest_framework import generics


# POST User
"""
@apiVersion 0.0.1
@api {get} /Users/:id Create User
@apiName CreateUser
@ApiGroup Users

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 201 Created
"""


class UserCreate(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# GET User
"""
@apiVersion 0.0.1
@api {get} /Users/:id Get User
@apiName GetUser
@ApiGroup Users

@apiParam {Number} id User unique ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT User
"""
@apiVersion 0.0.1
@api {put} /User/:id Update User
@apiName UpdateUser
@ApiGroup Users

@apiParam {Number} id User unique ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE User
"""
@apiVersion 0.0.1
@api {put} /User/:id Delete User
@apiName DeleteUser
@ApiGroup Users

@apiParam {Number} id User unique ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT

"""


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

