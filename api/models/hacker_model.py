from django.db import models
from api.models import Hackathon, User
from api.utils.enums import HACKER_ROLES

""" 
Hackathon Model
"""


class Hacker(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    role = models.TextField(choices=HACKER_ROLES)

    class Meta:
        unique_together = (("user", "hackathon"),)
