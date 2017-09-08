from api.models import Hackathon
from api.models import User
from api.serializers import HackathonSerializer
from rest_framework import generics
from django.db.transaction import atomic

"""
GET All Hackathons
CREATE Hackathon
"""


class HackathonListAndCreate(generics.ListCreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

    """
    Override post in Generics to CREATE Hackathon
    """

    @atomic
    def post(self, request, *args, **kwargs):
        # Get User id
        serializer = HackathonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.data.organiser_email_id

        # Create User
        User.objects.get_or_create(id=user_id)

        # Finally, Create Hackathon
        return self.create(request, *args, **kwargs)


"""
GET Hackathon
PUT Hackathon
DELETE Hackathon
"""


class HackathonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
