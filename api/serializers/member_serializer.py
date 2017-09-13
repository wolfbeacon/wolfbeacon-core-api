from rest_framework import serializers
from api.models.hackathon_member_model import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('hackathon', 'member', 'role')
