from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models import Hacker
from api.serializers import HackerSerializer
from api.utils import validators

# POST Hackers
"""
@apiVersion 1.0.0
@api {post} /hackathons/:hackathon-id/hackers/ 1. Create Hacker 
@apiName CreateHacker
@apiDescription Users are added to Hackathons as Hackers. Every Hackathon has it's own set of Hackers.
@apiGroup Hackers
@apiParam {String} user User ID of Hacker
@apiParam {String} hackathon Hackathon Id Hacker is to attend
@apiParam {String="organiser","volunteer","participant","mentor"} role Role of Hacker in Hackathon
@apiParam {String="accepted","wait-listed","applied","rejected"} application_status Hacker's Application status for particular hackathon
@apiParamExample {json} Request Data Example:
{"user":1,"hackathon":1,"role":"organiser"}
@apiSuccessExample {json} Success Response Code (HTTP/1.1 200 OK):
{"id":1,"hackathon":1,"user":1,"created_at":"2017-11-06T09:46:31.459815Z","updated_at":"2017-11-06T09:46:31.459856Z","role":"organiser"}
"""

# GET Hackers
"""
@apiVersion 1.0.0
@api {get} /hackers/? 2. List Hackers 
@apiName ListHackers
@apiGroup Hackers

@apiParam {Number} hackathon Hackathon ID hacker is part of
@apiParam {Number} event Event ID Hacker is part

@apiParamExample Sample Request 
https://api.wolfbeacon.com/v1/hackers?hackathon=1&event=2

@apiSuccessExample {json} Sample Success Response
[{"id":1,"hackathon":1,"user":1,"created_at":"2017-11-06T09:46:31.459815Z","updated_at":"2017-11-06T09:46:31.459856Z","role":"volunteer"},{"id":2,"hackathon":1,"user":2,"created_at":"2017-11-06T12:42:00.335711Z","updated_at":"2017-11-06T12:42:00.335746Z","role":"organiser"}]
Success Response Code: HTTP/1.1 200 OK
"""

# GET Hacker
"""
@apiVersion 1.0.0
@api {get} /hackers/:hacker-id/ 3. Get Hacker
@apiName GetHacker
@apiGroup Hackers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Hacker
"""
@apiVersion 1.0.0
@api {put} /hackers/:hacker-id/ 4. Replace Hacker
@apiName ReplaceHacker
@apiGroup Hackers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PATCH Hacker
"""
@apiVersion 1.0.0
@api {patch} /hackers/:hacker-id/ 5. Update Hacker
@apiName UpdateHacker
@apiDescription Supports Partial Update
@apiGroup Hackers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Hacker
"""
@apiVersion 1.0.0
@api {delete} /hackers/:hacker-id/ 6. Delete Hacker
@apiName DeleteHacker
@apiGroup Hackers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class HackerViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    serializer_class = HackerSerializer
    filter_fields = (
        'id', 'user', 'hackathon', 'role', 'application_status'
    )

    # Custom queryset
    def get_queryset(self):

        queryset = Hacker.objects.all()

        # Filter for Hackathons
        hackathon = self.request.query_params.get('hackathon', None)
        if hackathon:
            queryset = queryset.filter(hackathon=hackathon)

        # Filter for Events
        event = self.request.query_params.get('event', None)
        if event:
            queryset = queryset.filter(event__id=event)

        return queryset

    def create(self, request, *args, **kwargs):
        # validators.validate_body_url_id(request.data['hackathon'], self.kwargs['fk'])

        return super(HackerViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(HackerViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(HackerViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data.get('id', None)], [self.kwargs['pk']])

        return super(HackerViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data.get('id', None)], [self.kwargs['pk']])

        return super(HackerViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(HackerViewSet, self).destroy(request, *args, **kwargs)
