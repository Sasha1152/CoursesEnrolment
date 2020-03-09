import re

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def is_string(string):
    return isinstance(string, str)

def name_validator(name):
    if is_string(name):
        name = ' '.join(name.split())
    else:
        print('The "name" field should be a string type!')
        return False
    if name == '':
        print('The "name" field is required!')
        return False
    elif not re.match(r'^[A-Za-z\s-]*$', name):
        print('The name should consist of only Latin letters, hyphens and spaces!')
        return False

    print('name is valid!')
    return True


def email_validator(email):
    if not is_string(email):
        print('The "email" field should be a string type!')
        return False
    else:
        email = email.strip()
    if email == '':
        print('The "email" field is required!')
        return False
    try:
        validate_email(email)
        print('email is valid!')
        return True
    except ValidationError:
        print('E-mail is not valid!')
        return False


def phone_validator(phone_num):
    """Function that provides phone number validation"""
    if not is_string(phone_num):
        print('phone number should be a string type')
        return False

    if not re.match(r'^\+38\(0\d{2}\) \d{3}-\d{2}-\d{2}$', phone_num):
        print('phone number is not valid')
        return False

    print('phone number is valid!')
    return True
