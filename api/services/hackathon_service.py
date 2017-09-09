from api.models.hackathon_model import Hackathon
from api.models.user_model import User
from django.db.transaction import atomic


@atomic
def create_hackathon_upserting_user(serialized_hackathon, user_id):
    serialized_hackathon.save()
    User.objects.get_or_create(id=user_id)

