from django.db import models
from django.contrib.postgres.fields import JSONField
from api.utils.constants import MEDIUM_FIELD_LIMIT, LONG_FIELD_LIMIT
from api.utils.enums import HACKATHON_TYPE

""" 
Hackathon Model
"""


class Hackathon(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    name = models.CharField(max_length=MEDIUM_FIELD_LIMIT)
    version = models.PositiveIntegerField(default=1)
    description = models.TextField()
    logo = models.TextField(null=True)
    hackathon_type = models.TextField(choices=HACKATHON_TYPE)
    location = models.CharField(max_length=LONG_FIELD_LIMIT)
    shipping_address = models.CharField(max_length=LONG_FIELD_LIMIT)
    travel_reimbursements = models.TextField()
    university_name = models.CharField(max_length=LONG_FIELD_LIMIT, null=True)
    contact_email = models.EmailField()

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    social_links = JSONField()
    bus_routes = JSONField()
    timetable = JSONField()
    sponsors = JSONField()
    judges = JSONField()
    speakers = JSONField()
    prizes = JSONField()

