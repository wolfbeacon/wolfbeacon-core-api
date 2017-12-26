from django.db import models
from api.models import Hackathon, User
from api.utils.enums import HACKER_ROLES, APPLICATION_STATUS

""" 
Hacker Model
-Hackers are users attending the event. Every Hackathon has it's own set of Hackers
-Hackers are linked to users and hackathons
"""


class Hacker(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    application_status = models.TextField(choices=APPLICATION_STATUS)
