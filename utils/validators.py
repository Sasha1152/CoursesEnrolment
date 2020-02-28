import re

def phone_validator(phone_num):
    """Function that provides phone number validation"""
    try:
        if not re.match(r'^\+380\(\d{2}\)\d{7}$', phone_num):
            return False
    except (TypeError, AttributeError):
        return False

    return True

print(phone_validator('+380(67)9525445'))