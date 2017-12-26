from django.db import models
from api.models import Hackathon, User

""" 
Volunteer Model
-Volunteers are users organizing the event. Every Hackathon has it's own set of Organizer
"""


class Volunteer(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    # Eg Photographer, Guide etc
    duty_assigned = models.TextField(null=True)

