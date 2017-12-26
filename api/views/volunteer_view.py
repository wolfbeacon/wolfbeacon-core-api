from rest_framework.viewsets import ModelViewSet

from api.models import Volunteer
from api.serializers import VolunteerSerializer

# POST Volunteer
"""
@apiVersion 1.0.0
@api {post} /hackathons/:hackathon-id/volunteers/ 1. Create Volunteer 
@apiName CreateVolunteer
@apiDescription Users are added to Hackathons as Volunteers. Every Hackathon has it's own set of Volunteers.
@apiGroup Volunteers
@apiParam {String} user User ID of Volunteer
@apiParam {String} hackathon Hackathon Id Volunteer is to attend
@apiParam {String} duty_assigned (Optional) Duty assigned to Volunteer like Photographer, Guide etc
@apiParamExample {json} Request Data Example:
{"user":1,"hackathon":1}
@apiSuccessExample {json} Success Response Code (HTTP/1.1 200 OK):
{"id":1,"hackathon":1,"user":1,"created_at":"2017-11-06T09:46:31.459815Z","updated_at":"2017-11-06T09:46:31.459856Z"}
"""

# GET Volunteers
"""
@apiVersion 1.0.0
@api {get} /volunteers/? 2. List Volunteers 
@apiName ListVolunteers
@apiGroup Volunteers

@apiParam {Number} hackathon Hackathon ID volunteer is part of
@apiParam {Number} event Event ID Volunteer is part

@apiParamExample Sample Request 
https://api.wolfbeacon.com/v1/volunteers?hackathon=1&event=2

@apiSuccessExample {json} Sample Success Response
[{"id":1,"hackathon":1,"user":1,"created_at":"2017-11-06T09:46:31.459815Z","updated_at":"2017-11-06T09:46:31.459856Z"},{"id":2,"hackathon":1,"user":2,"created_at":"2017-11-06T12:42:00.335711Z","updated_at":"2017-11-06T12:42:00.335746Z"}]
Success Response Code: HTTP/1.1 200 OK
"""

# GET Volunteer
"""
@apiVersion 1.0.0
@api {get} /volunteers/:volunteer-id/ 3. Get Volunteer
@apiName GetVolunteer
@apiGroup Volunteers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Volunteer
"""
@apiVersion 1.0.0
@api {put} /volunteers/:volunteer-id/ 4. Replace Volunteer
@apiName ReplaceVolunteer
@apiGroup Volunteers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PATCH Volunteer
"""
@apiVersion 1.0.0
@api {patch} /volunteers/:volunteer-id/ 5. Update Volunteer
@apiName UpdateVolunteer
@apiDescription Supports Partial Update
@apiGroup Volunteers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Volunteer
"""
@apiVersion 1.0.0
@api {delete} /volunteers/:volunteer-id/ 6. Delete Volunteer
@apiName DeleteVolunteer
@apiGroup Volunteers
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class VolunteerViewSet(ModelViewSet):
    serializer_class = VolunteerSerializer
    queryset = Volunteer.objects.all()
    filter_fields = (
        'id', 'user', 'hackathon', 'duty_assigned'
    )

    def create(self, request, *args, **kwargs):
        # validators.validate_body_url_id(request.data['hackathon'], self.kwargs['fk'])

        return super(VolunteerViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(VolunteerViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(VolunteerViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data.get('id', None)], [self.kwargs['pk']])

        return super(VolunteerViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # validators.validate_body_url_id([request.data.get('id', None)], [self.kwargs['pk']])

        return super(VolunteerViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(VolunteerViewSet, self).destroy(request, *args, **kwargs)
