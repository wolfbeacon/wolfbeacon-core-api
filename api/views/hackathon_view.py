from api.models.hackathon_model import Hackathon
from api.serializers.hackathon_serializer import HackathonSerializer
from rest_framework import generics
from api.services import hackathon_service
from rest_framework.response import Response
from rest_framework import status

"""
GET All Hackathons
POST Hackathon
"""


class HackathonListAndCreate(generics.ListCreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

    """
    Override post method in Generics to CREATE Hackathon
    """

    def post(self, request, *args, **kwargs):
        # Get User id
        serialized_hackathon = HackathonSerializer(data=request.data)

        # Create Hackathon while upserting user
        if serialized_hackathon.is_valid():
            user_id = serialized_hackathon.data.organiser_email_id
            hackathon_service.create_hackathon_upserting_user(serialized_hackathon, user_id)

            return Response(serialized_hackathon.data, status=status.HTTP_201_CREATED)

        return Response(serialized_hackathon.errors, status=status.HTTP_400_BAD_REQUEST)


# GET Hackathon
"""
@apiVersion 0.0.1
@api {get} /hackathon/:id Get Hackathon
@apiName GetHackathon
@apiGroup Hackathon

@apiParam {Number} id Hackathon unique ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Hackathon
"""
@apiVersion 0.0.1
@api {put} /hackathon/:id Update Hackathon
@apiName UpdateHackathon
@apiGroup Hackathon

@apiParam {Number} id Hackathon unique ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Hackathon
"""
@apiVersion 0.0.1
@api {put} /hackathon/:id Delete Hackathon
@apiName DeleteHackathon
@apiGroup Hackathon

@apiParam {Number} id Hackathon unique ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK

"""


class HackathonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
