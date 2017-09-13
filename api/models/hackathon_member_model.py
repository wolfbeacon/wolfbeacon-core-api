from django.db import models
from api.models.user_model import User
from django.contrib.postgres.fields import JSONField

""" 
Hackathon Model
"""


class Hackathon(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    members = models.ManyToManyField(User, through='Member')
    is_published = models.BooleanField(default=False)
    data = JSONField()

    class Meta:
        ordering = ('id',)


"""
Model for Membership
Acts as Pivot Table
"""

# Enum for roles of a Member
MEMBER_ROLES = (
    ('O', 'Organiser'),
    ('P', 'Participant'),
    ('V', 'Volunteer'),
    ('M', 'Mentor'),
)


class Member(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=MEMBER_ROLES)
