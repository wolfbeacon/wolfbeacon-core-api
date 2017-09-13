from api.models.hackathon_member_model import Hackathon
from django.db.models import Count

"""
SETTERS
"""

"""
GETTERS
"""


def get_featured_hackathons():
    featured_hackathon = (Hackathon.objects.annotate(num_members=Count('members')).filter(members__gt=5))
    return featured_hackathon
