from django.db import models

"""
User Model
"""


class User(models.Model):
    id = models.TextField(primary_key=True)
