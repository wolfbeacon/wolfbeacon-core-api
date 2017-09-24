from django.db import models
from api.models.user_model import User
from django.contrib.postgres.fields import JSONField
from api.utils.enums import MEMBER_ROLES

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
Junction Table between Hackathon and User table
"""


class Member(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.TextField(choices=MEMBER_ROLES)

    # new entity, add event entity id

    class Meta:
        unique_together = (("hackathon", "member"),)
