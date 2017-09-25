from api.models.user_model import User
from api.serializers.user_serializer import UserSerializer
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import generics
from api.services import user_service
from rest_framework.response import Response

# POST User
"""
@apiVersion 0.0.1
@api {post} /users/ 1. Create User
@apiName CreateUser
@apiGroup Users

@apiParam {String} auth0_id Auth0 ID for User.
@apiParam {String{50 chars}} first_name First Name.
@apiParam {String{50 chars}} last_name Last Name.
@apiParam {String="male","female","other"} gender Gender 
@apiParam {String} email Email Id 
@apiParam {String} phone_number (Optional) Phone Number in the format example `+999999` with a max of 15 digits
@apiParam {String="high-school","undergraduate","graduate","doctoral","other"} level_of_study Indicates Level of Study
@apiParam {String{50 chars}} major_of_study College Major
@apiParam {String{50 chars}} school_last_attended (Optional) Educational Institution Attended
@apiParam {Number{1950-}} graduation_year (Optional) Year of Graduation
@apiParam {Number{1-12}} graduation_month (Optional) Month of Graduation
@apiParam {String="XS","S","M","L","XL","XXL"} tshirt_size T-Shirt Size
@apiParam {String{50 chars}} country (Optional) Country
@apiParam {String{50 chars}} city (Optional) City
@apiParam {Number} pincode (Optional) Pincode
@apiParam {String{200 chars}} street_address (Optional) Street Address
@apiParam {String="YYYY-MM-DD"} birthday Date of Birth
@apiParam {JSON} social_urls Social URLs as `{"social_platform_1":"link", "social_platform_2":"link"...}`
@apiParam {String="halal","vegetarian","vegan","gluten-free","lactose-intolerant","none"} dietary_restrictions Dietary Restrictions
@apiParam {String} special_accommodations (Optional) Special Accommodations Required
@apiParam {List} technical_interests (Optional) List of Technology sub categories Interested In
@apiParam {List} technologies (Optional) List of Technologies Interested In
@apiParam {String} about_me (Optional) Description of User and Interests
@apiParam {List} sponsors_interested_in (Optional) List of Sponsors User would like to see
@apiParam {List} prizes_interested_in (Optional) List of Prizes User would like to see
@apiParam {List} prizes_interested_in (Optional) List of Prizes User would like to see
@apiParam {List} badges_links (Optional) List of Badges User has won
@apiParam {Number} experience_points (Optional) Experience points User has been awarded
@apiParam {List} sticker_book_links (Optional) List of Links to pictures in User's Sticker Book

@apiParamExample {json} Request Data Example:
{"auth0_id":"facebook_1133","first_name":"John","last_name":"Doe","gender":"male","email":"john.doe@gmail.com","phone_number":"+999999999","level_of_study":"undergraduate","major_of_study":"Computer Science and Engineering","school_last_attended":"XYZ University","graduation_year":2018,"graduation_month":6,"tshirt_size":"XL","country":"USA","city":"Washington","birthday":"1196-04-19","social_urls":{"github":"https://github.com/bholagabbar"},"dietary_restrictions":"vegetarian","special_accommodations":"Well, nothing as such","technical_interests":["Backend","Databases"],"technologies":["Java","Python"],"about_me":"ADIDAC - All Day I Dream About Coding","sponsors_interested_in":["github","digitalocean","facebook","microsoft"],"prizes_interested_in":["holo lens","2000$ AWS Credits"]}

@apiSuccessExample {json} Success Response (HTTP/1.1 201 Created):
{"user_id":2,"auth0_id":"github_1133","created_at":"2017-09-25T16:40:17.403123Z","updated_at":"2017-09-25T16:40:17.403151Z","first_name":"Johny","last_name":"Doe","gender":"male","email":"john.doe@gmail.com","phone_number":"+999999999","level_of_study":"undergraduate","major_of_study":"Computer Science and Engineering","school_last_attended":"XYZ University","graduation_year":2018,"graduation_month":6,"tshirt_size":"XL","country":"USA","city":"Washington","birthday":"1196-04-19","social_urls":{"github":"https://github.com/bholagabbar"},"dietary_restrictions":"vegetarian","special_accommodations":"Well, nothing as such","technical_interests":["Backend","Databases"],"technologies":["Java","Python"],"about_me":"ADIDAC - All Day I Dream About Coding","sponsors_interested_in":["github","digitalocean","facebook","microsoft"],"prizes_interested_in":["holo lens","2000$ AWS Credits"],"badges_links":[],"experience_points":0,"sticker_book_links":[]}
"""

# GET ALL Users
"""
@apiVersion 0.0.1
@api {get} /users/ 2. Get all Users
@apiName GetAllUser
@apiGroup Users
@apiDescription Allowed Additional search parameters are: <br><br>
<i>user_id, auth0_id, first_name, last_name, gender, email, phone_number, level_of_study, 
major_of_study, school_last_attended, graduation_year, graduation_month,tshirt_size, 
country, city, birthday, dietary_restrictions, special_accommodations, experience_points</i><br><br>

@apiParamExample Sample Request 
https://api.wolfbeacon.com/users?city=Washington&graduation_year=2018

@apiSuccessExample {json} Success Response:
HTTP/1.1 200 OK
[{"user_id":1,"auth0_id":"facebook_1133","created_at":"2017-09-25T16:39:42.249020Z","updated_at":"2017-09-25T16:39:42.249047Z","first_name":"John","last_name":"Doe","gender":"male","email":"john.doe@gmail.com","phone_number":"+999999999","level_of_study":"undergraduate","major_of_study":"Computer Science and Engineering","school_last_attended":"XYZ University","graduation_year":2018,"graduation_month":6,"tshirt_size":"XL","country":"USA","city":"Washington","birthday":"1196-04-19","social_urls":{"github":"https://github.com/bholagabbar"},"dietary_restrictions":"vegetarian","special_accommodations":"Well, nothing as such","technical_interests":["Backend","Databases"],"technologies":["Java","Python"],"about_me":"ADIDAC - All Day I Dream About Coding","sponsors_interested_in":["github","digitalocean","facebook","microsoft"],"prizes_interested_in":["holo lens","2000$ AWS Credits"],"badges_links":[],"experience_points":0,"sticker_book_links":[]},{"user_id":2,"auth0_id":"github_1133","created_at":"2017-09-25T16:40:17.403123Z","updated_at":"2017-09-25T16:40:17.403151Z","first_name":"Johny","last_name":"Doe","gender":"male","email":"john.doe@gmail.com","phone_number":"+999999999","level_of_study":"undergraduate","major_of_study":"Computer Science and Engineering","school_last_attended":"XYZ University","graduation_year":2018,"graduation_month":6,"tshirt_size":"XL","country":"USA","city":"Washington","birthday":"1196-04-19","social_urls":{"github":"https://github.com/bholagabbar"},"dietary_restrictions":"vegetarian","special_accommodations":"Well, nothing as such","technical_interests":["Backend","Databases"],"technologies":["Java","Python"],"about_me":"ADIDAC - All Day I Dream About Coding","sponsors_interested_in":["microsoft"],"prizes_interested_in":["oculus","2000$ AWS Credits"],"badges_links":[],"experience_points":0,"sticker_book_links":[]}]

"""


class UserListAndCreate(generics.ListCreateAPIView):
    """
    List All Users, Create a new User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_fields = (
        'user_id', 'auth0_id', 'created_at', 'updated_at', 'first_name', 'last_name', 'gender', 'email', 'phone_number',
        'level_of_study', 'major_of_study', 'school_last_attended', 'graduation_year', 'graduation_month',
        'tshirt_size', 'country', 'city', 'birthday', 'dietary_restrictions', 'special_accommodations',
        'experience_points',
    )


# GET User
"""
@apiVersion 0.0.1
@api {get} /users/:user-id/ 3. Get User
@apiName GetUser
@apiGroup Users
@apiParam {Number} user-id User ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PUT User
"""
@apiVersion 0.0.1
@api {put} /users/:user-id/ 4. Update User
@apiName UpdateUser
@apiGroup Users
@apiDescription JSON field parameters remain the same as listed down in **1. Create User** 
@apiParam {Number} user-id User ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE User
"""
@apiVersion 0.0.1
@api {delete} /user/:user-id/ 5. Delete User
@apiName DeleteUser
@apiGroup Users
@apiParam {Number} id User ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class UserDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Extract id from URL and reinsert, for data safety
        request.data['id'] = self.kwargs['pk']

        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# GET User Hackathons
"""
@apiVersion 0.0.1
@api {get} /users/:id/hackathons/ 6. Get all User Hackathons
@apiName GetUserHackathons
@apiGroup Users
@apiParam {Number} id User ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""


class UserHackathons(APIView):
    """
    List All Hackathons User is a part of
    """

    def get(self, request, *args, **kwargs):
        # Get user id
        user_id = self.kwargs['pk']

        # Fetch user hackathons
        user_hackathons = user_service.get_user_hackathons(user_id)

        return Response(user_hackathons)
