from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from api.utils.enums import GENDER, LEVEL_OF_STUDY, TSHIRT_SIZES, DIETARY_RESTRICTIONS
from api.utils.constants import MEDIUM_FIELD_LIMIT, PHONE_FIELD_LIMIT, GRAD_YEAR_LOWER_LIMIT, LONG_FIELD_LIMIT, \
    PHONE_NUMBER_ERR_MSG, SHORT_FIELD_LIMIT
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

""" 
User Model
- User profile. More permanent data is stored here. 
- Every User has a different Hacker entity profile for different Hackathons 
"""


class User(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    auth0_id = models.TextField(unique=True)

    # Sourced from Auth0 User profile, hence TextField
    profile_picture_link = models.TextField(null=True)

    username = models.CharField(max_length=SHORT_FIELD_LIMIT)
    first_name = models.CharField(max_length=MEDIUM_FIELD_LIMIT)
    last_name = models.CharField(max_length=MEDIUM_FIELD_LIMIT)
    gender = models.TextField(choices=GENDER)
    email = models.EmailField()
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message=PHONE_NUMBER_ERR_MSG)],
                                    max_length=PHONE_FIELD_LIMIT, null=True)
    level_of_study = models.TextField(choices=LEVEL_OF_STUDY)
    major_of_study = models.CharField(max_length=MEDIUM_FIELD_LIMIT)
    school_last_attended = models.CharField(max_length=MEDIUM_FIELD_LIMIT, null=True)
    graduation_year = models.PositiveIntegerField(validators=[MinValueValidator(GRAD_YEAR_LOWER_LIMIT)], null=True)
    graduation_month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], null=True)
    tshirt_size = models.TextField(choices=TSHIRT_SIZES)
    country = models.CharField(max_length=MEDIUM_FIELD_LIMIT)
    city = models.CharField(max_length=MEDIUM_FIELD_LIMIT)
    zipcode = models.PositiveIntegerField(null=True)
    street_address = models.CharField(max_length=LONG_FIELD_LIMIT, null=True)
    birthday = models.DateField()
    social_links = JSONField(null=True)
    dietary_restrictions = models.TextField(choices=DIETARY_RESTRICTIONS)
    special_accommodations = models.TextField(null=True)
    technical_interests = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
    technologies = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
    about_me = models.TextField(null=True)
    sponsors_interested_in = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
    prizes_interested_in = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
    experience_points = models.IntegerField(default=0)
    badges_links = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
    sticker_book_links = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
