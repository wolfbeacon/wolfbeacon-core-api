from api.models import Hackathon
from api.serializers import HackathonSerializer
from rest_framework import viewsets
from api.utils import validators

# POST Hackathon
"""
@apiVersion 1.0.0
@api {post} /hackathons/ 1. Create Hackathon
@apiName CreateHackathon
@apiGroup Hackathons 

@apiParam {String{150 chars}} name Name/Title of Hackathon
@apiParam {String} version Denotes which iteration of this hackathon
@apiParam {String} description Short note about the uniqueness of the Hackathon
@apiParam {File} logo_image_file (Optional) Image file (.jpg, png) of Hackathon Logo (Multipart Request) 
@apiParam {String="high-school","university","corporate","other"} hackathon_type Type of Hackathon denoting audience
@apiParam {String{350 chars}} location Location of Hackathon Example: EX: 756 Finch Ave, Toronto, Canada
@apiParam {Number} latitude Location of Hackathon Example: EX: 756 Finch Ave, Toronto, Canada
@apiParam {Number} longitude Location of Hackathon Example: EX: 756 Finch Ave, Toronto, Canada
@apiParam {String{350 chars}} shipping_address Address for contact or shipping goodies. Example: Apt # 708, 1365 Military Trail	
@apiParam {String} travel_reimbursements Note about travel reimbursements
@apiParam {String} university_name (Optional) For University MLH Rankings
@apiParam {String} contact_email Email Id to reach out to hackathon organisers
@apiParam {String="YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]"} start Denotes start time of hackathon
@apiParam {String="YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]"} end Denotes end time of hackathon
@apiParam {json} social_links Social URLs as `{"social_platform_1":"link", "social_platform_2":"link"...}`
@apiParam {json} bus_routes Bus Routes in travel arrangements 
@apiParam {json} timetable Timetable of hackathon events and happenings
@apiParam {json} sponsors Sponsors
@apiParam {json} judges Judges
@apiParam {json} speakers Speakers
@apiParam {json} prizes Prizes

@apiParamExample {json} Request Data Example:
{"name":"Hack The Valley","description":"Hackathon at UoT Scarborough","logo":"hello://google.com","hackathon_type":"university","location":"Toronto, ON","latitude":43.6532,"longitude":79.3832,"shipping_address":"Road 123, Toronto, Canada","travel_reimbursements":"Yes, depending on location","university_name":"University Of Toronto","contact_email":"ralphpal@wolfbeacon.com","start":"2017-10-10 06:00:00+0000","end":"2017-10-14 06:00:00+0000","social_links":{"facebook":"https://facebook.com/htv","twitter":"https://twitter.com/hackthevalley"},"bus_routes":{},"timetable":{},"sponsors":{},"judges":{},"speakers":{},"prizes":{}}

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 201 Created
"""

# List Hackathons
"""
@apiVersion 1.0.0
@api {get} /hackathons/ 2. List Hackathons
@apiName ListHackathons
@apiGroup Hackathons
@apiDescription Allowed additional search parameters are <br><br> <i>id, created_at, updated_at, is_published, name, version, description, hackathon_type, location, shipping_address, university_name, contact_email, start, end,</i> <br><br>
@apiParam {boolean=true,false} featured Filters featured hackathons for featured=true
@apiParam {String="YYYY-MM-DD"} start_date Filters Hackathons which have `start` >= `start_date` passed
@apiParam {String="YYYY-MM-DD"} featured Filters Hackathons which have `end` <= `end_date` passed

@apiParamExample Sample Request 
https://api.wolfbeacon.com/hackathons?featured=true&start_date=2017-09-01&hackathon_type=university

@apiSuccessExample {json} Success Response Code (HTTP/1.1 200 OK):
[{"id":1,"created_at":"2017-10-16T16:27:27.403807Z","updated_at":"2017-10-16T16:27:27.403856Z","is_published":false,"name":"Hack The Valley","version":1,"description":"Hackathon at UoT Scarborough","logo":"hello://google.com","hackathon_type":"university","location":"Toronto, ON","latitude": 43.6532,"longitude": 79.3832,"shipping_address":"Road 123, Toronto, Canada","travel_reimbursements":"Yes, depending on location","social_links":{"facebook":"https://facebook.com/htv","twitter":"https://twitter.com/hackthevalley"},"university_name":"University Of Toronto","contact_email":"ralphpal@wolfbeacon.com","start":"2017-09-03T22:00:00Z","end":"2017-09-04T22:00:00Z","bus_routes":{},"timetable":{},"sponsors":{},"judges":{},"speakers":{},"prizes":{},"no_of_organisers":1,"no_of_volunteers":0,"no_of_participants":750,"no_of_mentors":0},{"id":2,"created_at":"2017-10-16T16:27:45.946560Z","updated_at":"2017-10-16T16:27:45.946588Z","is_published":false,"name":"Hack The Noth","version":1,"description":"Hackathon at University of Waterloo","latitude": 43.6532,"longitude": 79.3832,"logo":"hello://google.com","hackathon_type":"university","location":"Waterloo, Canada","shipping_address":"Road 123, Waterloo, Canada","travel_reimbursements":"Yes, depending on location","social_links":{"facebook":"https://facebook.com/htv","twitter":"https://twitter.com/hackthevalley"},"university_name":"University Of Waterloo","contact_email":"ralphpal@wolfbeacon.com","start":"2017-09-03T22:00:00Z","end":"2017-09-04T22:00:00Z","bus_routes":{},"timetable":{},"sponsors":{},"judges":{},"speakers":{},"prizes":{},"no_of_organisers":2,"no_of_volunteers":0,"no_of_participants":1200,"no_of_mentors":0}]
"""

# GET Hackathon
"""
@apiVersion 1.0.0
@api {get} /hackathons/:hackathon-id/ 3. Get Hackathon
@apiName GetHackathon
@apiGroup Hackathons

@apiSuccessExample {json} Success Response (HTTP/1.1 200 OK):
{"id":2,"created_at":"2017-10-16T16:27:45.946560Z","updated_at":"2017-10-16T16:27:45.946588Z","is_published":false,"name":"Hack The Valley","version":1,"description":"Hackathon at UoT Scarborough","logo":"hello://google.com","hackathon_type":"university","location":"Toronto, ON","latitude": 43.6532,"longitude": 79.3832,"shipping_address":"Road 123, Toronto, Canada","travel_reimbursements":"Yes, depending on location","social_links":{"twitter":"https://twitter.com/hackthevalley","facebook":"https://facebook.com/htv"},"university_name":"University Of Toronto","contact_email":"ralphpal@wolfbeacon.com","start":"2017-09-04T06:00:00+08:00","end":"2017-09-05T06:00:00+08:00","bus_routes":{},"timetable":{},"sponsors":{},"judges":{},"speakers":{},"prizes":{},"no_of_organisers":0,"no_of_volunteers":0,"no_of_participants":0,"no_of_mentors":0}
"""

# PUT Hackathon
"""
@apiVersion 1.0.0
@api {put} /hackathons/:hackathon-id/ 4. Replace Hackathon
@apiName ReplaceHackathon
@apiDescription Complete Entity update, expects all mandatory fields
@apiGroup Hackathons
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PATCH User
"""
@apiVersion 1.0.0
@api {patch} hackathons/:hackathon-id/ 5. Update Hackathon
@apiName UpdateHackathon
@apiDescription Supports partial updates.
@apiGroup Hackathons
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Hackathon
"""
@apiVersion 1.0.0
@api {delete} /hackathons/:hackathon-id/ 6. Delete Hackathon
@apiName DeleteHackathon
@apiGroup Hackathons
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class HackathonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    def get_queryset(self):
        queryset = Hackathon.objects.all()

        # Check for featured hackathon params
        featured = self.request.query_params.get('featured', None)
        if featured == 'true':
            queryset = queryset.featured()

        # Filter Hackathons starting after start_date and ending before end_date
        start_date = self.request.query_params.get('start_date', None)
        if start_date:
            # Get formatted in datetime
            start_date = validators.validate_hackathon_url_date(start_date)

            queryset = queryset.start_date(start_date)

        end_date = self.request.query_params.get('end_date', None)
        if end_date:
            end_date = validators.validate_hackathon_url_date(end_date)

            queryset = queryset.end_date(end_date)

        return queryset

    serializer_class = HackathonSerializer
    filter_fields = (
        'id', 'created_at', 'updated_at', 'is_published', 'name', 'version',
        'description', 'hackathon_type', 'location', 'shipping_address', 'university_name',
        'contact_email', 'start', 'end',
    )
