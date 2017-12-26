from rest_framework import serializers
from api.models import Organizer


class OrganizerSerializer(serializers.ModelSerializer):
    def validate(self, data):

        """
        Check that same User is not being added as a Organizer to a Hackathon again
        """

        # self.instance is None during POST and not None during PUT. We need to check duplicates during POST
        if self.instance is None:
            unique_check = Organizer.objects.filter(user_id=data['user'].id, hackathon_id=data['hackathon'].id)
            if len(unique_check) > 0:
                raise serializers.ValidationError("A User cannot be added as a Organizer to the same Hackathon again")

        return data

    class Meta:
        model = Organizer
        fields = ('id', 'hackathon', 'user', 'created_at', 'updated_at',)
        read_only_fields = ('id', 'created_at', 'updated_at',)
