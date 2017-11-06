from rest_framework import serializers
from api.models import Event


class EventSerializer(serializers.ModelSerializer):
    no_of_attendees = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('id', 'created_at', 'updated_at', 'hackathon', 'type', 'name',
                  'tagline', 'description', 'speaker_details', 'location', 'giveaway',

                  'no_of_attendees', 'rating',
                  )

        read_only_fields = ('id', 'created_at', 'updated_at',)

    def get_no_of_attendees(self, obj):
        return len(obj.hackers.all())

    def get_rating(self, obj):
        # TODO Write rate average query
        return 0
