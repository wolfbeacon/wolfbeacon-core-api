from api.models import Rating
from api.serializers import RatingSerializer
from rest_framework import viewsets

# POST Rating
"""
@apiVersion 0.0.1
@api {post} /ratings/ 1. Create Rating
@apiName CreateRating
@apiGroup Ratings 

@apiParam {Number} hackathon ID of Hackathon for which rating is
@apiParam {Number} hacker ID of Hacker who is posting the rating
@apiParam {String="hackathon","event"} rating_for Denotes what the rating is for
@apiParam {String} event (Optional) Id of Event of Hackathon IF rating is for `event` type
@apiParam {Number=1,2,3,4,5} rating Rating on a scale of 1 - 5

@apiParamExample {json} Request Data Example:
{"hackathon":1,"hacker":1,"rating_for":"hackathon","rating":5}

@apiSuccessExample {json} Success Response Code(HTTP/1.1 201 Created):
{"id":3,"created_at":"2017-11-07T17:08:27.213067Z","updated_at":"2017-11-07T17:08:27.213090Z","hackathon":1,"hacker":1,"rating_for":"event","event":1,"rating":5}

"""

# GET All Ratings
"""
@apiVersion 0.0.1
@api {get} /ratings/ 2. Get All Ratings
@apiName GetAllRatings
@apiGroup Ratings
@apiDescription Additional search parameters can be <br><br> <i>id, hackathon, hacker, rating_for, event, rating</i> <br><br>

@apiParamExample Sample Request 
https://api.wolfbeacon.com/ratings?hackathon=1&user=1&hacker=1

@apiSuccessExample {json} Success Response Code (HTTP/1.1 200 OK):
[{"id":3,"created_at":"2017-11-07T17:08:27.213067Z","updated_at":"2017-11-07T17:08:27.213090Z","hackathon":1,"hacker":1,"rating_for":"event","event":1,"rating":5},{"id":5,"created_at":"2017-11-07T17:10:24.830366Z","updated_at":"2017-11-07T17:10:24.830396Z","hackathon":1,"hacker":1,"rating_for":"hackathon","event":null,"rating":4}]
"""

# GET Rating
"""
@apiVersion 0.0.1
@api {get} /ratings/:rating-id/ 3. Get Rating
@apiName GetRating
@apiGroup Ratings

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT Rating
"""
@apiVersion 0.0.1
@api {put} /ratings/:rating-id/ 4. Update Rating
@apiName UpdateRating
@apiDescription Complete Entity update, expects all mandatory fields
@apiGroup Ratings
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PATCH User
"""
@apiVersion 0.0.1
@api {patch} ratings/:rating-id/ 5. Partially Update Rating
@apiName PartiallyUpdateRating
@apiDescription Supports partial updates.
@apiGroup Ratings
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE Rating
"""
@apiVersion 0.0.1
@api {delete} /ratings/:rating-id/ 6. Delete Rating
@apiName DeleteRating
@apiGroup Ratings
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class RatingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_fields = (
        'hackathon', 'hacker', 'rating_for', 'event', 'rating'
    )
