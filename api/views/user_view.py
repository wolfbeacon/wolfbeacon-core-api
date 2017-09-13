from api.models.user_model import User
from api.serializers.user_serializer import UserSerializer
from rest_framework import mixins
from rest_framework import generics


# POST User
"""
@apiVersion 0.0.1
@api {post} /users/ 1. Create User
@apiName CreateUser
@ApiGroup Users
@apiParamExample {json} Request Data Example:
{
    "id": "github_12345"
}

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
@api {get} /users/:id 2. Get User
@apiName GetUser
@ApiGroup Users

@apiParam {Number} id User ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT User
"""
@apiVersion 0.0.1
@api {put} /users/:id 3. Update User
@apiName UpdateUser
@ApiGroup Users

@apiParam {Number} id User ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE User
"""
@apiVersion 0.0.1
@api {delete} /User/:id 4. Delete User
@apiName DeleteUser
@ApiGroup Users

@apiParam {Number} id User ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT

"""


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

