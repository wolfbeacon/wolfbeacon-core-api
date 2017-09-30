from api.models import Hackathon
from django.db.models import Count

"""
SETTERS
"""

"""
GETTERS
"""


# Returns all featured algorithm. Currently hackathons > 50
def filter_featured_hackathons():
    featured_hackathon = (Hackathon.objects.annotate(num_members=Count('members')).filter(members__gt=50))
    return featured_hackathon.values()
