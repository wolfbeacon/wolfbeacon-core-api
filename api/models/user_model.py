from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
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

    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.TextField(choices=(
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ))
    birthday = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\+?1?\d{9,15}$',
                       message="Phone number format: '+999999999'. Max 15 digits allowed.")], null=True)
    level_of_study = models.TextField(choices=(
        ('high-school', 'High School'),
        ('undergraduate', 'Undergraduate'),
        ('graduate', 'Graduate'),
        ('doctoral', 'PhD'),
        ('other', 'Other'),
    ))
    major_of_study = models.CharField(max_length=100)
    school_last_attended = models.CharField(max_length=100, null=True)
    graduation_year = models.PositiveIntegerField(validators=[MinValueValidator(1950)], null=True)
    graduation_month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], null=True)
    street_address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=75)
    zipcode = models.PositiveIntegerField(null=True)
    country = models.CharField(max_length=75)
    tshirt_size = models.TextField(choices=(
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ))
    about_me = models.CharField(max_length=1000, null=True)
    social_links = JSONField(null=True)
    dietary_restrictions = models.TextField(choices=(
        ('halal', 'Halal'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('gluten-free', 'Gluten-free'),
        ('lactose-intolerant', 'Lactose Intolerant'),
        ('kosher', 'Kosher'),
        ('none', 'None'),
    ))
    special_accommodations = models.CharField(max_length=250, null=True)
    technical_interests = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
    technologies = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
    sponsors_interested_in = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
    prizes_interested_in = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
    experience_points = models.IntegerField(default=0)
    badges_links = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
    sticker_book_links = ArrayField(models.TextField(blank=False, null=False), blank=True, default=list)
