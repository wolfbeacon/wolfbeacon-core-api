from rest_framework import serializers
from api.models import Hackathon


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ('id', 'created_at', 'updated_at', 'is_published', 'name', 'version',
                  'description', 'logo_image_file', 'hackathon_type', 'location', 'latitude', 'longitude',
                  'shipping_address', 'travel_reimbursements', 'social_links', 'university_name',
                  'contact_email', 'start', 'end', 'bus_routes', 'timetable', 'sponsors',
                  'judges', 'speakers', 'prizes',)
        read_only_fields = ('id', 'created_at', 'updated_at',)
