from django.db import models
from django.contrib.postgres.fields import JSONField
from api.utils.enums import GENDER, LEVEL_OF_STUDY, TSHIRT_SIZES, DIETARY_RESTRICTIONS
from django.contrib.postgres.fields import ArrayField
from api.utils.constants import MEDIUM_FIELD_LIMIT, PHONE_FIELD_LIMIT, GRAD_YEAR_LOWER_LIMIT, LONG_FIELD_LIMIT, \
    PHONE_NUMBER_ERR_MSG
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator


class User(models.Model):
    id = models.TextField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
    pincode = models.PositiveIntegerField(null=True)
    street_address = models.CharField(max_length=LONG_FIELD_LIMIT, null=True)
    birthday = models.DateField()
    social_urls = JSONField(null=True)
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
