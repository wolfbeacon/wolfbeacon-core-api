import requests

BASE_URL = 'http://localhost:8000/v1/'


def add_hackathon():
    url = BASE_URL + 'hackathons/'
    res = requests.post(url, json={
        "name": "Hack The Valley",
        "description": "Hackathon at UoT Scarborough",
        "logo": "hello://google.com",
        "hackathon_type": "university",
        "location": "Toronto, ON",
        "latitude": 43.6532,
        "longitude": 79.3832,
        "shipping_address": "Road 123, Toronto, Canada",
        "travel_reimbursements": "Yes, depending on location",
        "university_name": "University Of Toronto",
        "contact_email": "ralphpal@wolfbeacon.com",
        "start": "2017-10-10 06:00:00+0000",
        "end": "2017-10-14 06:00:00+0000",
        "social_links": {
            "facebook": "https://facebook.com/htv",
            "twitter": "https://twitter.com/hackthevalley"
        },
        "bus_routes": {},
        "timetable": {},
        "sponsors": {},
        "judges": {},
        "speakers": {},
        "prizes": {}
    })
    print(res.status_code)


def add_user():
    url = BASE_URL + 'users/'
    res = requests.post(url, json={
        "auth0_id": "facebook_1234",
        "first_name": "John",
        "last_name": "Doe",
        "gender": "male",
        "username": "johndoe123",
        "email": "john.doe@gmail.com",
        "phone_number": "+999999999",
        "level_of_study": "undergraduate",
        "major_of_study": "Computer Science and Engineering",
        "school_last_attended": "XYZ University",
        "graduation_year": 2018,
        "graduation_month": 6,
        "tshirt_size": "XL",
        "country": "USA",
        "city": "Washington",
        "birthday": "1196-04-19",
        "social_links": {
            "github": "https://github.com/bholagabbar"
        },
        "dietary_restrictions": "vegetarian",
        "special_accommodations": "Well, nothing as such",
        "technical_interests": [
            "Backend",
            "Databases"
        ],
        "technologies": [
            "Java",
            "Python"
        ],
        "about_me": "ADIDAC - All Day I Dream About Coding",
        "sponsors_interested_in": [
            "github",
            "digitalocean",
            "facebook",
            "microsoft"
        ],
        "prizes_interested_in": [
            "holo lens",
            "2000$ AWS Credits"
        ]
    })
    print(res.status_code)


def add_event():
    url = BASE_URL + 'hackathons/1/events/'
    res = requests.post(url, json={
        "hackathon": 1,
        "name": "Test Name",
        "type": "general-workshop",
        "tagline": "Test Workshop",
        "description": "Test Description",
        "speaker_details": {},
        "location": "Building A",
        "giveaway": "Tshirt"
    })
    print(res.status_code)


def add_hacker():
    url = BASE_URL + 'hackathons/1/hackers/'
    res = requests.post(url, json={
        "user": 1,
        "hackathon": 1,
        "role": "organiser"
    })
    print(res.status_code)


def add_hacker_to_event():
    url = BASE_URL + 'hackathons/1/events/1/hackers/1/'
    res = requests.post(url)
    print(res.status_code)


add_hackathon()
add_user()
add_event()
add_hacker()
add_hacker_to_event()
