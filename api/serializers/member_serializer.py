from rest_framework import serializers
from api.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('hackathon_id', 'user_id', 'created_at', 'updated_at', 'role')

        read_only_fields = ('user_id', 'hackathon_id', 'created_at', 'updated_at',)
