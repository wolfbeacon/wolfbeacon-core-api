from rest_framework import serializers
from api.models import Hackathon, User


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ('id', 'data', 'organiser_email_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id'
