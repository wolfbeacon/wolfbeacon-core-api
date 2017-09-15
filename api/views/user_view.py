from api.models.user_model import User
from api.serializers.user_serializer import UserSerializer
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import generics
from api.services import user_service
from rest_framework.response import Response

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
    """
    Create a new User
    """
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
@api {delete} /user/:id 4. Delete User
@apiName DeleteUser
@ApiGroup Users
@apiParam {Number} id User ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List details for a User, Update a User, Delete a User
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


# GET User
"""
@apiVersion 0.0.1
@api {get} /users/:id/hackathons 5. Get all User Hackathons
@apiName GetUserHackathons
@ApiGroup Users
@apiParam {Number} id User ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""


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
