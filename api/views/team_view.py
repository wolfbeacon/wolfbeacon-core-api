from rest_framework.viewsets import ModelViewSet
from api.models import Team
from api.serializers import TeamSerializer


class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    filter_fields = (
        'id', 'search_key', 'name', 'organization', 'hackathon',
    )

    def create(self, request, *args, **kwargs):
        # request.data['hackathon'] = self.kwargs['fk']

        return super(TeamViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(TeamViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(TeamViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data['id']], [self.kwargs['pk']])

        return super(TeamViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data['id']], [self.kwargs['pk']])

        return super(TeamViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(TeamViewSet, self).destroy(request, *args, **kwargs)

