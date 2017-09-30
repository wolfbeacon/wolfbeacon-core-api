from api.models.hackathon_member_model import Hackathon
from api.serializers.hackathon_serializer import HackathonSerializer
from api.services import hackathon_service
from rest_framework import viewsets

# POST Hackathon
"""
@apiVersion 0.0.1
@api {post} /hackathons/ 1. Create Hackathon
@apiName CreateHackathon
@apiGroup Hackathons

@apiParam {String} cms_id Unique ID given to Hackathon in CMS
@apiParam {JSON} data Hackathon Data as JSON Object

@apiParamExample {json} Request Data Example:
{"cms_id":1,"data":{"exampleHackathonData":{"Name":"Penapps"}}}

@apiSuccessExample {json} Success Response (HTTP/1.1 201 OK):
{"hackathon_id":1234,cms_id":1,"data":{"exampleHackathonData":{"Name":"Penapps"}}}
"""

# GET All Hackathons
"""
@apiVersion 0.0.1
@api {get} /hackathons/ 2. Get All Hackathons
@apiName GetAllHackathons
@apiGroup Hackathons
@apiParam {boolean} featured Returns featured hackathons for featured=true
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# GET Hackathon
"""
@apiVersion 0.0.1
@api {get} /hackathons/:hackathon-id/ 3. Get Hackathon
@apiName GetHackathon
@apiGroup Hackathons
@apiParam {Number} hackathon-id Hackathon unique ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Hackathon
"""
@apiVersion 0.0.1
@api {put} /hackathons/:hackathon-id/ 4. Update Hackathon
@apiName UpdateHackathon
@apiGroup Hackathons
@apiParam {Number} hackathon-id Hackathon unique ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Hackathon
"""
@apiVersion 0.0.1
@api {delete} /hackathons/:hackathon-id/ 5. Delete Hackathon
@apiName DeleteHackathon
@apiGroup Hackathons
@apiParam {Number} hackathon-id Hackathon unique ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class HackathonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    def get_queryset(self):
        queryset = Hackathon.objects.all()

        # Featured Hackathons
        featured = self.request.query_params.get('featured', None)
        if featured == 'true':
            queryset = hackathon_service.filter_featured_hackathons()

        return queryset

    serializer_class = HackathonSerializer
