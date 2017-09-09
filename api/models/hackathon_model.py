from django.db import models
from api.models.user_model import User, USER_ROLES
from django.contrib.postgres.fields import JSONField

""" 
Hackathon Model
"""


class Hackathon(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    data = JSONField()
    organiser_email_id = models.EmailField()
    users = models.ManyToManyField(User, through='Membership')
    is_published = models.BooleanField(default=False)


"""
Model for Membership
Acts as Pivot Table
"""


class Membership(models.Model):
    hackathon_id = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=USER_ROLES)
