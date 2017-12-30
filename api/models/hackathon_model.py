from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import Count

""" 
Hackathon Model
"""


class HackathonQueryset(models.query.QuerySet):
    # Current condition for Featured Hackathons is having >= 50 members - set by HACKATHON_FEATURED_LIMIT
    def featured(self):
        return self.annotate(num_hackers=Count('hacker')).filter(
            num_hackers__gte=50)

    def start_date(self, start_date):
        return self.filter(start__date__gte=start_date)

    def end_date(self, end_date):
        return self.filter(end__date__lte=end_date)


class HackathonManager(models.Manager):
    def get_queryset(self):
        return HackathonQueryset(self.model)

    def featured(self):
        return self.get_queryset().featured()

    def start_date(self, start_date):
        return self.get_queryset().start_date(start_date=start_date)

    def end_date(self, end_date):
        return self.get_queryset().end_date(end_date=end_date)


class Hackathon(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    name = models.CharField(max_length=100)
    version = models.PositiveIntegerField(default=1)
    description = models.TextField()
    logo_image_file = models.ImageField(upload_to='hackathon_logos/', null=True)
    hackathon_type = models.TextField(choices=(
        ('high-school', 'High School Hackathon'),
        ('university', 'University Level Hackathon'),
        ('corporate', 'Corporate Level Hackathon'),
        ('other', 'Other')
    ))
    location = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    shipping_address = models.CharField(max_length=150)
    travel_reimbursements = models.TextField()
    university_name = models.CharField(max_length=100, null=True)
    contact_email = models.EmailField()

    start = models.DateTimeField()
    end = models.DateTimeField()
    social_links = JSONField()
    bus_routes = JSONField()
    timetable = JSONField()
    sponsors = JSONField()
    judges = JSONField()
    speakers = JSONField()
    prizes = JSONField()

    # Link to HackathonManager
    objects = HackathonManager()
