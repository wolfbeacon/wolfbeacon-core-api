# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-30 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_mentor_organizer_volunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='tagline',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='location',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='shipping_address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='hackathon',
            name='university_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='about_me',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='major_of_study',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='school_last_attended',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='special_accommodations',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='street_address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
