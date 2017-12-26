from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from api.models import Hacker
from io import BytesIO

import qrcode
import json


class Pass(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    qr_code = models.ImageField(upload_to='qr_codes/', editable=False, blank=True)
    hacker = models.OneToOneField(Hacker, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):

        try:
            # Retrieve Hacker Details
            hacker = Hacker.objects.get(id=self.hacker_id)
            qr_data = {
                'hacker_id': hacker.id,
                'user_id': hacker.user.id,
                'auth0_user_id': hacker.user.auth0_id,

                'first_name': hacker.user.first_name,
                'last_name': hacker.user.last_name,
            }

            # Embed data in QR
            str_qr_data = json.dumps(qr_data)
            img = qrcode.make(str_qr_data)

            # Convert from PIL to Django Format
            img_io = BytesIO()
            img.save(img_io, format='JPEG')
            file_name = 'qr_code_hacker_{}_hackathon_{}.jpg'.format(hacker.id, hacker.hackathon_id)
            self.qr_code = InMemoryUploadedFile(img_io, None, file_name, 'image/jpeg', img_io.tell(), None)

            # Save (Upload QR if generated)
            super(Pass, self).save()

        except Exception as e:
            print(e, "Could not generate Hacker pass")
