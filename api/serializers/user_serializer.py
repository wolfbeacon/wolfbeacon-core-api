from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    hacker_profiles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'auth0_id', 'username', 'profile_picture_link', 'created_at', 'updated_at', 'first_name', 'last_name',
            'gender', 'email', 'phone_number', 'level_of_study', 'major_of_study', 'school_last_attended', 'graduation_year',
            'graduation_month', 'tshirt_size', 'country', 'city', 'zipcode', 'street_address', 'birthday',
            'social_links', 'dietary_restrictions', 'special_accommodations', 'technical_interests',
            'technologies', 'about_me', 'sponsors_interested_in', 'prizes_interested_in', 'experience_points',
            'badges_links', 'sticker_book_links',

            'hacker_profiles'
        )
        read_only_fields = ('id', 'created_at', 'updated_at',)

    def get_hacker_profiles(self, obj):
        return obj.hacker_set.all().values()
