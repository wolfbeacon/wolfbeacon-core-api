from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from api.models.upload_model import Upload
from api.serializers.upload_serializer import UploadSerializer


class UploadViewSet(ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(datafile=self.request.data.get('datafile'))
