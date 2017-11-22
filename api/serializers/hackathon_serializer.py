from rest_framework import serializers
from api.models import Hackathon


class HackathonSerializer(serializers.ModelSerializer):
    # Additional Fields
    no_of_organisers = serializers.SerializerMethodField()
    no_of_volunteers = serializers.SerializerMethodField()
    no_of_participants = serializers.SerializerMethodField()
    no_of_mentors = serializers.SerializerMethodField()

    class Meta:
        model = Hackathon
        fields = ('id', 'created_at', 'updated_at', 'is_published', 'name', 'version',
                  'description', 'logo', 'hackathon_type', 'location', 'shipping_address',
                  'travel_reimbursements', 'social_links', 'university_name', 'contact_email',
                  'start_time', 'end_time', 'bus_routes', 'timetable', 'sponsors', 'judges',
                  'speakers', 'prizes',

                  'no_of_organisers', 'no_of_volunteers', 'no_of_participants', 'no_of_mentors'
                  )

        read_only_fields = ('id', 'created_at', 'updated_at',)

    def get_no_of_organisers(self, obj):
        return len(obj.hacker_set.all().filter(role='organiser'))

    def get_no_of_volunteers(self, obj):
        return len(obj.hacker_set.all().filter(role='volunteer'))

    def get_no_of_participants(self, obj):
        return len(obj.hacker_set.all().filter(role='participant'))

    def get_no_of_mentors(self, obj):
        return len(obj.hacker_set.all().filter(role='mentor'))
