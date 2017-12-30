from django.db import models
from api.models import Hacker, Hackathon
from django.contrib.postgres.fields import JSONField

""" 
Event Model
"""


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    hackers = models.ManyToManyField(Hacker)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    type = models.TextField(choices=(
        ('mini-mlh-event', 'Mini MLH Event'),
        ('general-workshop', 'General Workshop'),
        ('company-workshop', 'Company Workshop'),
        ('speaker-session', 'Speaker Session'),
        ('fireside-chats', 'Fireside Chats'),
        ('open-source-event', 'General Open Source Event'),
        ('activity', 'General Activity'),
    ))
    name = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    location = models.CharField(max_length=100)
    giveaway = models.TextField(null=True)
    speaker_details = JSONField()
