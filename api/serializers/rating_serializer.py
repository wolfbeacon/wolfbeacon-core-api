from rest_framework import serializers
from api.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # Assert that Id for Event has been provided if rating is for Event entity
        if data['rating_for'] == 'event' and 'event' not in data:
            raise serializers.ValidationError('Event Id must be provided if rating is for Event entity')

        return data

    class Meta:
        model = Rating
        fields = ('id', 'created_at', 'updated_at', 'hackathon', 'hacker', 'rating_for', 'event', 'rating')
        read_only_fields = ('id', 'created_at', 'updated_at',)
