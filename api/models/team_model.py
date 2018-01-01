from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Hackathon, Hacker
import uuid

""" 
Team Model
"""


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    search_key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    hackathon = models.ForeignKey(Hackathon)
    owner_hacker = models.OneToOneField(Hacker, related_name='+', on_delete=models.CASCADE)

    name = models.CharField(max_length=35)
    organization = models.CharField(max_length=75)

    project_link = models.URLField(null=True)


@receiver(post_save, sender=Team)
def add_owner_hacker_to_team(sender, instance, **kwargs):
    # Add Hacker to team
    owner_hacker = Hacker.objects.get(id=instance.owner_hacker.id)
    instance.hacker_set.add(owner_hacker)
