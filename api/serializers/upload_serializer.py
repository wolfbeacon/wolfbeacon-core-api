from rest_framework import serializers
from api.models.upload_model import Upload


class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload
        fields = ('datafile',)

