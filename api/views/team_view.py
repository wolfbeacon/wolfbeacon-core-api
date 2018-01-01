from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from api.models import Team, Hacker
from api.serializers import TeamSerializer

# POST Teams
"""
@apiVersion 1.0.0
@api {post} /hackathons/:hackathon-id/teams/ 1. Create Team 
@apiName CreateTeam
@apiDescription Teams are a part of Hackathons
@apiGroup Teams

@apiParam {Integer} hackathon ID of Hackathon this Team is a part of
@apiParam {Integer} owner_hacker ID of Hacker who created this team, who is the team owner by default
@apiParam {String{35 chars}} name Name of Team
@apiParam {String{75 chars}} organization Name of Organization like College, Company, etc
@apiParam {String{75 chars}} project_link (Optional) Link to project on GitHub

@apiParamExample {json} Request Data Example:
{"hackathon":1,"owner_hacker":1,"name":"ThreeJacks","organization":"XYZ University"}
@apiSuccessExample {json} Success Response Code (HTTP/1.1 200 OK):
{"id":2,"search_key":"398508c8-f455-458e-ad7e-b2026e00c374","created_at":"2018-01-01T07:37:05.693295Z","updated_at":"2018-01-01T07:37:05.693320Z","hackathon":1,"owner_hacker":1,"name":"ThreeJacks","organization":"XYZ University","project_link":null}
"""

# List Teams
"""
@apiVersion 1.0.0
@api {get} /teams/ 2. List Teams 
@apiName ListTeams
@apiGroup Teams
@apiParam {Number} hackathon Hackathon ID Team if a part of

@apiDescription Allowed additional filter parameters are <br><br> <i>hackathon, type, name</i> <br><br>

@apiParamExample Sample Request 
https://api.wolfbeacon.com/v1/teams?hackathon=1

@apiSuccessExample {json} Sample Success Response
[{"id":2,"search_key":"398508c8-f455-458e-ad7e-b2026e00c374","created_at":"2018-01-01T07:37:05.693295Z","updated_at":"2018-01-01T07:37:05.693320Z","hackathon":1,"owner_hacker":1,"name":"ThreeJacks","organization":"XYZ University","project_link":null,"hackers":[{"id":1,"created_at":"2018-01-01T07:36:40.114561Z","updated_at":"2018-01-01T07:36:40.114587Z","user_id":1,"hackathon_id":1,"team_id":2,"application_status":"accepted"}]}]
"""

# GET Team
"""
@apiVersion 1.0.0
@api {get} /teams/:team-id/ 3. Get Team
@apiName GetTeam
@apiGroup Teams
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Team
"""
@apiVersion 1.0.0
@api {put} /teams/:team-id/ 4. Replace Team
@apiName ReplaceTeam
@apiGroup Teams
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PATCH Team
"""
@apiVersion 1.0.0
@api {patch} /teams/:team-id/ 5. Update Team
@apiName UpdateTeam
@apiDescription Supports Partial Update
@apiGroup Teams
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Team
"""
@apiVersion 1.0.0
@api {delete} /teams/:team-id/ 6. Delete Team
@apiName DeleteTeam
@apiGroup Teams
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    filter_fields = (
        'id', 'search_key', 'name', 'organization', 'hackathon',
    )

    def create(self, request, *args, **kwargs):
        # request.data['hackathon'] = self.kwargs['fk']

        return super(TeamViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(TeamViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(TeamViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data['id']], [self.kwargs['pk']])

        return super(TeamViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data['id']], [self.kwargs['pk']])

        return super(TeamViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(TeamViewSet, self).destroy(request, *args, **kwargs)


# ADD Hacker to Team
"""
@apiVersion 1.0.0
@api {post} /teams/:team-id/hackers/:hacker-id/ 7. Add Hacker to Team
@apiDescription This endpoint adds a Hacker attending a Hackathon to an Team of that Hackathon. Since no new Entity is being created, the request body is empty but with an HTTP 201 CREATED status code
@apiName AddHackerToTeam
@apiGroup Teams
@apiSuccessExample {json} Success Response Code (HTTP/1.1 201 CREATED):
{"id":2,"search_key":"398508c8-f455-458e-ad7e-b2026e00c374","created_at":"2018-01-01T07:37:05.693295Z","updated_at":"2018-01-01T07:37:05.693320Z","hackathon":1,"owner_hacker":1,"name":"ThreeJacks","organization":"XYZ University","project_link":null,"hackers":[{"id":1,"created_at":"2018-01-01T07:36:40.114561Z","updated_at":"2018-01-01T07:36:40.114587Z","user_id":1,"hackathon_id":1,"team_id":2,"application_status":"accepted"},{"id":2,"created_at":"2018-01-01T09:20:17.459468Z","updated_at":"2018-01-01T09:20:17.459491Z","user_id":5,"hackathon_id":1,"team_id":2,"application_status":"accepted"}]}
"""

# DELETE Hacker from Team
"""
@apiVersion 1.0.0
@api {delete} /teams/:team-id/hackers/:hacker-id/ 8. Remove Hacker from Team 
@apiName RemoveHackerFromTeam
@apiGroup Teams
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class TeamHackerAddRemove(APIView):
    """
    List all Team Hackers, Add Hacker to Team
    """

    def post(self, request, *args, **kwargs):

        team_id = self.kwargs['fk']
        hacker_id = self.kwargs['pk']

        try:
            hacker = Hacker.objects.get(id=hacker_id)
            team = Team.objects.get(id=team_id)

            team.hacker_set.add(hacker)

            upd_team_data = TeamSerializer(Team.objects.get(id=team_id)).data

            return Response(data=upd_team_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        team_id = self.kwargs['fk']
        hacker_id = self.kwargs['pk']

        try:
            hacker = Hacker.objects.get(id=hacker_id)
            team = Team.objects.get(id=team_id)

            team.hacker_set.remove(hacker)

            upd_team_data = TeamSerializer(Team.objects.get(id=team_id)).data

            return Response(data=upd_team_data, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
