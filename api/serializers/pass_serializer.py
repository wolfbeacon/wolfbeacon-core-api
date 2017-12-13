from rest_framework import serializers
from api.models import Pass


class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = ('id', 'datafile', 'hacker')
