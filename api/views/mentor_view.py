from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models import Mentor
from api.serializers import MentorSerializer

# POST Mentor
"""
@apiVersion 1.0.0
@api {post} /hackathons/:hackathon-id/mentors/ 1. Create Mentor 
@apiName CreateMentor
@apiDescription Users are added to Hackathons as Mentors. Every Hackathon has it's own set of Mentors.
@apiGroup Mentors
@apiParam {String} user User ID of Mentor
@apiParam {String} hackathon Hackathon Id Mentor is to attend
@apiParamExample {json} Request Data Example:
{"user":1,"hackathon":1}
@apiSuccessExample {json} Success Response Code (HTTP/1.1 200 OK):
{"id":1,"hackathon":1,"user":1,"created_at":"2017-11-06T09:46:31.459815Z","updated_at":"2017-11-06T09:46:31.459856Z"}
"""

# GET Mentors
"""
@apiVersion 1.0.0
@api {get} /mentors/? 2. List Mentors 
@apiName ListMentors
@apiGroup Mentors

@apiParam {Number} hackathon Hackathon ID mentor is part of
@apiParam {Number} event Event ID Mentor is part

@apiParamExample Sample Request 
https://api.wolfbeacon.com/v1/mentors?hackathon=1&event=2

@apiSuccessExample {json} Sample Success Response
[{"id":1,"hackathon":1,"user":1,"created_at":"2017-11-06T09:46:31.459815Z","updated_at":"2017-11-06T09:46:31.459856Z"},{"id":2,"hackathon":1,"user":2,"created_at":"2017-11-06T12:42:00.335711Z","updated_at":"2017-11-06T12:42:00.335746Z"}]
Success Response Code: HTTP/1.1 200 OK
"""

# GET Mentor
"""
@apiVersion 1.0.0
@api {get} /mentors/:mentor-id/ 3. Get Mentor
@apiName GetMentor
@apiGroup Mentors
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Mentor
"""
@apiVersion 1.0.0
@api {put} /mentors/:mentor-id/ 4. Replace Mentor
@apiName ReplaceMentor
@apiGroup Mentors
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PATCH Mentor
"""
@apiVersion 1.0.0
@api {patch} /mentors/:mentor-id/ 5. Update Mentor
@apiName UpdateMentor
@apiDescription Supports Partial Update
@apiGroup Mentors
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Mentor
"""
@apiVersion 1.0.0
@api {delete} /mentors/:mentor-id/ 6. Delete Mentor
@apiName DeleteMentor
@apiGroup Mentors
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class MentorViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    serializer_class = MentorSerializer
    queryset = Mentor.objects.all()
    filter_fields = (
        'id', 'user', 'hackathon',
    )

    def create(self, request, *args, **kwargs):
        # validators.validate_body_url_id(request.data['hackathon'], self.kwargs['fk'])

        return super(MentorViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(MentorViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(MentorViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data.get('id', None)], [self.kwargs['pk']])

        return super(MentorViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data.get('id', None)], [self.kwargs['pk']])

        return super(MentorViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(MentorViewSet, self).destroy(request, *args, **kwargs)
