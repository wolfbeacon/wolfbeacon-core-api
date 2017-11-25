from rest_framework import validators
from datetime import datetime

"""
This function takes in a list of URL ids and Request Body ids and asserts they are equal
Eg. Hacker id in URL and PUT Request Body should match
"""


def validate_body_url_id(url_values, data_values):
    try:
        for i in range(len(url_values)):
            if int(url_values[i]) != int(data_values[i]):
                raise Exception
    except Exception as e:
        raise validators.ValidationError(e, "id in URL and Request Body must match and be integers")


"""
This function takes in a start_date from URL and asserts format YYYY/DD/MM
"""


def validate_hackathon_url_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").date()

    except Exception as e:
        raise validators.ValidationError(e, "Date should be in format %Y-%m-%d")
