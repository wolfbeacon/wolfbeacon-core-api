from django.db import models


class Upload(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    datafile = models.FileField(upload_to='other/')
