from django.db import models
from api.models import Hackathon, User

""" 
Hacker Model
-Hackers are users attending the event. Every Hackathon has it's own set of Hackers
-Hackers are linked to users, hackathons and teams
"""


class Hacker(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    team = models.ForeignKey('api.Team', null=True, on_delete=models.SET_NULL)

    application_status = models.TextField(choices=(
        ('accepted', 'Accepted'),
        ('wait-listed', 'Wait Listed'),
        ('applied', 'Applied'),
        ('rejected', 'Rejected'),
    ))
