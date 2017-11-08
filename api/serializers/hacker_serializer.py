from rest_framework import serializers
from api.models import Hacker


class HackerSerializer(serializers.ModelSerializer):
    def validate(self, data):

        # Check that user is not already added to hackathon.
        unique_check = Hacker.objects.filter(user_id=data['user'].id, hackathon_id=data['hackathon'].id)
        if len(unique_check) == 0:
            return data
        else:
            raise serializers.ValidationError("A User cannot be added to the same Hackathon again")

    class Meta:
        model = Hacker
        fields = ('id', 'hackathon', 'user', 'created_at', 'updated_at', 'role')
        read_only_fields = ('id', 'created_at', 'updated_at',)
