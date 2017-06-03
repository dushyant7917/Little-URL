from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(url):
    url_validator = URLValidator()
    reg_url = url

    if "http" in reg_url:
        new_url = reg_url
    else:
        new_url = "http://" + url

    try:
        url_validator(new_url)
    except:
        raise ValidationError("Invalid URL!")

    return new_url


# Custom validator
def validate_dot_com(url):
    if not "com" in url:
        raise ValidationError("This is not valid because of no .com")
    return url
