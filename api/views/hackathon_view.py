from api.models.hackathon_member_model import Hackathon
from api.models.hackathon_member_model import Member
from api.serializers.hackathon_serializer import HackathonSerializer
from api.serializers.member_serializer import MemberSerializer
from api.services import hackathon_service
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# POST Hackathon
"""
@apiVersion 0.0.1
@api {post} /hackathons/ 1. Create Hackathon
@apiName CreateHackathon
@apiGroup Hackathons
@apiDescription NOTE: Schema to send is in 'Request Data Sample'
@apiParamExample {json} Request Data Example:
{
    "id": 1,
    "data": {
        "exampleHackathonData": {
            "Name": "Penapps"
        }
    }
}
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 201 OK
"""

# GET All Hackathons
"""
@apiVersion 0.0.1
@api {get} /hackathons/ 2. Get All Hackathons
@apiName GetAllHackathons
@apiGroup Hackathons
@apiParam {boolean} featured Returns featured hackathons for featured=true


@apiSuccessExample {json} Sample Success Response:
[
    {
        "id": 1,
        "data": {
            ...
        },
        "is_published": false
    },
    {
        "id": 5,
        "data": {
            ...
        },
        "is_published": false
    }
]
Success Response Code: HTTP/1.1 200 OK
"""


class HackathonListAndCreate(generics.ListCreateAPIView):
    """
    List All Hackathon, Create a new Hackathon

    Optional Parameters: featured=true
    """

    def get_queryset(self):
        queryset = Hackathon.objects.all()

        # Featured Hackathons
        featured = self.request.query_params.get('featured', None)
        if featured == 'true':
            queryset = hackathon_service.filter_featured_hackathons()

        return queryset

    serializer_class = HackathonSerializer


# GET Hackathon
"""
@apiVersion 0.0.1
@api {get} /hackathon/:id 3. Get Hackathon
@apiName GetHackathon
@apiGroup Hackathons
@apiParam {Number} id Hackathon unique ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Hackathon
"""
@apiVersion 0.0.1
@api {put} /hackathon/:id 4. Update Hackathon
@apiName UpdateHackathon
@apiGroup Hackathons
@apiParam {Number} id Hackathon unique ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Hackathon
"""
@apiVersion 0.0.1
@api {delete} /hackathon/:id 5. Delete Hackathon
@apiName DeleteHackathon
@apiGroup Hackathons
@apiParam {Number} id Hackathon unique ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class HackathonRUD(generics.RetrieveUpdateDestroyAPIView):
    """
    List a Hackathon, Update a Hackathon, Delete a Hackathon
    """
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


# POST Members
"""
@apiVersion 0.0.1
@api {post} /hackathons/:id 1. Create Hackathon Member 
@apiName CreateHackathonMember
@apiGroup HackathonMembers
@apiParam {Number} id Hackathon ID.
@apiParam {String} role O(Organiser)/ M (Mentor)/ P (Participant)/ V (Volunteer)
@apiParamExample {json} Request Data Example:
{
    "id": "github_12345",
    "role": "M"
}
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 201 Created
"""

# GET All Hackathon Members
"""
@apiVersion 0.0.1
@api {get} /hackathons/:id 2. Get Hackathon Members 
@apiName GetAllMembersForHackathon
@apiGroup HackathonMembers
@apiSuccessExample {json} Sample Success Response
[
    {
        "hackathon": 1,
        "member": "github_12345",
        "role": "P"
    },
    .
    .
    {
        "hackathon": 1,
        "member": "facebook_4342",
        "role": "M"
    }
]
Success Response Code: HTTP/1.1 200 OK
"""


class MemberListAndCreate(APIView):
    """
    List all Hackathon Members, Add a new Member to a Hackathon
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
@api {get} /hackathon/:id/members/:user-id 3. Get Hackathon Member
@apiName GetHackathonMember
@apiGroup HackathonMembers
@apiParam {Number} id Hackathon ID.
@apiParam {Number} user-id User ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Hackathon Member
"""
@apiVersion 0.0.1
@api {put} /hackathon/:id/members/:user-id 4. Update Hackathon
@apiName UpdateHackathonMember
@apiGroup HackathonMembers
@apiParam {Number} id Hackathon ID.
@apiParam {Number} user-id User ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Hackathon Member
"""
@apiVersion 0.0.1
@api {delete} /hackathon/:id 5. Delete Hackathon
@apiName DeleteHackathonMember
@apiGroup HackathonMembers
@apiParam {Number} id Hackathon ID.
@apiParam {Number} user-id User ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class MemberRUD(APIView):
    """
    List details for a Hackathon Member, Update a Hackathon Member, Delete a Hackathon Member
    """

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
