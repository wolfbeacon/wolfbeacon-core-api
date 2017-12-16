from rest_framework.views import APIView
from rest_framework.response import Response

"""
@apiVersion 1.0.0
@apiName HeadersRequired
@api {headers} /*all_endpoints*  To pass for API Authentication and Response
@apiGroup Headers
@apiDescription Headers that need to passed with every API request. Clients require an Auth0 access_token for Authorization. See API Integration Docs<br><br>

@apiParam {header="application/json"} Content-Type Indicates Content is JSON
@apiParam {header="Bearer AUTH0_JWT_ACCESS_TOKEN"} Authorisation Auth0 Authentication Token

@apiHeaderExample {json} Headers:
{
    "Content-Type": "application/json"
    "Authorisation": "Bearer AUTH0_JWT_ACCESS_TOKEN"
}
"""


class RootView(APIView):
    """
    Root of WolfBeacon API
    """

    def get(self, request, format=None):
        return Response({"message": "Welcome to WolfBeacon API. Documentation at https://api.wolfbeacon.com/docs/"
                         }, status=200)
