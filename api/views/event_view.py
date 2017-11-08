from api.models import Event, Hacker
from api.serializers import EventSerializer

from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# GET All Events
"""
@apiVersion 0.0.1
@api {get} /events/ 2. Get Events 

@apiName GetAllEventsForHackathon
@apiGroup Events 

@apiParam {Integer} hackathon ID of Hackathon this Event is a part of
@apiParam {String="mini-mlh-event","general-workshop","company-workshop","speaker-session", "fireside-chats", "open-source-event", "activity"} type Type of Event
@apiParam {String} name Name of Event
@apiParam {String} location Location of Event
@apiParam {String} giveaway Event Giveaways

@apiParamExample Sample Request 
https://api.wolfbeacon.com/hackers?hackathon=1

@apiSuccessExample {json} Sample Success Response
[{"id":3,"created_at":"2017-11-06T19:41:30.644678Z","updated_at":"2017-11-06T19:41:30.644721Z","hackathon":1,"type":"general-workshop","name":"Test Name","tagline":"Test Workshop","description":"Test Description","speaker_details":{},"location":"Building A","giveaway":"Tshirt","no_of_attendees":0,"rating":0},{"id":2,"created_at":"2017-11-06T19:41:30.439853Z","updated_at":"2017-11-06T19:41:30.439882Z","hackathon":1,"type":"general-workshop","name":"Test Name","tagline":"Test Workshop","description":"Test Description","speaker_details":{},"location":"Building A","giveaway":"Tshirt","no_of_attendees":0,"rating":0}]Success Response Code: HTTP/1.1 200 OK
"""


class EventList(mixins.ListModelMixin,
                generics.GenericAPIView):
    """
    List All Events
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    filter_fields = (
        'id', 'hackathon', 'type', 'name', 'tagline', 'description',
        'location', 'giveaway'
    )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# POST Events
"""
@apiVersion 0.0.1
@api {post} /hackathons/:hackathon-id/events/ 1. Create Event 
@apiName CreateEvent
@apiDescription Users are added to Hackathons as Events. Every Hackathon has it's own set of Events.
@apiGroup Events

@apiParam {Integer} hackathon ID of Hackathon this Event is a part of
@apiParam {String="mini-mlh-event","general-workshop","company-workshop","speaker-session", "fireside-chats", "open-source-event", "activity"} type Type of Event
@apiParam {String{50 chars}} name Name of Event
@apiParam {String{150 chars}} tagline Tagline for Event
@apiParam {String{350 chars}} description Description of Event
@apiParam {json} speaker_details Speaker Details
@apiParam {String{150 chars}} location Location of Event
@apiParam {String} giveaway Event Giveaways

@apiParamExample {json} Request Data Example:
{"hackathon":1,"name":"Test Name","type":"general-workshop","tagline":"Test Workshop","description":"Test Description","speaker_details":{},"location":"Building A","giveaway":"Tshirt"}
@apiSuccessExample {json} Success Response Code (HTTP/1.1 200 OK):
{"id":3,"created_at":"2017-11-06T19:41:30.644678Z","updated_at":"2017-11-06T19:41:30.644721Z","hackathon":1,"type":"general-workshop","name":"Test Name","tagline":"Test Workshop","description":"Test Description","speaker_details":{},"location":"Building A","giveaway":"Tshirt","no_of_attendees":0,"rating":0}
"""


class EventCreate(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    Create a new Event
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def post(self, request, *args, **kwargs):
        # Reinsert hackathon key for sanity
        request.data['hackathon'] = self.kwargs['fk']

        return self.create(request, *args, **kwargs)


# GET Event
"""
@apiVersion 0.0.1
@api {get} /hackathons/:hackathon-id/events/:event-id/ 3. Get Event
@apiName GetEvent
@apiGroup Events
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Event
"""
@apiVersion 0.0.1
@api {put} /hackathons/:hackathon-id/events/:event-id/ 4. Update Event
@apiName UpdateEvent
@apiDescription Supports Partial Update
@apiGroup Events
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Event
"""
@apiVersion 0.0.1
@api {patch} /hackathons/:hackathon-id/events/:event-id/ 5. Partially Update Event
@apiName PartiallyUpdateEvent
@apiDescription Supports Partial Update
@apiGroup Events
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Event
"""
@apiVersion 0.0.1
@api {delete} /hackathons/:hackathon-id/events/:event-id/ 6. Delete Event
@apiName DeleteEvent
@apiGroup Events
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class EventRUD(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):
    """
    Get Visitor, Update Visitor, Delete Visitor
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Insert keys for sanity
        request.data['hackathon'] = self.kwargs['fk']
        request.data['id'] = self.kwargs['pk']

        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # Insert keys for sanity
        request.data['hackathon'] = self.kwargs['fk']
        request.data['id'] = self.kwargs['pk']

        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# POST Hacker to Event
"""
@apiVersion 0.0.1
@api {post} /hackathons/:hackathon-id/events/:event-id/hackers/ 7. Add Hacker to Event 
@apiName AddHackerToEvent
@apiDescription Users are added to Hackathons as Events. Every Hackathon has it's own set of Events.
@apiGroup Events
@apiParam {Integer} hacker ID of Hacker to be added to this event
@apiParamExample {json} Request Data Example:
{"hacker":1}
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 201 CREATED
"""


class EventHackerAdd(APIView):
    """
    Add Hacker to Event
    """

    def post(self, request, *args, **kwargs):
        request.data['hackathon'] = self.kwargs['fk']
        request.data['event'] = self.kwargs['pk']

        hacker_id = request.data['hacker']
        event_id = request.data['event']

        try:
            event = Event.objects.get(id=event_id)
            hacker = Hacker.objects.get(id=hacker_id)

            event.hackers.add(hacker)

            return Response({'hacker': hacker_id}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
