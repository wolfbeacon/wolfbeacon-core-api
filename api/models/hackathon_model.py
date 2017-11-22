from django.db import models
from django.db.models import Count
from django.contrib.postgres.fields import JSONField
from api.utils.constants import MEDIUM_FIELD_LIMIT, LONG_FIELD_LIMIT, HACKATHON_FEATURED_LIMIT
from api.utils.enums import HACKATHON_TYPE

""" 
Hackathon Model
"""


class HackathonManager(models.Manager):
    # Featured Hackathons have 50 members or more
    def featured(self):
        return self.get_queryset().annotate(num_hackers=Count('hacker')).filter(
            num_hackers__gte=HACKATHON_FEATURED_LIMIT)


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

    objects = HackathonManager()
