from rest_framework import viewsets
from api.serializers.user_serializer import UserSerializer
from api.models.user_model import User

# POST User
"""
@apiVersion 1.0.0
@api {post} /users/ 1. Create User
@apiName CreateUser
@apiGroup Users
@apiDescription See API Integration Docs - <a href="https://wolfbeacon.atlassian.net/wiki/spaces/WG/pages/283443451/Sign-up+and+Sign-in" target="_blank">Sign-up and Sign-in flow</a>. Again, User Auth0 Profile Structure Link can be found <a href="https://auth0.com/docs/user-profile/user-profile-structure" target="_blank">here</a> 

@apiParam {String} auth0_id *user_id* field in User Auth0 Profile Structure
@apiParam {String} profile_picture_link (Optional) *picture* field in User Auth0 Profile Structure which is basically a link to user's profile picture of signed in platform 
@apiParam {String{50 chars}} first_name First Name
@apiParam {String{50 chars}} last_name Last Name
@apiParam {String{50 chars}} username Username
@apiParam {String="male","female","other"} gender Gender 
@apiParam {String="YYYY-MM-DD"} birthday Date of Birth
@apiParam {String} email Email Id 
@apiParam {String} phone_number (Optional) Phone Number in the format example `+999999` with a max of 15 digits
@apiParam {String="high-school","undergraduate","graduate","doctoral","other"} level_of_study Indicates Level of Study
@apiParam {String{100 chars}} major_of_study College Major
@apiParam {String{100 chars}} school_last_attended (Optional) Educational Institution Attended
@apiParam {Number{1950-}} graduation_year (Optional) Year of Graduation
@apiParam {Number{1-12}} graduation_month (Optional) Month of Graduation
@apiParam {String{100 chars}} street_address (Optional) Street Address
@apiParam {String{75 chars}} city City
@apiParam {Number} zipcode (Optional) Zipcode
@apiParam {String{75 chars}} country Country
@apiParam {String="XS","S","M","L","XL","XXL"} tshirt_size T-Shirt Size
@apiParam {String{1000 chars}} about_me (Optional) Description of User and Interests
@apiParam {JSON} social_links Social URLs as `{"social_platform_1":"link", "social_platform_2":"link"...}`
@apiParam {String="halal","vegetarian","vegan","gluten-free","lactose-intolerant","none"} dietary_restrictions Dietary Restrictions
@apiParam {String{250 chars}} special_accommodations (Optional) Special Accommodations Required
@apiParam {List} technical_interests (Optional) List of Technology sub categories Interested In
@apiParam {List} technologies (Optional) List of Technologies Interested In
@apiParam {List} sponsors_interested_in (Optional) List of Sponsors User would like to see
@apiParam {List} prizes_interested_in (Optional) List of Prizes User would like to see
@apiParam {List} prizes_interested_in (Optional) List of Prizes User would like to see
@apiParam {List} badges_links (Optional) List of Badges User has won
@apiParam {Number} experience_points (Optional) Experience points User has been awarded
@apiParam {List} sticker_book_links (Optional) List of Links to pictures in User's Sticker Book

@apiParamExample {json} Request Data Example:
{"auth0_id":"facebook_1234","first_name":"John","last_name":"Doe","gender":"male","email":"john.doe@gmail.com","phone_number":"+999999999","level_of_study":"undergraduate","major_of_study":"Computer Science and Engineering","school_last_attended":"XYZ University","graduation_year":2018,"graduation_month":6,"tshirt_size":"XL","country":"USA","city":"Washington","birthday":"1196-04-19","social_links":{"github":"https://github.com/bholagabbar"},"dietary_restrictions":"vegetarian","special_accommodations":"Well, nothing as such","technical_interests":["Backend","Databases"],"technologies":["Java","Python"],"about_me":"ADIDAC - All Day I Dream About Coding","sponsors_interested_in":["github","digitalocean","facebook","microsoft"],"prizes_interested_in":["holo lens","2000$ AWS Credits"]}

@apiSuccessExample {json} Success Response Code:
HTTP/1.1 201 Created

"""

# GET ALL Users
"""
@apiVersion 1.0.0
@api {get} /users/ 2. List Users
@apiName ListUser
@apiGroup Users
@apiDescription Allowed Additional search parameters are: <br><br>
<i>user_id, auth0_id, first_name, last_name, gender, email, phone_number, level_of_study, 
major_of_study, school_last_attended, graduation_year, graduation_month,tshirt_size, 
country, city, birthday, dietary_restrictions, special_accommodations, experience_points</i><br><br>

@apiParamExample Sample Request 
https://api.wolfbeacon.com/users?city=Washington&graduation_year=2018

@apiSuccessExample {json} Success Response (HTTP/1.1 200 OK):
[{"user_id":1,"auth0_id":"facebook_1133","created_at":"2017-09-25T16:39:42.249020Z","updated_at":"2017-09-25T16:39:42.249047Z","first_name":"John","last_name":"Doe","gender":"male","email":"john.doe@gmail.com","phone_number":"+999999999","level_of_study":"undergraduate","major_of_study":"Computer Science and Engineering","school_last_attended":"XYZ University","graduation_year":2018,"graduation_month":6,"tshirt_size":"XL","country":"USA","city":"Washington","birthday":"1196-04-19","social_links":{"github":"https://github.com/bholagabbar"},"dietary_restrictions":"vegetarian","special_accommodations":"Well, nothing as such","technical_interests":["Backend","Databases"],"technologies":["Java","Python"],"about_me":"ADIDAC - All Day I Dream About Coding","sponsors_interested_in":["github","digitalocean","facebook","microsoft"],"prizes_interested_in":["holo lens","2000$ AWS Credits"],"badges_links":[],"experience_points":0,"sticker_book_links":[],"hackathons":[{"hackathon":4}]},{"user_id":2,"auth0_id":"github_1133","created_at":"2017-09-25T16:40:17.403123Z","updated_at":"2017-09-25T16:40:17.403151Z","first_name":"Johny","last_name":"Doe","gender":"male","email":"john.doe@gmail.com","phone_number":"+999999999","level_of_study":"undergraduate","major_of_study":"Computer Science and Engineering","school_last_attended":"XYZ University","graduation_year":2018,"graduation_month":6,"tshirt_size":"XL","country":"USA","city":"Washington","birthday":"1196-04-19","social_links":{"github":"https://github.com/bholagabbar"},"dietary_restrictions":"vegetarian","special_accommodations":"Well, nothing as such","technical_interests":["Backend","Databases"],"technologies":["Java","Python"],"about_me":"ADIDAC - All Day I Dream About Coding","sponsors_interested_in":["github","digitalocean","facebook","microsoft"],"prizes_interested_in":["holo lens","2000$ AWS Credits"],"badges_links":[],"experience_points":0,"sticker_book_links":[],"hackathons":[]}]
"""

# GET User
"""
@apiVersion 1.0.0
@api {get} /users/:user-id/ 3. Get User
@apiName GetUser
@apiGroup Users
@apiSuccessExample {json} Success Response (HTTP/1.1 200 OK):
{"id":7,"auth0_id":"facebook_1234","created_at":"2017-09-30T19:19:38.450302Z","updated_at":"2017-09-30T19:19:38.450330Z","first_name":"John","last_name":"Doe","gender":"male","email":"john.doe@gmail.com","phone_number":"+999999999","level_of_study":"undergraduate","major_of_study":"Computer Science and Engineering","school_last_attended":"XYZ University","graduation_year":2018,"graduation_month":6,"tshirt_size":"XL","country":"USA","city":"Washington","birthday":"1196-04-19","social_links":{"github":"https://github.com/bholagabbar"},"dietary_restrictions":"vegetarian","special_accommodations":"Well, nothing as such","technical_interests":["Backend","Databases"],"technologies":["Java","Python"],"about_me":"ADIDAC - All Day I Dream About Coding","sponsors_interested_in":["github","digitalocean","facebook","microsoft"],"prizes_interested_in":["holo lens","2000$ AWS Credits"],"badges_links":[],"experience_points":0,"sticker_book_links":[],"hackathons":[{"hackathon":1}]}
"""

# PUT User
"""
@apiVersion 1.0.0
@api {put} /users/:user-id/ 4. Replace User
@apiName ReplaceUser
@apiGroup Users
@apiDescription Complete Entity update, expects all mandatory fields 
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# PATCH User
"""
@apiVersion 1.0.0
@api {patch} /users/:user-id/ 5. Update User
@apiName UpdateUser
@apiGroup Users
@apiDescription Supports partial updates 
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 200 OK
"""

# DELETE User
"""
@apiVersion 1.0.0
@api {delete} /user/:user-id/ 6. Delete User
@apiName DeleteUser
@apiGroup Users
@apiParam {Number} id User ID.
@apiSuccessExample {json} Success Response Code:
HTTP/1.1 204 NO CONTENT
"""


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = (
        'id', 'auth0_id', 'username', 'first_name', 'last_name', 'gender', 'email',
        'phone_number', 'level_of_study', 'major_of_study', 'school_last_attended', 'graduation_year',
        'graduation_month', 'tshirt_size', 'country', 'city', 'zipcode', 'birthday', 'dietary_restrictions',
        'special_accommodations', 'experience_points',
    )
