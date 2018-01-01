from rest_framework import serializers
from api.models import Team, Hacker


class TeamSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Don't exceed max team size while adding member
        """

        # self.instance is None during POST and not None during PUT. We need to check duplicates during POST
        if self.instance is not None:
            # TODO
            pass
        return data

    hackers = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ('id', 'search_key', 'created_at', 'updated_at', 'hackathon', 'owner_hacker', 'name', 'organization',
                  'project_link',

                  'hackers')
        read_only_fields = ('id', 'created_at', 'updated_at', 'search_key')

    def get_hackers(self, obj):
        return obj.hacker_set.all().values()
