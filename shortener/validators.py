from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(url):
    url_validator = URLValidator()

    try:
        url_validator(url)
    except:
        raise ValidationError("Invalid URL!")

    return url


# Custom validator
def validate_dot_com(url):
    if not "com" in url:
        raise ValidationError("This is not valid because of no .com")
    return url
