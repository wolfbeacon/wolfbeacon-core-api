from django.db import models
from api.models import Hacker, Hackathon
from django.contrib.postgres.fields import JSONField
from api.utils.constants import SHORT_FIELD_LIMIT, MEDIUM_FIELD_LIMIT, LONG_FIELD_LIMIT
from api.utils.enums import EVENT_TYPE

""" 
Event Model
"""


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    hackers = models.ManyToManyField(Hacker)

    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    type = models.TextField(choices=EVENT_TYPE)
    name = models.CharField(max_length=SHORT_FIELD_LIMIT)
    tagline = models.CharField(max_length=MEDIUM_FIELD_LIMIT)
    description = models.CharField(max_length=LONG_FIELD_LIMIT)
    speaker_details = JSONField()
    location = models.CharField(max_length=MEDIUM_FIELD_LIMIT)
    giveaway = models.TextField(null=True)
