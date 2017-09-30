from api.models.hackathon_member_model import Member
from api.serializers.member_serializer import MemberSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# POST Members
"""
@apiVersion 0.0.1
@api {post} /hackathons/:hackathon-id/members/ 1. Create Hackathon Member 
@apiName CreateHackathonMember
@apiGroup HackathonMembers
@apiParam {String} user_id User ID of Member
@apiParam {String} hackathon_id Hackathon Id Member is to attend
@apiParam {String="organiser","volunteer","participant","mentor"} role Role of Member in Hackathon
@apiParamExample {json} Request Data Example:
{"user_id":"github_12345","hackathon_id":"penapps_1","role":"organiser"}
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 201 Created
"""

# GET All Hackathon Members
"""
@apiVersion 0.0.1
@api {get} /hackathons/:hackathon-id/members/ 2. Get Hackathon Members 
@apiName GetAllMembersForHackathon
@apiGroup HackathonMembers
@apiParam {String} hackathon_id Hackathon Id Member is to attend
@apiSuccessExample {json} Sample Success Response
[{"hackathon_id":"penapps_1","user_id":"facebook_1133","role":"organiser"},{"hackathon_id":"bigreadhack_1","user_id":"github_1234","role":"volunteer"}]
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
        data['hackathon_id'] = hackathon_id

        # Create Membership
        serialized_member = MemberSerializer(data=data)
        if serialized_member.is_valid():
            serialized_member.save()

            return Response(serialized_member.data, status=status.HTTP_201_CREATED)

        return Response(serialized_member.errors, status=status.HTTP_400_BAD_REQUEST)


# GET Hackathon Member
"""
@apiVersion 0.0.1
@api {get} /hackathons/:hackathon-id/members/:user-id/ 3. Get Hackathon Member
@apiName GetHackathonMember
@apiGroup HackathonMembers
@apiParam {String} user_id User ID of Member
@apiParam {String} hackathon_id Hackathon Id Member is to attend
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Hackathon Member
"""
@apiVersion 0.0.1
@api {put} /hackathons/:hackathon-id/members/:user-id/ 4. Update Hackathon Member
@apiName UpdateHackathonMember
@apiGroup HackathonMembers
@apiParam {String} user_id User ID of Member
@apiParam {String} hackathon_id Hackathon Id Member is to attend
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Hackathon Member
"""
@apiVersion 0.0.1
@api {delete} /hackathons/:hackathon-id/members/:user-id/ 5. Delete Hackathon Member
@apiName DeleteHackathonMember
@apiGroup HackathonMembers
@apiParam {String} user_id User ID of Member
@apiParam {String} hackathon_id Hackathon Id Member is to attend
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
        data['hackathon_id'] = hackathon_id
        data['user_id'] = user_id

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
