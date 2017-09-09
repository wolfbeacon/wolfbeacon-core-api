from rest_framework import serializers
from api.models.hackathon_model import Hackathon


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ('id', 'data', 'organiser_email_id', 'is_published')
