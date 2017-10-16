from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from api.models.user_model import User
from api.utils.constants import MEDIUM_FIELD_LIMIT, LONG_FIELD_LIMIT
from api.utils.enums import MEMBER_ROLES, HACKATHON_TYPE

""" 
Hackathon Model
"""


class Hackathon(models.Model):
    hackathon_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    members = models.ManyToManyField(User, through='Member')

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

    # YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ], eg 2012-09-04 06:00:00+0800
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    social_links = JSONField()
    bus_routes = JSONField()
    timetable = JSONField()
    sponsors = JSONField()
    judges = JSONField()
    speakers = JSONField()
    prizes = JSONField()


"""
Model for Membership
Acts as Junction Table between Hackathon and User table
"""


class Member(models.Model):
    hackathon_id = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    role = models.TextField(choices=MEMBER_ROLES)

    # TODO Add id link to 'events' entity

    class Meta:
        unique_together = (("hackathon_id", "user_id"),)
