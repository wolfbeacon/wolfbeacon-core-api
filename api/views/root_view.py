from rest_framework.views import APIView
from rest_framework.response import Response

"""
@apiVersion 0.0.1
@apiName HeadersRequired
@api {headers} /*  To pass for API Authentication and Response
@apiGroup Headers
@apiDescription These headers need to passed along with every API request
@apiHeaderExample {json} Headers:
{
    "Content-Type": "application/json"
    "Authorisation": "Bearer JWT_TOKEN"
}
"""

class RootView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        return Response({"message": "Welcome to WolfBeacon API."}, status=200)
