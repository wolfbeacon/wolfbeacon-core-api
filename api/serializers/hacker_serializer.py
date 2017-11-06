from rest_framework import serializers
from api.models import Hacker


class HackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hacker
        fields = ('id', 'hackathon', 'user', 'created_at', 'updated_at', 'role')
        read_only_fields = ('id', 'created_at', 'updated_at', )
