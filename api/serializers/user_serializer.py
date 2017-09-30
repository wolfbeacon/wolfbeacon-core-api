from rest_framework import serializers
from api.models.user_model import User


class UserSerializer(serializers.ModelSerializer):
    hackathons = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'user_id', 'auth0_id', 'created_at', 'updated_at', 'first_name', 'last_name', 'gender', 'email',
            'phone_number', 'level_of_study', 'major_of_study', 'school_last_attended', 'graduation_year',
            'graduation_month', 'tshirt_size', 'country', 'city', 'birthday', 'social_urls', 'dietary_restrictions',
            'special_accommodations', 'technical_interests', 'technologies', 'about_me', 'sponsors_interested_in',
            'prizes_interested_in', 'badges_links', 'experience_points', 'sticker_book_links', 'hackathons'
        )
        read_only_fields = ('user_id', 'created_at', 'updated_at',)

    def get_hackathons(self, obj):
        return obj.hackathon_set.all().values('hackathon_id', )
