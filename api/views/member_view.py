from api.models import Member
from api.serializers import MemberSerializer

from rest_framework import mixins, generics

# POST Members
"""
@apiVersion 0.0.1
@api {post} /hackathons/:hackathon_id/members/ 1. Create Hackathon Member 
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
@api {get} /hackathons/:hackathon_id/members/ 2. Get Hackathon Members 
@apiName GetAllMembersForHackathon
@apiGroup HackathonMembers
@apiParam {String} hackathon_id Hackathon Id Member is to attend
@apiSuccessExample {json} Sample Success Response
[{"hackathon_id":"penapps_1","user_id":"facebook_1133","role":"organiser"},{"hackathon_id":"bigreadhack_1","user_id":"github_1234","role":"volunteer"}]
Success Response Code: HTTP/1.1 200 OK
"""


class MemberListAndCreate(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):
    """
    List All Users, Create a new Event
    """
    serializer_class = MemberSerializer

    # Custom queryset
    def get_queryset(self):
        # Get Hackathon id
        hackathon_id = self.kwargs['pk']

        # Filter for Hackathon's members
        queryset = Member.objects.filter(hackathon_id=hackathon_id)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Reinsert hackathon_id key for sanity
        request.data['hackathon_id'] = self.kwargs['pk']

        return self.create(request, *args, **kwargs)


# GET Hackathon Member
"""
@apiVersion 0.0.1
@api {get} /hackathons/:hackathon_id/members/:user_id/ 3. Get Hackathon Member
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
@api {put} /hackathons/:hackathon_id/members/:user_id/ 4. Update Hackathon Member
@apiName UpdateHackathonMember
@apiDescription Supports Partial Update
@apiGroup HackathonMembers
@apiParam {String} user_id User ID of Member
@apiParam {String} hackathon_id Hackathon Id Member is to attend
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Hackathon Member
"""
@apiVersion 0.0.1
@api {patch} /hackathons/:hackathon_id/members/:user_id/ 5. Partially Update Hackathon Member
@apiName PartiallyUpdateHackathonMember
@apiDescription Supports Partial Update
@apiGroup HackathonMembers
@apiParam {String} user_id User ID of Member
@apiParam {String} hackathon_id Hackathon Id Member is to attend
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Hackathon Member
"""
@apiVersion 0.0.1
@api {delete} /hackathons/:hackathon_id/members/:user_id/ 6. Delete Hackathon Member
@apiName DeleteHackathonMember
@apiGroup HackathonMembers
@apiParam {String} user_id User ID of Member
@apiParam {String} hackathon_id Hackathon Id Member is to attend
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class MemberRUD(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    """
    Get Visitor, Update Visitor, Delete Visitor
    """
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Re-Insert keys for sanity
        request.data['hackathon_id'] = self.kwargs['pk']
        request.data['user_id'] = self.kwargs['fk']

        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # Re-Insert keys for sanity
        request.data['hackathon_id'] = self.kwargs['pk']
        request.data['user_id'] = self.kwargs['fk']

        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
