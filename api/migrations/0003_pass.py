# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-13 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('qr_code', models.ImageField(blank=True, editable=False, upload_to='qr_codes/')),
                ('hacker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Hacker')),
            ],
        ),
    ]
