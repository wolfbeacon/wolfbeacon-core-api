from rest_framework.views import APIView
from rest_framework.response import Response


class RootView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        return Response({"message": "Welcome to WolfBeacon API."}, status=200)
