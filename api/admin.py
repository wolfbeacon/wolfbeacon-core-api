from django.contrib import admin

from api.models.hackathon_member_model import Hackathon
from api.models.hackathon_member_model import User

admin.site.register(Hackathon)
admin.site.register(User)
