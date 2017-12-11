from rest_framework import serializers
from api.models.file_upload_model import FileUpload


class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileUpload
        fields = ('datafile',)

