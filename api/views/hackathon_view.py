from api.models.hackathon_member_model import Hackathon
from api.models.hackathon_member_model import Member
from api.serializers.hackathon_serializer import HackathonSerializer
from api.serializers.member_serializer import MemberSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# GET All Hackathons
"""
@apiVersion 0.0.1
@api {get} /hackathons/ Get All Hackathons
@apiName GetAllHackathons
@ApiGroup Hackathons

@apiParam {filter=featured} Gets Featured Hackathons

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# POST Hackathon
"""
@apiVersion 0.0.1
@api {get} /hackathons/ Get All Hackathons
@apiName CreateHackathon
@ApiGroup Hackathons

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 201 OK
"""


class HackathonListAndCreate(generics.ListCreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


# GET Hackathon
"""
@apiVersion 0.0.1
@api {get} /hackathon/:id Get Hackathon
@apiName GetHackathon
@ApiGroup Hackathons

@apiParam {Number} id Hackathon unique ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Hackathon
"""
@apiVersion 0.0.1
@api {put} /hackathon/:id Update Hackathon
@apiName UpdateHackathon
@ApiGroup Hackathons

@apiParam {Number} id Hackathon unique ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Hackathon
"""
@apiVersion 0.0.1
@api {put} /hackathon/:id Delete Hackathon
@apiName DeleteHackathon
@ApiGroup Hackathons

@apiParam {Number} id Hackathon unique ID.

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT

"""


class HackathonRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


# GET All Hackathon Members
"""
@apiVersion 0.0.1
@api {get} /hackathons/ Get All Hackathons
@apiName GetAllMembersForHackathon
@ApiGroup HackathonMembers

@apiParam {role=o/p/m/v} Gets Organisers/Participants/Mentor/Volunteers

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# POST Members
"""
@apiVersion 0.0.1
@api {get} /hackathons/ Get All Hackathons
@apiName CreateHackathonMember
@ApiGroup HackathonMembers

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 201 Created
"""


class MemberListAndCreate(APIView):
    """
    List all hackathons, or create a new hackathon.
    """

    def get(self, request, *args, **kwargs):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Get hackathon key from request
        hackathon_id = self.kwargs['pk']

        # Append Hackathon Id to data
        data = request.data
        data['hackathon'] = hackathon_id

        # Create Membership
        serialized_member = MemberSerializer(data=data)
        if serialized_member.is_valid():
            serialized_member.save()

            return Response(serialized_member.data, status=status.HTTP_201_CREATED)

        return Response(serialized_member.errors, status=status.HTTP_400_BAD_REQUEST)


# GET Hackathon Member
"""
@apiVersion 0.0.1
@api {get} /hackathon/:id Get Hackathon Member
@apiName GetHackathonMember
@ApiGroup HackathonMembers

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Hackathon Member
"""
@apiVersion 0.0.1
@api {put} /hackathon/:id Update Hackathon
@apiName UpdateHackathonMember
@ApiGroup HackathonMembers

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Hackathon Member
"""
@apiVersion 0.0.1
@api {put} /hackathon/:id Delete Hackathon
@apiName DeleteHackathonMember
@ApiGroup HackathonMembers


@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT

"""


class MemberRUD(APIView):
    def get_object(self, hackathon_id, user_id):
        try:
            return Member.objects.get(hackathon=hackathon_id, member=user_id)

        except Member.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        # Get Member
        hackathon_id = self.kwargs['pk']
        user_id = self.kwargs['fk']
        member = self.get_object(hackathon_id, user_id)

        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        # Get Member
        hackathon_id = self.kwargs['pk']
        user_id = self.kwargs['fk']
        member = self.get_object(hackathon_id, user_id)

        # Add hackathon and member details to data
        data = request.data
        data['hackathon'] = hackathon_id
        data['member'] = user_id

        serializer = MemberSerializer(member, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        # Get Member
        hackathon_id = self.kwargs['pk']
        user_id = self.kwargs['fk']
        member = self.get_object(hackathon_id, user_id)

        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
