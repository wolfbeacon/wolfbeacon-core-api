from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models import Organizer
from api.serializers import OrganizerSerializer

# POST Organizer
"""
@apiVersion 1.0.0
@api {post} /hackathons/:hackathon-id/organizers/ 1. Create Organizer 
@apiName CreateOrganizer
@apiDescription Users are added to Hackathons as Organizers. Every Hackathon has it's own set of Organizers.
@apiGroup Organizers
@apiParam {String} user User ID of Organizer
@apiParam {String} hackathon Hackathon Id Organizer is to attend
@apiParamExample {json} Request Data Example:
{"user":1,"hackathon":1,"application_status":"accepted"}
@apiSuccessExample {json} Success Response Code (HTTP/1.1 200 OK):
{"id":1,"hackathon":1,"user":1,"created_at":"2017-11-06T09:46:31.459815Z","updated_at":"2017-11-06T09:46:31.459856Z"}
"""

# GET Organizers
"""
@apiVersion 1.0.0
@api {get} /organizers/? 2. List Organizers 
@apiName ListOrganizers
@apiGroup Organizers

@apiParam {Number} hackathon Hackathon ID organizer is part of
@apiParam {Number} event Event ID Organizer is part

@apiParamExample Sample Request 
https://api.wolfbeacon.com/v1/organizers?hackathon=1&event=2

@apiSuccessExample {json} Sample Success Response
[{"id":1,"hackathon":1,"user":1,"created_at":"2017-11-06T09:46:31.459815Z","updated_at":"2017-11-06T09:46:31.459856Z"},{"id":2,"hackathon":1,"user":2,"created_at":"2017-11-06T12:42:00.335711Z","updated_at":"2017-11-06T12:42:00.335746Z"}]
Success Response Code: HTTP/1.1 200 OK
"""

# GET Organizer
"""
@apiVersion 1.0.0
@api {get} /organizers/:organizer-id/ 3. Get Organizer
@apiName GetOrganizer
@apiGroup Organizers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Organizer
"""
@apiVersion 1.0.0
@api {put} /organizers/:organizer-id/ 4. Replace Organizer
@apiName ReplaceOrganizer
@apiGroup Organizers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PATCH Organizer
"""
@apiVersion 1.0.0
@api {patch} /organizers/:organizer-id/ 5. Update Organizer
@apiName UpdateOrganizer
@apiDescription Supports Partial Update
@apiGroup Organizers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Organizer
"""
@apiVersion 1.0.0
@api {delete} /organizers/:organizer-id/ 6. Delete Organizer
@apiName DeleteOrganizer
@apiGroup Organizers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class OrganizerViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):
    serializer_class = OrganizerSerializer
    queryset = Organizer.objects.all()
    filter_fields = (
        'id', 'user', 'hackathon',
    )

    def create(self, request, *args, **kwargs):
        # validators.validate_body_url_id(request.data['hackathon'], self.kwargs['fk'])

        return super(OrganizerViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(OrganizerViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(OrganizerViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data.get('id', None)], [self.kwargs['pk']])

        return super(OrganizerViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data.get('id', None)], [self.kwargs['pk']])

        return super(OrganizerViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(OrganizerViewSet, self).destroy(request, *args, **kwargs)
