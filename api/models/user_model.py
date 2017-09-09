from django.db import models

"""
User Model
"""

# Enum for roles of a user
USER_ROLES = (
    ('O', 'Organiser'),
    ('P', 'Participant'),
    ('V', 'Volunteer'),
    ('M', 'Mentor'),
)


class User(models.Model):
    id = models.EmailField(primary_key=True)
