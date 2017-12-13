from rest_framework.viewsets import ModelViewSet
from api.models import Pass
from api.serializers import PassSerializer


class PassViewSet(ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    filter_fields = (
        'hacker',
    )
