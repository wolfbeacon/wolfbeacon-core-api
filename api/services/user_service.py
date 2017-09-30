from api.models import Hackathon, Member

"""
SETTERS
"""

"""
GETTERS
"""


def get_user_hackathons(user_id):
    return Member.objects.filter(member=user_id).values()
