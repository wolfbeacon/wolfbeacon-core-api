from django.db import models
from api.models import Hacker, Hackathon, Event
from api.utils.enums import RATING_FOR, RATING_NUMS

""" 
Rating Model
"""


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Rating should be for some aspect of a Hackathon. Hence, Hackathon ID is mandatory
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    # ID of Hacker at that Hackathon who gave this rating
    hacker = models.ForeignKey(Hacker, on_delete=models.CASCADE)

    # Rating for what? Hackathon, Event, Food etc.
    rating_for = models.TextField(choices=RATING_FOR)

    # If the rating is for Event entity, ID of Event should be passed
    event = models.ForeignKey(Event, null=True)

    # Rating scale from 1 to 5
    rating = models.IntegerField(choices=RATING_NUMS)

    # One Hacker and a Hackathon cannot have more than one rating for the same 'rating_for'
    class Meta:
        unique_together = (("hacker", "hackathon", "rating_for"),)
