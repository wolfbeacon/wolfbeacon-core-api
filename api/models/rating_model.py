from django.db import models
from api.models import Hacker, Hackathon, Event

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
    rating_for = models.TextField(choices=(
        ('hackathon', 'Rating for Hackathon'),
        ('event', 'Rating for Event at Hackathon'),
    ))

    # If the rating is for Event entity, ID of Event should be passed
    event = models.ForeignKey(Event, null=True)

    # Rating scale from 1 to 5
    rating = models.IntegerField(choices=(
        (1, 'Poor'),
        (2, 'Fair'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent'),
    ))

    # TODO find fix
    # One Hacker and a Hackathon cannot have more than one rating for the same 'rating_for'
    # class Meta:
    #     unique_together = (("hacker", "hackathon", "rating_for"),)
