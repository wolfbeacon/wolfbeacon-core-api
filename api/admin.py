from django.contrib import admin

from api.models.hackathon_model import Hackathon
from api.models.hackathon_model import User

admin.site.register(Hackathon)
admin.site.register(User)
