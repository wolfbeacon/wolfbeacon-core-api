from rest_framework import serializers
from api.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('hackathon_id', 'user_id', 'role')
