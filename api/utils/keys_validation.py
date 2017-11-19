from rest_framework import validators

"""
This function takes in a list of URL ids and Request Body ids and asserts they are equal
Eg. Hacker id in URL and PUT Request Body should match
"""


def validate_keys(url_values, data_values):
    try:
        for i in range(len(url_values)):
            if int(url_values[i]) != int(data_values[i]):
                raise validators.ValidationError("id in URL and Request Body must match")
    except Exception as e:
        raise validators.ValidationError(e)
        pass
