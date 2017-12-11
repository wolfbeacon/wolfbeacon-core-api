from django.db import models


class FileUpload(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    datafile = models.FileField()
